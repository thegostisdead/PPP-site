# modele_Index.py

import csv_api

liens_importants = [
                    ('Onisep',"L’Onisep a pour vocation d’informer sur les formations, les métiers, les secteurs professionnels. Il guide les jeunes et leur famille dans leurs choix de parcours de formation et de projet professionnel.",'http://www.onisep.fr/','../../../img/onisep.png'),
                    ('Studyrama',"En tant qu’acteur référent du monde de l’orientation et de l’aide à la réussite aux examens et aux concours, notre vocation est d’accompagner et de conseiller chaque individu tout au long de son parcours étudiant et professionnel.",'http://www.studyrama.com','../../../img/onisep.png'),
                    ('Diplomeo',"Diplomeo est un des principaux moteurs de recherche de formations en France. Il recense plus de 40 000 formations ciblant les étudiants.C'est un outil rassemblant en un seul endroit toutes les informations concernant l’enseignement supérieur",'https://diplomeo.com/','../../../img/onisep.png'),
                    ('Imaginetonfutur',"Sur imaginetonfutur retrouvez plus de 600 fiches métiers et des infos pratiques sur votre futur diplome pour trouver le métier vous convient.",'https://www.imaginetonfutur.com/','../../../img/onisep.png'),
                    ]


                  
                    
etudiants = {
    "Dorian Hardy": [("img","Etudiant en 1ère année en DUT informatique.")],
    "Jules Brossier": [("img","Etudiant en 1ère année en DUT informatique.")],
    "Simon Cavillon": [("img","Etudiant en 1ère année en DUT informatique.")],
    "Silvain Roc": [("img","Etudiant en 1ère année en DUT informatique.")]
}


# traitement 


# def get_student(dico):
#     """
#     params : 
#     retourn : 
#     """
#     res = []
#     for student_name, (profile_picture, description) in dico.items():
#         res.append(student_name,profile_picture,description)

#     return res 

    
# def get_categories():
#     """
#     params : 
#     retourne : 
#     """
#     category = set()
#     for elem in csv_api.get_all_category():
#         category.add(elem)
#     return category

# def get_levels():
#     """
#     paramètre : 
#     retourne : un ensemble qui contient 
#     """
#     levels = set()
#     for elem in csv_api.get_all_level_of_studies():
#         levels.add(elem)
#     return levels