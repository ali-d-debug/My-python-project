# test_my_module.py
"""
Tests unitaires pour le module my_module.
"""
# On importe pytest, un framework de test pour Python
import pytest
# On importe les fonctions que l'on souhaite tester depuis le module my_module
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from my_module import add, subtract, multiply, divide, modulo, power

# Test de la fonction 'add' (additionner deux nombres)
def test_add():
    # Vérifie que l'addition de 2 et 3 donne bien 5
    assert add(2, 3) == 5
    # Vérifie que l'addition de -1 et 1 donne bien 0
    assert add(-1, 1) == 0

# Test de la fonction 'subtract' (soustraire un nombre d'un autre)
def test_subtract():
    # Vérifie que la soustraction de 3 à 5 donne bien 2
    assert subtract(5, 3) == 2
    # Vérifie que la soustraction de 3 à 0 donne bien -3
    assert subtract(0, 3) == -3

# Test de la fonction 'multiply' (multiplier deux nombres)
def test_multiply():
    # Vérifie que la multiplication de 4 et 3 donne bien 12
    assert multiply(4, 3) == 12
    # Vérifie que la multiplication de 0 et 3 donne bien 0
    assert multiply(0, 3) == 0

# Test de la fonction 'divide' (diviser un nombre par un autre)
def test_divide():
    # Vérifie que la division de 10 par 2 donne bien 5
    assert divide(10, 2) == 5
    # Vérifie que la fonction lève une exception ValueError lorsqu'on tente de diviser par 0
    with pytest.raises(ValueError):
        divide(10, 0)

# Test de la fonction 'modulo' (calculer le reste de la division entière)
def test_modulo():
    # Vérifie que le modulo de 10 par 3 donne bien 1 (10 divisé par 3 donne un reste de 1)
    assert modulo(10, 3) == 1
    # Vérifie que la fonction lève une exception ValueError lorsqu'on tente de diviser par 0
    with pytest.raises(ValueError):
        modulo(10, 0)

# Test de la fonction 'power' (calculer la puissance d'un nombre)
def test_power():
    # Vérifie que 2 élevé à la puissance 3 donne bien 8 (2^3 = 8)
    assert power(2, 3) == 8
    # Vérifie que tout nombre élevé à la puissance 0 donne bien 1 (par exemple, 5^0 = 1)
    assert power(5, 0) == 1

# Cette section permet de lancer les tests si le script est exécuté directement
if __name__ == "__main__":
    pytest.main()
