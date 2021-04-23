import requests
import os
def get_json(save_dir, adcode):
    # 获取当前地图轮廓
    base_url = 'https://geo.datav.aliyun.com/areas/bound/' + str(adcode) + '.json'
    full_url = 'https://geo.datav.aliyun.com/areas/bound/' + str(adcode) + '_full.json'
    base_r = requests.get(base_url)
    if base_r.status_code == 200:
        cur_obj_name = base_r.json()['features'][0]['properties']['name']
        print(cur_obj_name)
        cur_file_dir = os.path.join(save_dir, cur_obj_name)
        if not os.path.exists(cur_file_dir):
            os.mkdir(cur_file_dir)
        base_json_file = os.path.join(cur_file_dir, str(adcode) + '.json')
        with open(base_json_file, 'w') as file:
            file.write(base_r.text)
    # 获取当前地图子地图轮廓
    full_r = requests.get(full_url)
    if full_r.status_code == 200 and 'cur_obj_name' in vars():
        full_json_file = os.path.join(cur_file_dir, str(adcode) + '_full.json')
        with open(full_json_file, 'w') as file:
            file.write(full_r.text)
        for item in full_r.json()['features']:
            chadcode = item['properties']['adcode']
            if chadcode == adcode:
                pass
            else:
                get_json(cur_file_dir, chadcode)
get_json('/Users/yuchenli/Downloads/city_geojson-master', 100000)