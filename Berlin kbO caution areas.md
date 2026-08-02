---
aliases:
  - Berlin warning areas
tags:
  - berlin
  - map
  - housing-research
---

# Berlin kbO caution areas

> [!warning] Interpretation
> These polygons are a caution and inspection layer for housing research. They do not mean that every street, building, or resident inside an outlined area is unsafe.

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
draw: false
noScrollZoom: true
```

The blue-gray outlines show Berlin's 12 administrative districts; the red polygons show the seven areas contained in [[berlin_kbo_caution_leaflet.geojson|the kbO GeoJSON layer]]; the amber polygons show the approximate, lower-severity housing inspection zones in [[berlin_lower_severity_caution_leaflet.geojson|the lower-severity caution layer]]; and the colored routes show the U1–U9 lines from [[berlin-ubahn-lines.geojson|the Berlin U-Bahn GeoJSON layer]]. Hover over a feature to see its details. Use the layer control in the map's top-right corner to toggle any dataset, and use the other controls to pan and zoom.

| Layer | Meaning |
| --- | --- |
| Blue-gray outline | Berlin district boundary |
| Red outline and fill | kbO caution area |
| Amber outline and fill | Approximate lower-severity housing caution area |
| Colored line | U-Bahn route, using its official line color |

## kbO areas

- Alexanderplatz
- Rigaer Straße
- Warschauer Brücke
- Görlitzer Park/Wrangelkiez
- Kottbusser Tor
- Hermannplatz/Donaukiez
- Hermannstraße/Bhf Neukölln

## Lower-severity areas

- RAW-Gelände / Revaler Straße
- Simon-Dach-Straße / Boxhagener Platz

## Data note

The GeoJSON describes these as police-designated *kriminalitätsbelastete Orte* (kbO). Its metadata says the boundaries were digitized from Polizei Berlin maps published on 19 January 2026 and that the seven-area list took effect on 1 July 2026. Treat the boundaries as an orientation aid and verify important decisions against the current official source.

The lower-severity layer in [[berlin_lower_severity_caution_leaflet.geojson]] contains two approximate inspection zones based on nightlife, noise, and crowd considerations. These are interpretive housing-research areas, not official police or statistical crime boundaries. Check the exact building and surrounding streets at the times described in each feature's details.

The district layer in [[berlin_districts_leaflet.geojson]] contains all 12 *Bezirke*. It was retrieved on 2 August 2026 from the [official Berlin ALKIS district-boundary WFS](https://daten.berlin.de/datensaetze/alkis-berlin-bezirke-wfs-ced31d7d) and lightly simplified for responsive display. The source dataset is licensed under Datenlizenz Deutschland – Zero – Version 2.0.

The U-Bahn layer in [[berlin-ubahn-lines.geojson]] contains routes U1–U9. Its paths connect VBB GTFS station coordinates in service order and are intended as an orientation aid, not as engineering-grade track centerlines. The data is attributed to Verkehrsverbund Berlin-Brandenburg (VBB) under CC BY 4.0.
