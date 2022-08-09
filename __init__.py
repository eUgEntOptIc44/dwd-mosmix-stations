
from pprint import pprint
import json
import sys

import requests

from wetterdienst import Wetterdienst, Resolution, Period
from wetterdienst.provider.dwd.mosmix import DwdMosmixType

twfg_req = requests.get('https://tinyweatherforecastgermanygroup.gitlab.io/index/twfg-stations.json', timeout=10)
if twfg_req.ok:
    twfg_req = twfg_req.json()
else:
    print(f"ERROR: failed to download twfg-stations.json -> server returned unexpected status code '{twfg_req.status_code}' ")
    sys.exit(1)

with open('twfg-stations.json', 'w+', encoding='utf-8') as fh:
    fh.write(str(json.dumps(twfg_req, indent=4)))

print(f"DEBUG: retrieved {len(twfg_req)} stations from parsed app data")

station_names_old = []

for stations_dict in twfg_req:
    station_names_old.append(stations_dict['name'])

API = Wetterdienst(provider="dwd", network="mosmix")
stations = API(parameter="small", mosmix_type=DwdMosmixType.LARGE)
stations_df = stations.all().df
stations_list = []

station_names = list(stations_df['name'])

for row_index, stations_row in stations_df.iterrows():
    stations_list.append({
        'id':stations_row['station_id'],
        'name':stations_row['name'],
        'latitude':stations_row['latitude'],
        'longitude':stations_row['longitude']
    })

    # if stations_row['name'] not in station_names_old:
    #     print(stations_row['name'])

print(f"DEBUG: retrieved {len(stations_list)} stations via wetterdienst")
with open('stations.json', 'w+', encoding='utf-8') as fh:
    fh.write(str(json.dumps(stations_list, indent=4)))

print(f"DEBUG: new station(s):")
pprint(set(station_names) - set(station_names_old)) # new stations

print(f"DEBUG: deprecated or removed station(s):")
pprint(set(station_names_old) - set(station_names)) # deprecated/removed stations




