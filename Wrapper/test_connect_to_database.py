import sqlite3
import json

# connect python wrapper to Sqlite
conn = sqlite3.connect('/home/samuel/PycharmProjects/CAMS_Workshop/AbcSmc_Python_Wrapper/Database/Wrapper_database.sqlite')
print("Opened Wrapper_database database successfully")


# open json file and load into data
with open('data.json') as data_file: #'data.json' must be replaced with sys.argv[5]    
    data = json.load(data_file)

#print examples
print(data["maps"][0]["id"])
print(data["masks"]["id"])
print(data["om_points"])
