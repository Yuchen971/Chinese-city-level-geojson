import json
import os

def r_json(path):
    with open(path, 'r') as rf:
        data = json.load(rf)
    return data

def get_path(city):
    temp_path = []
    for root,dirs,files in os.walk('中华人民共和国/'): 
        for file in files:
            #print(os.path.join(root,file))
            if city in root and '_full' not in file:
                #print(os.path.join(root,file))
                temp_path.append(os.path.join(root,file))
                temp_len = []
                for path in temp_path:
                    temp_len.append(len(path))
                path = temp_path[temp_len.index(min(temp_len))]
    return path


def get_geo_json(city_list, data):
    geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    for city in city_list:
        city_dict = {
            'geometry': {
                'type': 'MultiPolygon',
                'coordinates': [r_json(get_path(city))['features'][0]['geometry']['coordinates']]
            },
                "type": "Feature",
                'properties': {
                    'waste': data[f'{city}'],
                    'name': city,
                },
            }
        geojson['features'].append(city_dict)
    return geojson

def write_geo_json(geojson, filename):
    j = json.dumps(geojson)
    with open(f'{filename}.json','w')as f:
        f.write(j)
