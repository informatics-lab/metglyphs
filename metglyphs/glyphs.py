"""Glyph set names and lookup tables for glyph file names."""

# Constants for available set names
YRNO_GLYPHS = 'yrno'
MET_OFFICE_GLYPHS = 'metoffice'
WEATHER_ICONS_IO_GLYPHS = 'weathericonsio'
DEFAULT_GLYPHS = MET_OFFICE_GLYPHS


# Lookup tables for wmo code to filename for each glyph set
# Paths are relative to assets/<set_name>/
WMO_GLYPH_LOOKUP = {
    YRNO_GLYPHS: {
        "00d": "01d.1.svg",
        "00n": "01n.1.svg",
        '01d': '02d.1.svg',
        '01n': '02n.1.svg',
        '03d': '04.1.svg',
        '10d': '15.1.svg',
        '14d': '15.1.svg',
        '30d': '15.1.svg',
        '50d': '46.1.svg',
        '60d': '09.1.svg',
        '63d': '10.1.svg',
        '65d': '12.1.svg',
        '65n': '12.1.svg',
        '70d': '13.1.svg',
        '75d': '48.1.svg',
        '81d': '05d.1.svg',
        '81n': '05n.1.svg',
        '83d': '41d.1.svg',
        '83n': '41n.1.svg',
        '85d': '08d.1.svg',
        '85n': '08n.1.svg',
        '87d': '45d.1.svg',
        '87n': '45n.1.svg',
        '89d': '43d.1.svg',
        '89n': '43n.1.svg',
        '90d': '30.1.svg',
        '95d': '25d.1.svg',
        '95n': '25n.1.svg'
    },
    MET_OFFICE_GLYPHS: {
        "00d": "1.svg",
        "00n": "0.svg",
        '01d': '3.svg',
        '01n': '2.svg',
        '03d': '7.svg',
        '10d': '5.svg',
        '14d': '8.svg',
        '30d': '5.svg',
        '50d': '11.svg',
        '60d': '10.svg',
        '63d': '15.svg',
        '65d': '17.svg',
        '65n': '16.svg',
        '70d': '23.svg',
        '75d': '21.svg',
        '81d': '10.svg',
        '81n': '9.svg',
        '83d': '14.svg',
        '83n': '13.svg',
        '85d': '23.svg',
        '85n': '22.svg',
        '87d': '26.svg',
        '87n': '25.svg',
        '89d': '20.svg',
        '89n': '19.svg',
        '90d': '30.svg',
        '95d': '29.svg',
        '95n': '28.svg'
    },
    WEATHER_ICONS_IO_GLYPHS: {
        "00d": "wi-day-sunny.svg",
        "00n": "wi-night-clear.svg",
        '01d': 'wi-day-cloudy.svg',
        '01n': 'wi-night-cloudy.svg',
        '03d': 'wi-cloud.svg',
        '10d': 'wi-day-fog.svg',
        '14d': 'wi-cloudy.svg',
        '18d': 'wi-strong-wind.svg',
        '30d': 'wi-fog.svg',
        '50d': 'wi-sprinkle.svg',
        '60d': 'wi-rain.svg',
        '63d': 'wi-rain-wind.svg',
        '65d': 'wi-day-rain-mix.svg',
        '65n': 'wi-night-alt-rain-mix.svg',
        '70d': 'wi-snow.svg',
        '75d': 'wi-hail.svg',
        '81d': 'wi-day-showers.svg',
        '81n': 'wi-night-alt-showers.svg',
        '83d': 'wi-day-rain.svg',
        '83n': 'wi-night-rain.svg',
        '85d': 'wi-day-snow.svg',
        '85n': 'wi-night-alt-snow.svg',
        '87d': 'wi-day-snow-wind.svg',
        '87n': 'wi-night-alt-snow-wind.svg',
        '89d': 'wi-day-hail.svg',
        '89n': 'wi-night-alt-hail.svg',
        '90d': 'wi-thunderstorm.svg',
        '95d': 'wi-day-thunderstorm.svg',
        '95n': 'wi-night-alt-thunderstorm.svg'
    }
}
