#!/usr/bin/python3
# -*- coding: utf-8 -*-
from jinja2 import *  # ne pas modifier

from modele import *


def creer_html(fichier_template, fichier_sortie, **infos):
    """
    fonction qui génère automatiquement un fichier à partir d'un template et d'informations
    paramètres :
            fichier_template : un fichier template (template HTML par exemple)
            fichier_sortie : le nom du fichier généré
            **infos : un nombre indéfini de paramètres qu'il suffit de nommer
    return : rien
    """
    env = Environment(loader=FileSystemLoader('.'), trim_blocks=True)
    template = env.get_template(fichier_template)
    html = template.render(infos)
    f = open(fichier_sortie, 'w')
    f.write(html)
    f.close()


# Ajouter ici les appels à la fonction creer_html


# GENERATION DE LA PAGE INDEX
creer_html("templates/template_index.html", "../pages-dev/index.html",
           categories = get_all_category(),
           niveaux = get_all_level_of_studies(),
           jobs = default_data,
           search_data = get_all_job_card()
           )

# GENERATION DE LA PAGE AIDE
creer_html("templates/template_aide.html", "../pages-dev/aide.html",
           liens_importants = liens_importants
           )


creer_html("templates/template_categories.html", "../pages-dev/categories.html",  # GENERATION DE LA PAGE CATEGORIES
            categories_liste = get_all_category_card()
           )

creer_html("templates/template_a_propos.html", "../pages-dev/a_propos.html",  # GENERATION DE LA PAGE A Propos
            groupe = etudiants
           )
