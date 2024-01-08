def show_manual_intro():
    return ">>> Bonjour,\n" \
           "Ce manuel va vous aider a comprendre comment bien utiliser **Snow**."


def show_manual_global():
    return ">>> ### Voici quelques commandes globales :\n" \
           "- **/manual** (ou /man) -> Permet d'acceder a ce manuel\n" \
           "- **/add_word** -> permet d'ajouter un mot (ou une liste de mots) a la black liste\n"


def show_manual_history():
    return ">>> ### Voici quelques commandes utiles concernant l'utilisation " \
           "et la gestion de l'historique de commande :\n" \
           "- **/show_all** (ou /sa) -> Permet d'afficher votre historique \n" \
           "- **/show_last** (ou /sl) -> Permet d'afficher uniquement la dernière commande rentrée \n" \
           "- **/clear** (ou /c) -> Permet de supprimer votre l'historique"


def show_manual_black_list():
    return ">>> Qu'est ce qu'est la **black liste** (ou filtre) ?\n" \
           "La black liste est une liste de mots qui sont bani par **Snow**,\n" \
           "Si ce mot apparait dans un message, ce message cera supprimé et son auteur recevra un avertissement\n" \
           "(Dans le futur, si une personne ressoit trois avertissement elle recevera un TO (Time out) de 60 secondes)"


def lien_github():
    return ">>> Voici le lien du repo github ou vous pouvez trouver le code de **Snow**\n" \
           "- https://github.com/DannyLap/Snow_Bot.git"
