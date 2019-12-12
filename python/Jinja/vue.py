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



creer_html("template_index.html","../../Pages_Genere/index.html", #GENERATION DE LA PAGE INDEX
            
            )

creer_html("template_a_propos.html","../../Pages_Genere/index.html", #GENERATION DE LA PAGE A_PROPOS
            
            )

creer_html("template_aide.html","../../Pages_Genere/index.html", #GENERATION DE LA PAGE AIDE
            
            )

creer_html("template_categories.html","../../Pages_Genere/index.html", #GENERATION DE LA PAGE CATEGORIES
            
            )

creer_html("template_recherches.html","../../Pages_Genere/index.html", #GENERATION DE LA PAGE RECHERCHES
            
            )