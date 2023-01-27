# DWD Mosmix stations

**IMPORTANT**: This workflow currently returns invalid results due to a upstream change.

A python script to create the [`stations-report.json`](https://eugentoptic44.github.io/dwd-mosmix-stations/stations-report.json) file for [`Tiny Weather Forecast Germany`](https://codeberg.org/Starfish/TinyWeatherForecastGermany) to identifiy modifications of the Mosmix weather stations  used by Deutscher Wetterdienst (DWD).

## stations-report.json

The file reports on modificaions of the list of weather stations used by the DWD when issuing weather forecasts.

Please see [https://tinyweatherforecastgermanygroup.gitlab.io/index/**stations.html**](https://tinyweatherforecastgermanygroup.gitlab.io/index/stations.html) for a searchable table of the contents.

### format

```json
{
    "new": [
        "station not present within TWFG"
    ],
    "old": [
        "station not being used by the DWD anymore"
    ]
}
```

## Copyright

**License**: please see `LICENSE` files

This project is **not affialited** with or officially approved by any of the following organizations: Alphabet, Codeberg, the DWD, Google, GitLab or GitHub or related individuals in any way. Named trademarks, brands and icons belong to their owners.

## Disclaimer

Only use the source code in this repository on your **own risk**. The source code published here is by no means production-ready and not intended to be used in critical or commercial environments. Your mileage might vary.

## Contributing

* All contributions to **Tiny Weather Forecast Germany** are managed at the ['main'](https://codeberg.org/Starfish/TinyWeatherForecastGermany) code repository at [codeberg.org](https://codeberg.org/Starfish/TinyWeatherForecastGermany)
* [**Translations**](https://translate.codeberg.org/engage/tiny-weather-forecast-germany/) are managed on the [**weblate** server](https://translate.codeberg.org/projects/tiny-weather-forecast-germany/) provided by Codeberg e.V.
* Feel free to contribute to this script by opening issues and/or merge requests.
* Please also see the automatically generated *javadoc* **code documentation** of Tiny Weather Forecast Germany [at GitLab](https://gitlab.com/tinyweatherforecastgermanygroup/twfg-javadoc).
* For cybersec, privacy and/or copyright related issues regarding this repository please directly contact the maintainer [**Jean-Luc Tibaux**](https://codeberg.org/eUgEntOptIc44).
