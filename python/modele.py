#!/usr/bin/python3
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
    'Dorian Hardy': [('https://avatarfiles.alphacoders.com/173/173382.png',
                     "Etudiant en 1ère année en DUT informatique.","hrdy.dorian@gmail.com","https://github.com/thegostisdead")],
    'Jules Brossier': [('https://avatars2.githubusercontent.com/u/58080822?s=460&v=4',
                       "Etudiant en 1ère année en DUT informatique.","jules.brossier@gmail.com","https://github.com/IronJulo")],
    'Simon Cavillon': [('https://avatars2.githubusercontent.com/u/24855825?s=460&v=4',
                       "Etudiant en 1ère année en DUT informatique.","simon.cavillon@gmail.com","https://github.com/Sueezen")],
    'Silvain Roc': [('https://avatars0.githubusercontent.com/u/58080816?s=460&v=4',
                    "Etudiant en 1ère année en DUT informatique.","silvain.roc@gmail.com","https://github.com/ElectroPuls")],
    }

# Assignement des images pour chaques catégories pour les cards de la page categories 

images_categorie = [
    ("Système - Développement", "https://www.courb.net/wp-content/uploads/2019/05/web-development.jpg"),
    ("Système - Animation" , "https://i.ytimg.com/vi/0U0uxls41ZI/maxresdefault.jpg"),
    ("Système - Multimédia", "http://cpon.infocom-nancy.fr/wp-content/uploads/2017/01/HTFile.ashx_.jpg"),
    ("Web - Internet", "https://cdn.radiofrance.fr/s3/cruiser-production/2019/03/303573cf-dbbe-4582-a841-a732aac5629b/838_webgettyimages-603713201.jpg"),
    ("Système - Réseaux", "http://3supports.com.ng/wp-content/uploads/2018/12/data-cabling-1024x696.jpg"),
    ("Système - Base de donnée","https://storage.googleapis.com/hackersandslackers-cdn/2019/07/sqlalchemy-queries@2x.jpg")
]


# traitement

#  csv interaction
CSV_FILE = "../data/output.csv"

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

# fonction  d'initialisation, créer la variable global defaultdata, pour quelle soie accessible partout.
global default_data
default_data = csv_to_dico(CSV_FILE)



def get_image_by_key(nom_categorie): 
    """
    parametres : nom_categorie, une chaine de caractères, qui correspond a une categorie
    resultat : le lien de l'image associée a la catégorie sous la forme d'un str
    """
    for (nom,lien) in images_categorie :
        if nom_categorie == nom:
            return lien


def get_all_job_card(data=default_data):
    """
    parametres: data : La variable data représente notre dictionnaire qui comporte les informations de chaque métiers, ou il aura comme clés le nom du métier et sa valeur sera un autre dictionnaire contenant les informations.
    resultat: Renvoi une liste de tuple contenant les informations de chaque métiers.
    """
    liste=[]
    liste_tuple_metier=[]
    for (metier, dico_info) in data.items():
        liste_tuple_metier.append(metier)

        for valeur in dico_info.values():
            liste_tuple_metier.append(valeur)

        liste.append(tuple(liste_tuple_metier))
        liste_tuple_metier = []
    return liste

assert get_all_job_card({"developpeur": {"level": 3, "description": "Un métier d'avenir", "category": "Développement", "money": 2400, "link": "http://test.com"},"ingedb": {"level": 5, "description": "Un métier de BDD", "category": "Base de Donnée", "money": 2800, "link": "http://test.fr"}}) == [("developpeur", 3, "Un métier d'avenir", "Développement", 2400, "http://test.com"), ("ingedb", 5, "Un métier de BDD", "Base de Donnée", 2800, "http://test.fr")]



def get_all_category_card(data=default_data):
    """
    {
        "cat1" : [9,img]
    }
    """
    res = {}
    for (nom,dictionnaire) in data.items():
        if dictionnaire["category"] not in res :
            res[dictionnaire["category"]] = [1, get_image_by_key(dictionnaire["category"])]

        else:
            res[dictionnaire["category"]][0] += 1 

    return res


def get_all_name_jobs(data=default_data):
    """
    parametres : data, un dictionnaire contenant les données
    resultat : le nom de tout les métiers dans une liste
    """

    res = [] 
    for name in data.keys():
        res.append(name)   
    return res


def get_all_level_of_studies(data=default_data):
    """
    parametres : vide 
    resultat : l'ensemble des niveau d'études
    """

    res = set()
    for (_, dico) in data.items():
        res.add(dico["level"])   
    return res


def get_all_description(data=default_data):
    """
    parametres : data, un dictionnaire contenant les données
    resultat : toute les descriptions sous la forme de liste
    """

    res = [] 
    for (_, dico) in data.items():
        res.append(dico["description"])   
    return res


def get_all_category(data=default_data):
    """
    parametres : data, un dictionnaire contenant les données
    resultat : toute les catégories sous la forme d'un ensemble
    """

    res = set()
    for (_, dico) in data.items():
        res.add(dico["category"])   
    return res
     


def get_all_link(data=default_data):
    """
    parametres : data, un dictionnaire contenant les données
    resultat : la liste de tout les liens dans une liste
    """

    res = [] 
    for (_, dico) in data.items():
        res.append(dico["link"])   
    return res


#  filtre

def get_student(dico):
    """
    parametres : dico, un dictionnaire  
    resultat : une liste de tuples qui sont le nom, le lien de la photo de profile, et la description
    """

    res = []
    for (student_name, (profile_picture, description)) in dico.items():
        res.append(student_name, profile_picture, description)
        return res


def search(level, category):
    """
    paramertres : level, un string qui correspond au nombre d'étude voulu
                  category, un string qui est la categorie a rechercher
    resultat : une liste de métier
    """
    res = []
    for (_,dico) in data.items():
       if dico['level'] == level and dico["category"] == category :
           print("match found ")
           res.append(dico)
    return res
""" 
assert search("6","Système - Réseaux'") == [{'level': '6', 'description': "Expert de la virtualisation des données en dehors de l'entreprise, et de leur stockage sécurisé sur des serveurs distants pour un accès depuis mobiles, tablettes ou postes de travail, l'ingénieur cloud computing accompagne les ent reprises dans leur mutation vers cette nouvelle tendance qui se généralise.", 'category': 'Système - Réseaux', 'money': '3300', 'link': 'http://www.onisep.fr/Ressources/Univers-Metier/Metiers/ingenieur-ingenieure-cloud-computing'}] 
"""