''' TP de Farès AZOUAOUI'''

''' Imports eventuels'''

import random as rd

'''Declaration de classe et fonctions'''

class Jeu :
    def __init__(self, n, m):
        self.k = rd.randint(0,m)
        self.n = n
    
    
''' Programme principal'''

if __name__ == '__main__' :
    import doctest
    doctest.testmod()
