''' TP de Farès AZOUAOUI'''

''' Imports eventuels'''

import random as rd

'''Declaration de classe et fonctions'''

class Jeu :
    def __init__(self, n, m):
        '''Constructeur de la classe Jeu
        
        Paramètres: m, la borne maximale du tirage et n, le nombre maximal d'essais
        '''

        self.k = rd.randint(0,m)
        self.n = n
    
    def test(self, k) :
        '''Compare le nombre deviné avec celui a deviner
        
        Paramètres : k, le nombre a deviner
        
        Returns : Booléen: 
        True si le nombre est le même, 
        False si il est trop petit ou trop grand 
        '''

        if k != self.k :
            if k < self.k :
                print("Trop petit")
            if k > self.k :
                print("Trop grand")
            return False
        else :
            print("Super tu as gagné t'es un monstre")
        return True
        
    def jouer(self) :
        ''' Cette méthode fait une boucle jusqu'à ce que le nombre d'essais maximum,n ,soit atteint
        ou jusqu'à ce que le nombre soit trouvé

        Returns : Booléen
        '''

        n = 0
        while n != self.n :
            try :
                k = int(input("Entre un nombre"))
                self.test(k)
                n += 1
                print("Il vous reste", self.n - n,"essais")
            except ValueError :
                print("Ceci n'est pas un entier")
        print("Tu n'as plus d'essais, dommage")


''' Programme principal'''

if __name__ == '__main__' :
    import doctest
    doctest.testmod()

Jeu(15,5).jouer()