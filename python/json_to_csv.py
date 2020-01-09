#=======================#
# Nom : Hardy Dorian    #
#=======================#

import json

def convert(json_file, csv):
    """
    paramètres : 
    json_file : str, le fichier json (chemain) 
    csv : str, le nom du fichier de sortie apres conversion 
    résultat : création d'un fichier au format csv 
    """
    with open(json_file) as json_data:
        data_dict = json.load(json_data)
    print(data_dict)
    

print(convert('../data/data.json','output2.csv'))



