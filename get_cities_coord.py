import json
import pypinyin
import pandas as pd

def r_json(path):
    with open(path, 'r') as rf:
        data = json.load(rf)
    return data

def pinyin(word):
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        s += ''.join(i)
    return s

def get_coord(coords, city_list, coord_of_selected_cities_init):
    lonlat_dict = {}
    for city in [i[:-1] for i in city_list]:
        temp_city_list = []
        for raw_data in coords[:]:
            cities = list(raw_data.keys())[0]
            if city in cities:
                temp_city_list.append(cities)
        city_len_list = [len(i) for i in temp_city_list]  # find the min len()
        minimum = min(city_len_list)
        key = temp_city_list[city_len_list.index(minimum)]  # find the value
        for raw_data in coords[:]:
            if raw_data.get(key) != None:
                p = raw_data.get(key)
                lonlat_dict[key] = p
                coord_of_selected_cities_init['lon'][f'{city}市'] = p[0]
                coord_of_selected_cities_init['lat'][f'{city}市'] = p[1]
                print(f'finding lon and lat for {key}市：{p}')
    return coord_of_selected_cities_init

def main():
    path = 'coords.json'
    city_list = ['北京市','上海市','天津市','重庆市']
    coords = r_json(path)
    coord_of_selected_cities_init = pd.DataFrame(index = city_list, columns=['lon','lat'])
    coord_of_selected_cities = get_coord(coords, city_list, coord_of_selected_cities_init)
    # change to english
    coord_of_selected_cities.index = [pinyin(i[:-1]) for i in list(coord_of_selected_cities.index)]
    coord_of_selected_cities.to_csv('coord_of_selected_cities.csv', encoding = 'utf_8_sig')


if __name__ == '__main__':
    main()





