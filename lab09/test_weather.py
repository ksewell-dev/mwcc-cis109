
import unittest
from unittest.mock import patch, Mock

import weather


class TestWeather(unittest.TestCase):

    @patch("weather.requests.get")
    def test_get_coordinates(self, mock_get):

        response = Mock()

        response.json.return_value = [
            {
                "lat": "42.5751",
                "lon": "-71.9981"
            }
        ]

        mock_get.return_value = response

        lat, lon = weather.get_coordinates("Gardner, MA")

        self.assertEqual(lat, "42.5751")
        self.assertEqual(lon, "-71.9981")

    @patch("weather.requests.get")
    def test_get_noaa_endpoint(self, mock_get):

        response = Mock()

        response.json.return_value = {
            "properties": {
                "forecast": "https://api.weather.gov/test"
            }
        }

        mock_get.return_value = response

        result = weather.get_noaa_endpoint(
            "42.5751",
            "-71.9981"
        )

        self.assertEqual(result, "https://api.weather.gov/test")

    @patch("weather.requests.get")
    def test_get_noaa_forecast(self, mock_get):

        periods = [
            {
                "name": "Tonight",
                "temperature": 48,
                "temperatureUnit": "F",
                "shortForecast": "Clear",
                "detailedForecast": "Clear skies tonight."
            }
        ]

        response = Mock()

        response.json.return_value = {
            "properties": {
                "periods": periods
            }
        }

        mock_get.return_value = response

        result = weather.get_noaa_forecast(
            "https://api.weather.gov/test"
        )

        self.assertEqual(result, periods)

    def test_average_temperature(self):

        temperatures = [48, 55, 60, 65]

        average = sum(temperatures) / len(temperatures)

        self.assertEqual(average, 57)


if __name__ == "__main__":
    unittest.main()
