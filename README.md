# Berlin apartment notes

## Extract HousingAnywhere coordinates

Use `housinganywhere_coordinates.py` to extract latitude and longitude from one
or more HousingAnywhere listing URLs. Pass every URL as a separate argument:

```bash
./housinganywhere_coordinates.py \
  "https://housinganywhere.com/room/ut551278/de/Berlin/k-penicker-stra-e" \
  "https://housinganywhere.com/room/ANOTHER_LISTING"
```

The command writes CSV to standard output with these columns:

```text
url,latitude,longitude,error
```

Save the results when needed:

```bash
./housinganywhere_coordinates.py "URL_1" "URL_2" > coordinates.csv
```

For Codex: when asked to find coordinates for HousingAnywhere links, run this
script with all supplied links as positional arguments. No Python packages are
required. A failed listing gets an error in its CSV row, and the script exits
with status 1 if any listing failed.
