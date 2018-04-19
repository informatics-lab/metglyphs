# MetGlyphs

A small libary which bundles sets of weather glyphs/icons/symbols with useful code to convert between image types for data visualisation and plotting.

When retrieving data from the multitude of weather APIs that are available you often get the weather represented by a code, however the codes are often inconsistent between services. This package allows you to simply convert the codes into glyphs/icons/symbols for use in your plots or applications.


## Getting started

```bash
pip install metglyphs
```

```python
# Import the GlyphSet constructor
from metglyphs import GlyphSet

# Create a new set object
glyphs = GlyphSet()

# Get a glyph for a given weather code
glyph = glyphs.get_glyph(datapoint_code="10")
```

A `glyph` object can provide an SVG byte string, PNG byte string, or NumPy array of RGB values for you to use however you like.

```python
# SVG
glyph.to_svg()

# PNG
glyph.to_png()

# NumPy array
glyph.to_np_array()
```


## Supported services

This library currently supports the following weather codes.

| Provider | Example |
| -------- | ------- |
| [Met Office Datapoint](https://www.metoffice.gov.uk/datapoint) | `GlyphSet().get_glyph(datapoint_code=<code>)` |


## Glyph sets

All glyphs/symbols/icons bundled in this library are open source and free to use provided you adhere to the terms of their respective licenses. 

To use them import the constant for the set you want and then pass it to your `GlyphSet` object when you construct it.

```python
from metglyphs import GlyphSet
from metglyphs.glyphs import DEFAULT_GLYPHS

glyphs = GlyphSet(name=DEFAULT_GLYPHS)
```

| Set Name | Constant | Provider | Colour type | Colours | License |
| -------- | -------- | -------- | ----------- | ------- | ------- |
| Met Office | `MET_OFFICE_GLYPHS` (also `DEFAULT_GLYPHS`) | [Met Office](https://www.metoffice.gov.uk/) | Full colour | TBC | None |
| yr.no | `YRNO_GLYPHS` | [yr.no](https://www.yr.no/) ([NRK](https://www.nrk.no) and [MET Norway](https://www.met.no)) | Full colour | TBC | [MIT](https://opensource.org/licenses/MIT) |
| weathericons.io | `WEATHER_ICONS_IO_GLYPHS` | [Eric Flowers](http://www.twitter.com/erik_flowers) | Monochrome | `#9150a1` | [SIL OFL 1.1](http://scripts.sil.org/OFL)


## Code reference

A combined subset of the [WMO 4677](http://www.wmo.int/pages/prog/www/WMOCodes/WMO306_vI1/Publications/2017update/Sel9.pdf) and [WMO 4680](http://weatherfaqs.org.uk/book/export/html/150) code references is used by this library. This creates a common translation layer between data APIs and glyph sets. 

Despite these codes being detailed they were designed for recording observations from manned and unmanned sites respectively. Therefore it is still not always obvious which glyph represents which code, so along with the official description of the code I have included a simple description and glyph suggestion which explains how I have interpreted it.

| Day Code | Night Code | Original set  | Official Description | Simple Description | Suggested symbol |
| -------- | ---------- | ------------- | -------------------- | ------------------ | ---------------- |
| 00d      | 00n        | WMO 4677      | Cloud development not observed or not observable | No clouds, clear blue sky | Sun/moon |
| 01d      | 01n        | WMO 4680      | Clouds generally dissolving or becoming less developed | Partial cloud with clear breaks | Cloud with sun/moon |
| 03d      | 03n        | WMO 4680      | Clouds forming or developing | Cloudy | Light cloud |
| 10d      | 10n        | WMO 4680      | Mist | Mist | Cloud with bars or word mist |
| 14d      | 14n        | WMO 4677      | Precipitation within sight, not reaching the ground or the surface of the sea | Dark clouds, precipitation* imminent but not falling yet | Dark cloud |
| 18d      | 18n        | WMO 4680      | Squalls | Wind | Wind lines |
| 30d      | 30n        | WMO 4680      | Fog | Fog | Cloud with bars or word fog |
| 50d      | 50n        | WMO 4680      | Drizzle | Drizzle | Cloud with small rain drops |
| 60d      | 60n        | WMO 4680      | Rain | Rain | Cloud with rain drops |
| 63d      | 63n        | WMO 4680      | Rain, not freezing - heavy | Heavy rain | Cloud with big/many rain drops |
| 65d      | 65n        | WMO 4680      | Freezing rain - moderate | Sleet | Cloud with rain drop and ice |
| 70d      | 70n        | WMO 4680      | Snow | Snow | Cloud with snowflake |
| 75d      | 75n        | WMO 4680      | Ice Pellets - moderate | Hail | Cloud with hail stones |
| 81d      | 81n        | WMO 4680      | Intermittent rain - slight | Light rain showers | Cloud with sun/moon and rain drop |
| 83d      | 83n        | WMO 4680      | Intermittent rain - heavy | Heavy rain showers | Cloud with sun/moon and multiple rain drops |
| 85d      | 85n        | WMO 4680      | Intermittent snow - slight | Light snow showers | Cloud with sun/moon and snow flake |
| 87d      | 87n        | WMO 4680      | Intermittent snow - heavy | Heavy snow showers | Cloud with sun/moon and multiple snow flakes |
| 89d      | 89n        | WMO 4680      | Hail | Hail showers | Cloud with sun/moon and hail stone |
| 90d      | 90n        | WMO 4680      | Thunderstorm | Thunderstorm without rain | Dark cloud with lightening bolt |
| 95d      | 95n        | WMO 4680      | Thunderstorm, heavy - rain/snow showers | Thunderstorm with rain showers | Dark cloud with sun/moon, ligitening bolt and rain drop |

_*precipitation = rain, sleet, snow, hail, etc_

All glyph sets should provide a symbol for every code, even if they are duplicated (e.g a dark cloud for 14d and 14n). Data providers will most likely use a subset of codes and therefore a subset of symbols.

## Changing colours

It is possible to recolour your glyph sets. You can do this by providing the `recolor` kwarg in `GlyphSet` or `GlyphSet.get_glyph` with a dictionary in the format of `{"old hex value": "new hex value"}`. Some sets are monochrome and so you only need to change one colour, others are full colour and you should be able to change individual colours to your liking. See the table of sets above for information on which colours to replace.

For example

```python
# This will replace blue with green in all glyphs in this set
glyphs = GlyphSet(recolor={"#0000FF", "#00FF00"})

# This will change the thunder glyph to red 
# (note that we are still replacing blue as recoloring is done at render time)
thunder_glyph = glyphs.get_glyph(datapoint_code='30', recolor={"#0000FF", "#FF0000"}
```

![Recoloured glyphs](https://images.informaticslab.co.uk/misc/8b125b1dbbac150e46ce2660f02ec2eb.png)

## Useful links from Chris Little
https://external.opengeospatial.org/twiki_public/MetOceanDWG/WebHome
https://external.opengeospatial.org/twiki_public/MetOceanDWG/WMOandICAOstyles
https://github.com/OGCMetOceanDWG/WorldWeatherSymbols
http://artefacts.ceda.ac.uk/badc_datadocs/surface/code.html
http://codes.wmo.int/
