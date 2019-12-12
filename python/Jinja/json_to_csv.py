#=======================#
# Nom : Hardy Dorian    #
#=======================#

import json

def convert(json_file, csv):
    with open(json_file) as json_data:
        data_dict = json.load(json_data)
    print(data_dict)
    

print(convert('../data/data.json','output.csv'))



