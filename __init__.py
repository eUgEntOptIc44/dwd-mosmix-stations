
from pprint import pprint
import json
import sys

import requests

from wetterdienst import Wetterdienst # , Resolution, Period
from wetterdienst.provider.dwd.mosmix import DwdMosmixRequest, DwdMosmixType

twfg_req = requests.get('https://tinyweatherforecastgermanygroup.gitlab.io/index/'
                        'twfg-stations.json',
                        timeout=10)
if twfg_req.ok:
    twfg_req = twfg_req.json()
else:
    print("ERROR: failed to download 'twfg-stations.json' -> server returned"
          f" unexpected status code '{twfg_req.status_code}' ")
    sys.exit(1)

with open('twfg-stations.json', 'w+', encoding='utf-8') as fh:
    fh.write(str(json.dumps(twfg_req, indent=4)))

print(f"DEBUG: retrieved {len(twfg_req)} stations from parsed app data")

station_names_old = []

for stations_dict in twfg_req:
    station_names_old.append(stations_dict['name'])

stations = DwdMosmixRequest(parameter="large", mosmix_type=DwdMosmixType.LARGE)
stations_df = stations.all().df
stations_list = []

station_names = list(stations_df['name'])

for row_index, stations_row in stations_df.iterrows():
    station_to_dt = str(stations_row['to_date'])
    if station_to_dt != 'NaT': #TODO: double check this with wetterdienst docs
        print(f"WARNING: station '{stations_row['name']}'"
              f" ({stations_row['station_id']}) -> to_date: {station_to_dt} ")

    stations_list.append({
        'id':stations_row['station_id'],
        'name':stations_row['name'],
        'latitude':stations_row['latitude'],
        'longitude':stations_row['longitude'],
        'altitude':stations_row['height']
    })

print(f"DEBUG: retrieved {len(stations_list)} MOSMIX stations via wetterdienst")
with open('stations.json', 'w+', encoding='utf-8') as fh:
    fh.write(str(json.dumps(stations_list, indent=4)))

print("DEBUG: new station(s):")
new_stations_names = list(set(station_names) - set(station_names_old))
pprint(new_stations_names)

print("DEBUG: deprecated or removed station(s):")
old_stations_names = list(set(station_names_old) - set(station_names))
pprint(old_stations_names)

with open('stations-report.json', 'w+', encoding='utf-8') as fh:
    fh.write(str(json.dumps({'new':new_stations_names,'old':old_stations_names},
                            indent=4)))

print("done")