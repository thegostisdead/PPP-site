import csv
csv_file = None 
with open('output.csv', mode='r') as csv_file:
    csv_file = csv.DictReader(csv_file)
    


def readCollum(collum_name,csv_file):
    """
    parametres : collum_name : la collone a lire 
                 csv_file : le fichier csv 
    resultat : le text des collones 

    """
    res = []
    line_count = 0
    for row in csv_file:
        if line_count == 0:
            line_count += 1
        res.append([str(collum_name)])
        line_count += 1
    return res
    


def get_all_name_jobs():
    """
    parametres :
    resultat : le nom de tout les métiers
    """
    return readCollum("name", csv_file)
    
def get_all_level_of_studies():
    """
    parametres :
    resultat : le nom de tout les métiers
    """
    return readCollum("level", csv_file)
    

def get_all_description():
    """
    parametres :
    resultat : le nom de tout les métiers
    """
    return readCollum("description", csv_file)

def get_all_category():
    """
    parametres :
    resultat : le nom de tout les métiers
    """
    return readCollum("category", csv_file)

def get_all_money():
    """
    parametres :
    resultat : le nom de tout les métiers
    """
    return readCollum("money", csv_file)

def get_all_link():
    """
    parametres :
    resultat : le nom de tout les métiers
    """
    return readCollum("link", csv_file)