
def addition(x, y):
    """Retourne la somme de x et y"""
    return x + y


def soustraction(x, y):
    return x-y



def noms_binome():
    """
    Affiche les noms des membres du binôme
    Attention, chacun écrit la ligne pour afficher son nom
    """


a = 3
b = 1

print(f"La somme de {a} et {b} vaut {addition(a, b)}")
print(f"La différence de {a} et {b} vaut {soustraction(a, b)}")

noms_binome()
