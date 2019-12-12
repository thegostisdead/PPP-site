# modele_Index.py

import csv_api

liens_importants = [
                    ('Onisep',"",'http://www.onisep.fr/'),
                    ('Studyrama',"",'http://www.studyrama.com'),
                    ('Diplomeo'," ",'https://diplomeo.com/'),
                    ('Imaginetonfutur',"Sur imaginetonfutur retrouvez plus de 600 fiches métiers et des infos pratiques sur votre futur diplome",'https://www.imaginetonfutur.com/'),
                    ('','','')
                    ]


                  
                    
etudiants = {
    "Dorian Hardy": [("img","Etudiant en 1ère année en DUT informatique.")],
    "Jules Brossier": [("img","Etudiant en 1ère année en DUT informatique.")],
    "Simon Cavillon": [("img","Etudiant en 1ère année en DUT informatique.")],
    "Silvain Roc": [("img","Etudiant en 1ère année en DUT informatique.")]
}


# traitement 


def get_student(dico):
    """
    params : 
    retourn : 
    """
    res = []
    for (student_name, (profile_picture, description)) in dico.items():
        res.append(student_name,profile_picture,description)

    return res 

    
def get_categories():
    """
    params : 
    retourn : 
    """
    category = set()
    category.add(csv_api.get_all_category())
    return category

def get_levels():
    """
    params : 
    retourn : 
    """
    levels = set()
    levels.add(csv_api.get_all_level_of_studies())
    return levels