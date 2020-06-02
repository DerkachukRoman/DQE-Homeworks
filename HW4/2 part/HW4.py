import pandas as pd
import os
import argparse

filename = 'HRR Scorecard_ 20 _ 40 _ 60 - 20 Population.csv'

def valid_directory(directory):
        if not os.path.isdir(directory):
            raise argparse.ArgumentTypeError(
                f"'{directory}' is not a name of an existing directory")
        if not os.path.isfile(os.path.join(directory, filename)):
            raise argparse.ArgumentTypeError(
                f"'{directory}' doesn't contain the required file")
        return directory


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-path", type=valid_directory, default=os.getcwd(),
                        help="a directory with .csv file to be opened")
    parser.add_argument("-bed", type=int, default=5,
                        help="number or HRR to be displayed")
    parsed_args = parser.parse_args()
    return parsed_args.path, parsed_args.bed



path, bed = args()

path = path + "\\" + filename


df = pd.read_csv(path,
                 header=0,
                 thousands = ',',
                 skiprows=range(1,2),
                 usecols = ['HRR',
                            'Total Hospital Beds',
                            'Available Hospital Beds'])

df['Percent'] = (df['Available Hospital Beds'] /
                 df['Total Hospital Beds'])*100


df = df.sort_values(by=['Percent'], ascending=False).reset_index(drop=True)


print(df.loc[range(int(bed)),['HRR', 'Percent']])

