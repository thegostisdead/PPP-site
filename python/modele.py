#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv

liens_importants = [('Onisep',
                    "L’Onisep a pour vocation d’informer sur les formations, les métiers, les secteurs professionnels. Il guide les jeunes et leur famille dans leurs choix de parcours de formation et de projet professionnel."
                    , 'http://www.onisep.fr/', '../img/onisep.png'),
                    ('Studyrama',
                    "En tant qu’acteur référent du monde de l’orientation et de l’aide à la réussite aux examens et aux concours, notre vocation est d’accompagner et de conseiller chaque individu tout au long de son parcours étudiant et professionnel."
                    , 'http://www.studyrama.com', '../img/onisep.png'),
                    ('Diplomeo',
                    "Diplomeo est un des principaux moteurs de recherche de formations en France. Il recense plus de 40 000 formations ciblant les étudiants.C'est un outil rassemblant en un seul endroit toutes les informations concernant l’enseignement supérieur"
                    , 'https://diplomeo.com/', '../img/onisep.png'),
                    ('Imaginetonfutur',
                    "Sur imaginetonfutur retrouvez plus de 600 fiches métiers et des infos pratiques sur votre futur diplome pour trouver le métier vous convient."
                    , 'https://www.imaginetonfutur.com/',
                    '../img/onisep.png')]

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
    for name, (_, _, _, _, _) in data.items():
        res.append(name)   
    return res


def get_all_level_of_studies():
    """
    parametres :
    resultat : le nom de tout les métiers
    """

    res = [] 
    for _, (level, _, _, _, _) in data.items():
        res.append(level)   
    return res


def get_all_description():
    """
    parametres :
    resultat : le nom de tout les métiers
    """

    res = [] 
    for _, (_, description, _, _, _) in data.items():
        res.append(description)   
    return res


def get_all_category():
    """
    parametres :
    resultat : le nom de tout les métiers
    """

    res = [] 
    for _, (_, _, category, _, _) in data.items():
        res.append(category)   
    return res


def get_all_money():
    """
    parametres :
    resultat : le nom de tout les métiers
    """

    res = [] 
    for _, (_, _, _, money, _) in data.items():
        res.append(money)   
    return res


def get_all_link():
    """
    parametres :
    resultat : le nom de tout les métiers
    """

    res = [] 
    for _, (_, _, _, _, link) in data.items():
        res.append(link)   
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


def get_categories():
    """
    parametres : 
    resultat : 
    """

    category = set()
    for elem in get_all_category():
        category.add(elem)
    return category


def get_levels():
    """
    paramètre : 
    resultat : un ensemble qui contient 
    """

    levels = set()
    for elem in get_all_level_of_studies():
        levels.add(elem)
    return levels
