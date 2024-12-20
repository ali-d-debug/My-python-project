# my_module.py
"""
Un module Python simple qui effectue des opérations arithmétiques de base.
"""

def add(a: float, b: float) -> float:
    """
    Additionne deux nombres.

    :param a: Premier nombre
    :param b: Deuxième nombre
    :return: Somme de a et b
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Soustrait un nombre d'un autre.

    :param a: Premier nombre
    :param b: Deuxième nombre
    :return: Différence entre a et b
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Multiplie deux nombres.

    :param a: Premier nombre
    :param b: Deuxième nombre
    :return: Produit de a et b
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Divise un nombre par un autre.

    :param a: Numérateur
    :param b: Dénominateur
    :return: Quotient de a et b
    :raises ValueError: Si b est zéro
    """
    if b == 0:
        raise ValueError("Impossible de diviser par zéro.")
    return a / b


def modulo(a: int, b: int) -> int:
    """
    Calcule le reste de la division entière de deux nombres.

    :param a: Dividende
    :param b: Diviseur
    :return: Reste de la division de a par b
    :raises ValueError: Si b est zéro
    """
    if b == 0:
        raise ValueError("Impossible de calculer le modulo avec un diviseur zéro.")
    return a % b


def power(a: float, b: float) -> float:
    """
    Calcule la puissance d'un nombre.

    :param a: Base
    :param b: Exposant
    :return: Résultat de a élevé à la puissance b
    """
    return a ** b

if __name__ == "__main__":
    print("Ceci est un module arithmétique simple.")


