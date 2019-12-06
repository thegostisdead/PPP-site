#!/usr/bin/python3
# =====================
# NOM :jules brossier
# ====================
from jinja2 import * # ne pas modifier

# Ajouter ici les éléments du modèles dont on a besoin
from modele_Index import *

def creer_html(fichier_template, fichier_sortie,**infos):
    """
    fonction qui génère automatiquement un fichier à partir d'un template et d'informations
    paramètres :
            fichier_template : un fichier template (template HTML par exemple)
            fichier_sortie : le nom du fichier généré
            **infos : un nombre indéfini de paramètres qu'il suffit de nommer
    return : Non
    """
    env=Environment(loader=FileSystemLoader('.'),trim_blocks=True)
    template=env.get_template(fichier_template)
    html=template.render(infos)
    f = open(fichier_sortie, 'w')
    f.write(html)
    f.close()


# Ajouter ici les appels à la fonction creer_html
creer_html("Pagination_0_template.html","./Pages_Genere/page-0.html",
            liste_images = liste_des_images(dico_infos_pages,0),
            navigation_page = navigation_page(dico_infos_pages,0),
            page_agenere = 0,
            )
creer_html("Pagination_0_template.html","./Pages_Genere/page-1.html",
            liste_images = liste_des_images(dico_infos_pages,1),
            navigation_page = navigation_page(dico_infos_pages,1),
            page_agenere = 1,
            )
creer_html("Pagination_0_template.html","./Pages_Genere/page-2.html",
            liste_images = liste_des_images(dico_infos_pages,2),
            navigation_page = navigation_page(dico_infos_pages,2),
            page_agenere = 2,
            )
creer_html("Pagination_0_template.html","./Pages_Genere/page-3.html",
            liste_images = liste_des_images(dico_infos_pages,3),
            navigation_page = navigation_page(dico_infos_pages,3),
            page_agenere = 3,
            )
creer_html("Pagination_0_template.html","./Pages_Genere/page-4.html",
            liste_images = liste_des_images(dico_infos_pages,4),
            navigation_page = navigation_page(dico_infos_pages,4),
            page_agenere = 4,
            )
