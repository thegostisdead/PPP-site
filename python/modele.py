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

def csv_to_dico(csv_file):
    """
    parametres : csv_file : le fichier csv 
    resultat : un dictionnaire 
    """

    reader = csv.reader(open('convertcsv.csv', 'r'))
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


def readCollum(collum_name, csv_filename):
    """
    parametres : collum_name : la collone a lire 
                 csv_file : le fichier csv 
    resultat : le text des collones 
    commentaire : il faut éviter d'appeler cette fonction car elle est conteuse en ressource. 
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

    return readCollum('name', 'output.csv')


def get_all_level_of_studies():
    """
    parametres :
    resultat : le nom de tout les métiers
    """

    return readCollum('level', 'output.csv')


def get_all_description():
    """
    parametres :
    resultat : le nom de tout les métiers
    """

    return readCollum('description', 'output.csv')


def get_all_category():
    """
    parametres :
    resultat : le nom de tout les métiers
    """

    return readCollum('category', 'output.csv')


def get_all_money():
    """
    parametres :
    resultat : le nom de tout les métiers
    """

    return readCollum('money', 'output.csv')


def get_all_link():
    """
    parametres :
    resultat : le nom de tout les métiers
    """

    return readCollum('link', 'output.csv')


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
