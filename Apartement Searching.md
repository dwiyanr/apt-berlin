---
aliases:
  - Berlin apartment search map
tags:
  - berlin
  - map
  - housing-research
---

# Berlin apartment search

Use this map to compare apartment locations, transport access, commute to the office, and factors worth checking during a viewing.

```leaflet
id: berlin-kbo-caution-areas
height: 650px
lat: 52.52
long: 13.405
minZoom: 9
maxZoom: 19
defaultZoom: 11
zoomFeatures: true
unit: meters
geojson:
  - [[berlin_districts_leaflet.geojson]]|Berlin districts
  - [[berlin_kbo_caution_leaflet.geojson]]|kbO caution areas
  - [[berlin_lower_severity_caution_leaflet.geojson]]|Lower-severity caution areas
  - [[berlin-ubahn-lines.geojson]]|Berlin U-Bahn lines
markerFile: [[Office]]
draw: false
noScrollZoom: true
```

Toggle layers in the map's top-right corner and hover over features for details. Use the U-Bahn network and office marker to estimate a listing's commute; the red and amber areas are prompts for closer research, not automatic reasons to reject an apartment.

| Layer | Use when comparing apartments |
| --- | --- |
| District boundaries | Identify the district and local administration |
| Red kbO areas | Check the exact street and immediate surroundings |
| Amber areas | Check nightlife, crowds, and evening noise |
| U-Bahn lines | Estimate connections and commute options |
| Office marker | Compare travel time to Hausvogteiplatz 3–4 |

## Viewing checklist

- Check the route to work and the nearest late-night transport.
- Visit the block during the day and on a weekend evening.
- Note street noise, nearby venues, and bedroom orientation.
- Evaluate the building and exact street rather than judging the wider neighborhood.

## Map notes

The red polygons are police-designated *kriminalitätsbelastete Orte* (kbO), effective 1 July 2026. The amber polygons are approximate housing-research zones around RAW/Revaler Straße and Simon-Dach-Straße/Boxhagener Platz, focused mainly on nightlife and noise. Neither layer describes every building or resident within it.

District boundaries come from the [official Berlin ALKIS WFS](https://daten.berlin.de/datensaetze/alkis-berlin-bezirke-wfs-ced31d7d). U-Bahn routes U1–U9 connect VBB GTFS station coordinates and are for orientation rather than precise track geometry.
