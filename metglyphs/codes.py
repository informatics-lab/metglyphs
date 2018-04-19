"""Lookup tables for converting between code reference systems."""

DATAPOINT_TO_WMO_LOOKUP = {
    "0":  "00n",  # Clear night
    "1":  "00d",  # Sunny day
    "2":  "01n",  # Partly cloudy (night)
    "3":  "01d",  # Partly cloudy (day)
    "4":  "",     # Not used
    "5":  "10d",  # Mist
    "6":  "30d",  # Fog
    "7":  "03d",  # Cloudy
    "8":  "14d",  # Overcast
    "9":  "81n",  # Light rain shower (night)
    "10": "81d",  # Light rain shower (day)
    "11": "50d",  # Drizzle
    "12": "60d",  # Light rain
    "13": "83n",  # Heavy rain shower (night)
    "14": "83d",  # Heavy rain shower (day)
    "15": "63d",  # Heavy rain
    "16": "65n",  # Sleet shower (night)
    "17": "65d",  # Sleet shower (day)
    "18": "65d",  # Sleet
    "19": "89n",  # Hail shower (night)
    "20": "89d",  # Hail shower (day)
    "21": "75d",  # Hail
    "22": "85n",  # Light snow shower (night)
    "23": "85d",  # Light snow shower (day)
    "24": "70d",  # Light snow
    "25": "87n",  # Heavy snow shower (night)
    "26": "87d",  # Heavy snow shower (day)
    "27": "70d",  # Heavy snow
    "28": "95n",  # Thunder shower (night)
    "29": "95d",  # Thunder shower (day)
    "30": "90d"   # Thunder
}

DARKSKY_TO_WMO_LOOKUP = {
    "clear-day": "00d",
    "clear-night": "00n",
    "rain": "63d",
    "snow": "70d",
    "sleet": "65d",
    "wind": "18d",
    "fog": "30d",
    "cloudy": "03d",
    "partly-cloudy-day": "01d",
    "partly-cloudy-night": "01n"
}
