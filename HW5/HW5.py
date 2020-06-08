import os
import argparse
import csv
import json

filename = 'user_details.csv'

def valid_directory(directory):
        if not os.path.isdir(directory):
            raise argparse.ArgumentTypeError(
                f"'{directory}' is not a name of an existing directory")
        return directory


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-csv", type=valid_directory, default=os.getcwd(),
                        help="a directory with .csv file to be opened")
    parser.add_argument("-json", type=str, default=os.getcwd() + "\\j_file",
                        help="path to json file and name")
    parsed_args = parser.parse_args()
    return parsed_args.csv, parsed_args.json


def read_csv(path):

    structures = []

    with open(path) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        data = f_csv

        for row in data:
            temp_dict = dict(zip(headers, row))
            del temp_dict["password"]
            structures.append(temp_dict)

    return structures



def write_json(path, structures):
    with open(path, 'w') as f:
        json.dump(structures, f, indent=4, sort_keys=True)



csv_path, json_path = args()

csv_file = csv_path + "\\" + filename
json_file = json_path + ".json"


data_dicts = read_csv(csv_file)

write_json(json_file, data_dicts)
