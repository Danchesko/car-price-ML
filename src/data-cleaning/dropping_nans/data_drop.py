import pandas as pd
import os

REL_PATH_DROPPED_DF = "../../../data/interim/cars_dropped.xlsx"
REL_PATH_MANUAL_CLEANED= "../../../data/raw/cars_manually_cleaned.xlsx"
FILE_EXISTS_MESSAGE = "File already exists"
ENCODING_XLSX = "utf-8-sig"

def main():
    if not os.path.isfile(REL_PATH_DROPPED_DF):
        data=read_data(REL_PATH_MANUAL_CLEANED)
        drop_missing_values(data)
        write_to_excel(data)
    else:
        print(FILE_EXISTS_MESSAGE)
        
def read_data(path):
    cars_data = pd.read_excel(path)
    return cars_data


def drop_missing_values(data):
    data.dropna(inplace = True)

def write_to_excel(data):
    writer = pd.ExcelWriter(REL_PATH_DROPPED_DF)
    data.to_excel(writer,"Sheet1",encoding=ENCODING_XLSX,index=False)


if __name__=='__main__':
    main()