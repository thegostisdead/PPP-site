import csv



def readCollum(collum_name,csv_filename):
    """
    parametres : collum_name : la collone a lire 
                 csv_file : le fichier csv 
    resultat : le text des collones 

    """

    with open(csv_filename, mode='r') as csv_file:
        res = []
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            res.append(row[collum_name])
            line_count += 1
        return res
       

def get_all_name_jobs():
    """
    parametres :
    resultat : le nom de tout les métiers
    """
    return readCollum("name", "output.csv")
    
def get_all_level_of_studies():
    """
    parametres :
    resultat : le nom de tout les métiers
    """
    return readCollum("level", "output.csv")
    

def get_all_description():
    """
    parametres :
    resultat : le nom de tout les métiers
    """
    return readCollum("description", "output.csv")

def get_all_category():
    """
    parametres :
    resultat : le nom de tout les métiers
    """
    return readCollum("category", "output.csv")

def get_all_money():
    """
    parametres :
    resultat : le nom de tout les métiers
    """
    return readCollum("money", "output.csv")

def get_all_link():
    """
    parametres :
    resultat : le nom de tout les métiers
    """
    return readCollum("link", "output.csv")