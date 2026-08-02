#!/usr/bin/env python3
"""Extract latitude and longitude from HousingAnywhere listing pages."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from html.parser import HTMLParser
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen


USER_AGENT = "Mozilla/5.0 (compatible; HousingAnywhereCoordinateExtractor/1.0)"


class JsonLdParser(HTMLParser):
    """Collect JSON-LD script contents from an HTML document."""

    def __init__(self) -> None:
        super().__init__()
        self._inside_json_ld = False
        self._buffer: list[str] = []
        self.documents: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "script":
            return
        attributes = {key.lower(): value for key, value in attrs}
        if attributes.get("type", "").lower() == "application/ld+json":
            self._inside_json_ld = True
            self._buffer = []

    def handle_data(self, data: str) -> None:
        if self._inside_json_ld:
            self._buffer.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "script" and self._inside_json_ld:
            self.documents.append("".join(self._buffer))
            self._inside_json_ld = False
            self._buffer = []


def find_coordinates(value: Any) -> tuple[float, float] | None:
    """Recursively find a GeoCoordinates object in decoded JSON."""
    if isinstance(value, dict):
        kind = value.get("@type")
        kinds = kind if isinstance(kind, list) else [kind]
        if "GeoCoordinates" in kinds and "latitude" in value and "longitude" in value:
            return float(value["latitude"]), float(value["longitude"])
        for child in value.values():
            result = find_coordinates(child)
            if result is not None:
                return result
    elif isinstance(value, list):
        for child in value:
            result = find_coordinates(child)
            if result is not None:
                return result
    return None


def extract_coordinates(html: str) -> tuple[float, float]:
    parser = JsonLdParser()
    parser.feed(html)

    for document in parser.documents:
        try:
            result = find_coordinates(json.loads(document))
        except (json.JSONDecodeError, TypeError, ValueError):
            continue
        if result is not None:
            return result

    # Fallback for coordinates in the page's serialized application state.
    match = re.search(
        r'"latitude"\s*:\s*"?(-?\d+(?:\.\d+)?)"?\s*,\s*'
        r'"longitude"\s*:\s*"?(-?\d+(?:\.\d+)?)"?',
        html,
    )
    if match:
        return float(match.group(1)), float(match.group(2))

    raise ValueError("no coordinates found in page")


def fetch(url: str, timeout: float) -> str:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not (
        parsed.hostname == "housinganywhere.com"
        or (parsed.hostname or "").endswith(".housinganywhere.com")
    ):
        raise ValueError("not a HousingAnywhere URL")

    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html"})
    with urlopen(request, timeout=timeout) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def main() -> int:
    argument_parser = argparse.ArgumentParser(description=__doc__)
    argument_parser.add_argument("urls", nargs="+", help="HousingAnywhere listing URLs")
    argument_parser.add_argument("--timeout", type=float, default=20, help="request timeout in seconds")
    args = argument_parser.parse_args()

    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow(("url", "latitude", "longitude", "error"))
    failed = False
    for url in args.urls:
        try:
            latitude, longitude = extract_coordinates(fetch(url, args.timeout))
            writer.writerow((url, latitude, longitude, ""))
        except (HTTPError, URLError, TimeoutError, ValueError, OSError) as error:
            failed = True
            writer.writerow((url, "", "", str(error)))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
