''' TP de Farès AZOUAOUI'''

''' Imports eventuels'''

import random as rd

'''Declaration de classe et fonctions'''

class Jeu :
    def __init__(self, n, m):
        self.k = rd.randint(0,m)
        self.n = n
    
    def test(self, k) :
        if k != self.k :
            if k < self.k :
                print("Trop petit")
            if k > self.k :
                print("Trop grand")
            return False
        else :
            print("Super tu as gagné t'es un monstre")
            return True

''' Programme principal'''

if __name__ == '__main__' :
    import doctest
    doctest.testmod()
