import json
import math
import time

import requests


def get_atms_to_update():
    try:
        with open('to_update.json', mode='r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def get_updated_atms():
    try:
        with open('clean_data.json', mode='r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_partial_data(not_updated, updated):
    print("Saving partial data.")
    with open('to_update.json', mode='w') as file:
        json.dump(not_updated, file)

    with open('clean_data.json', mode='w') as file:
        json.dump(updated, file)


def update_atms(updated_atms, to_update):
    total_entries = len(updated_atms) + len(to_update)
    successes = len(updated_atms)

    url = 'https://maps.mail.ru/osm/tools/overpass/api/interpreter'
    print(f"Updating {len(to_update)} items.")
    for atm in to_update:
        print(atm)

        latitude = atm['lat']
        longitude = atm['lon']

        lat_upper = float(latitude) + 0.00025
        lon_upper = float(longitude) + 0.00025
        lat_lower = float(latitude) - 0.00025
        lon_lower = float(longitude) - 0.00025

        data = f'data=[timeout:10][out:json];is_in({latitude},{longitude})->.a;way(pivot.a);out tags bb;out ids geom({lat_lower},{lon_lower},{lat_upper},{lon_upper});relation(pivot.a);out tags bb;'
        response_raw = requests.post(url, data=data)

        try:
            response = response_raw.json()
            if response['elements'] is not None:
                for element in response['elements']:
                    # Cantons are always relations
                    if element['type'] == 'relation':
                        # Find the relevant tag
                        atm_id = atm['_id']
                        try:
                            if element['tags']['admin_level'] == '4':
                                canton = element['tags']['name']

                                print(f'Updating element with ID: {atm_id}')
                                updated_atms.append(atm)
                                to_update.remove(atm)
                                successes += 1
                                atm['canton'] = canton
                        except KeyError:
                            print(f"ATM with _id {atm_id} might not contain a tag with admin level = 4.")

        except requests.JSONDecodeError:
            print("Failed to JSON-decode the following response:")
            print(response_raw.text)

        percentage = math.floor(100 / total_entries * successes)
        print(f"Updated {successes}/{total_entries} ({percentage}%) ATMs.")

        time.sleep(1)


if __name__ == '__main__':
    print("This is a legacy script used to augment the data.")
    print("Do not run this unless you know what you are doing.")
    exit(1)
    updated_atms = get_updated_atms()
    to_update = get_atms_to_update()

    try:
        update_atms(updated_atms, to_update)
    except KeyboardInterrupt:
        # save_partial_data(to_update, updated_atms)
        print("Keyboard Interrupt")
    except BaseException:
        # save_partial_data(to_update, updated_atms)
        print("An exception occured.")
    finally:
        save_partial_data(to_update, updated_atms)
        exit(0)
