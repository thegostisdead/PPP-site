#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv

liens_importants = [('Onisep',
                    "L’Onisep a pour vocation d’informer sur les formations, les métiers, les secteurs professionnels. Il guide les jeunes et leur famille dans leurs choix de parcours de formation et de projet professionnel."
                    , 'http://www.onisep.fr/', '../img/onisep.png'),
                    ('Studyrama',
                    "En tant qu’acteur référent du monde de l’orientation et de l’aide à la réussite aux examens et aux concours, notre vocation est d’accompagner et de conseiller chaque individu tout au long de son parcours étudiant et professionnel."
                    , 'http://www.studyrama.com', '../img/studyrama.jpg'),
                    ('Diplomeo',
                    "Diplomeo est un des principaux moteurs de recherche de formations en France. Il recense plus de 40 000 formations ciblant les étudiants.C'est un outil rassemblant en un seul endroit toutes les informations concernant l’enseignement supérieur"
                    , 'https://diplomeo.com/', '../img/diplomeo.png'),
                    ('Imaginetonfutur',
                    "Sur imaginetonfutur retrouvez plus de 600 fiches métiers et des infos pratiques sur votre futur diplome pour trouver le métier vous convient."
                    , 'https://www.imaginetonfutur.com/',
                    '../img/itf.jpeg'),
                    ('Orientation.com','DigiSchool orientation est un annuaire référence des formations supérieures en France. Trouvez facilement l\'établissement, le métier ou le diplôme idéal en seulement quelques clics.',
                    'https://www.orientation.com/diplomes/dut-informatique.html','../img/orientation.png'),
                    ('L\'étudiant',"Letudiant.fr est l’un des sites Internet les plus variés en matière d’orientation. Il propose de très nombreuses fonctionnalités pour guider les étudiants: tests, coaching, boite à outils, fiches métiers, annuaires, reportages et conseils de conseiller d'orientation… On ne peut toutes les citer ici tant elles sont nombreuses. Comme son nom l’indique, ce site est plutôt destiné aux étudiants post-bac.",
                    'https://www.letudiant.fr','../img/letudiant.jpg'),
                    ('Education.gouv','Le site Internet de l’Education Nationale propose également de nombreux services et renseignements en termes d’orientation. En effet, en fonction de votre série de BAC, le site vous indique les types de formations et les voies d’orientation qui peuvent vous convenir.',
                    'https://www.education.gouv.fr','../img/2018_MENJ_logo_horizontal_RVB_1019307.jpg')]

etudiants = {
    'Dorian Hardy': [('img',
                     "Etudiant en 1ère année en DUT informatique.")],
    'Jules Brossier': [('img',
                       "Etudiant en 1ère année en DUT informatique.")],
    'Simon Cavillon': [('img',
                       "Etudiant en 1ère année en DUT informatique.")],
    'Silvain Roc': [('img',
                    "Etudiant en 1ère année en DUT informatique.")],
    }


# traitement

#  csv interaction
CSV_FILE = "output.csv"

def csv_to_dico(csv_file):
    """
    parametres : csv_file : le fichier csv 
    resultat : un dictionnaire 
    """

    reader = csv.reader(open(csv_file, 'r'))
    dico = {}
    for row in reader:
        (
            name,
            level,
            description,
            category,
            money,
            link,
            ) = row
        if name == 'name' and level == 'level':  #  on enleve la premiere ligne du csv car on a pas besoins
            continue
        else:
            dico[name] = {
                'level': level,
                'description': description,
                'category': category,
                'money': money,
                'link': link,
                }

    return dico

# fonction  d'initialisation, créer la variable global data, pour quelle soie accessible partout.
def initialize():
    global data
    data = csv_to_dico(CSV_FILE)


initialize()



def get_all_name_jobs():
    """
    parametres :
    resultat : le nom de tout les métiers
    """

    res = [] 
    for name in data.keys():
        res.append(name)   
    return res


def get_all_level_of_studies():
    """
    parametres : vide 
    resultat : le nom de tout les métiers
    """

    res = set()
    for (_,dico) in data.items():
        res.add(dico["level"])   
    return res


def get_all_description():
    """
    parametres : vide 
    resultat : toute les descriptions sous la forme de liste
    """

    res = [] 
    for (_,dico) in data.items():
        res.append(dico["description"])   
    return res


def get_all_category():
    """
    parametres :
    resultat : toute les catégories
    """

    res = set()
    for (_,dico) in data.items():
        res.add(dico["category"])   
    return res


def get_all_money():
    """
    parametres :
    resultat : le nom de tout les métiers
    """

    res = [] 
    for (_,dico) in data.items():
        res.append(dico["money"])   
    return res


def get_all_link():
    """
    parametres :
    resultat : le nom de tout les métiers
    """

    res = [] 
    for (_,dico) in data.items():
        res.append(dico["link"])   
    return res


#  filtre

def get_student(dico):
    """
    parametres : 
    resultat : 
    """

    res = []
    for (student_name, (profile_picture, description)) in dico.items():
        res.append(student_name, profile_picture, description)
        return res


