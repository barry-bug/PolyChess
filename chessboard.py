"""


"""

from functools import reduce
from rules import Piece


class Echiquier:
        
    
    def __init__(self):
        
#        self.positions = \
#            [Piece('Tour', 'noir'), Piece('Cavalier', 'noir'), 
#             Piece('Fou','noir'),
#             Piece('Dame', 'noir'), Piece('Tour','noir'),
#             Piece('Fou', 'noir'), 
#             Piece('Cavalier', 'noir'), Piece('Tour', 'noir')] + \
#                \
#            [Piece('Pion', 'noir')] * 8 + \
#                \
#            [Piece()] * 8 * 4 + \
#                \
#            [Piece('Pion', 'blanc')] * 8 + \
#                \
#            [Piece('Tour', 'blanc'), Piece('Cavalier', 'blanc'), 
#             Piece('Fou','blanc'),
#             Piece('Dame', 'blanc'), Piece('Roi', 'blanc'),
#             Piece('Fou', 'blanc'),
#             Piece('Cavalier', 'blanc'), Piece('Tour', 'blanc')]
            
        self.positions = \
            [Piece()] * 8 +  \
                \
            [Piece('Tour', 'noir'), Piece('Cavalier', 'noir'), 
             Piece('Fou','noir'),
             Piece('Dame', 'noir'), Piece('Tour','noir'),
             Piece('Fou', 'noir'), 
             Piece('Cavalier', 'noir'), Piece('Tour', 'noir')] + \
                \
            [Piece()] * 8 + \
                \
            [Piece('Pion', 'noir')] * 8 + \
                \
            [Piece()] * 8 + \
                \
            [Piece('Pion', 'blanc')] * 8 + \
                \
            [Piece('Tour', 'blanc'), Piece('Cavalier', 'blanc'), 
             Piece('Fou','blanc'),
             Piece('Dame', 'blanc'), Piece('Roi', 'blanc'),
             Piece('Fou', 'blanc'),
             Piece('Cavalier', 'blanc'), Piece('Tour', 'blanc')] + \
                \
            [Piece()] * 8

                 
        
    #==============================================================================
    # Construction de l'échiquier
    #==============================================================================
    
    def coordonnees():
        return [lettre + str(chiffre) for chiffre in range(1,9) for lettre in ['A','B','C','D','E','F','G','H']]
    
    
    #==============================================================================
    # Affichage
    #==============================================================================
    
    
    def afficher(self):
    
        lettres = reduce(lambda ele1, ele2 : ele1 + ele2, ["  " + element + "  " for element in ['A','B','C','D','E','F','G','H']])
        interlignes = "    " + reduce(lambda ele1, ele2 : ele1 + ele2, ["-" * 4 + " "] * 8)
        
        
        
        print("   " + lettres)
        print(interlignes)
        
        numLigne = 8
        indexPosition = 0
        
        for piece in self.positions:
            
#            print(ligne)
            
            if indexPosition % 8 == 0:
                print(str(numLigne), end = "  |")
            
            if piece.nom != piece.pieceVide:
                
                print(" " + piece.nomAffichage + " ", end = "|")
        
            else:
                
                print("    ", end = "|")
            
            
            if (indexPosition + 1) % 8 == 0:
                
                print("  " + str(numLigne))
            
                print(interlignes)
            
                numLigne -= 1
                
            indexPosition += 1
            
        print("   " + lettres)
    
        
    
#         A    B    C    D    E    F    G    H  
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    8  | Tn | Cn | Fn | Dn | Rn | Fn | Cn | Tn |  8
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    7  | in | in | in | in | in | in | in | in |  7
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    6  |    |    |    |    |    |    |    |    |  6
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    5  |    |    |    |    |    |    |    |    |  5
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    4  |    |    |    |    |    |    |    |    |  4
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    3  |    |    |    |    |    |    |    |    |  3
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    2  | ib | ib | ib | ib | ib | ib | ib | ib |  2
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    1  | Tb | Cb | Fb | Db | Rb | Fb | Cb | Tb |  1
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#         A    B    C    D    E    F    G    H  
    
    
 
    
#==============================================================================
# Déplacement
#==============================================================================
    
    def deplacerPiece(self, caseDepart, caseArrive):
        
        lettres = ['A','B','C','D','E','F','G','H']
                
        ligDep, colDep = 8 - int(caseDepart[1]), lettres.index(caseDepart[0]) + 1
        ligArr, colArr = 8 - int(caseArrive[1]), lettres.index(caseArrive[0]) + 1
        
        indexDep = ligDep * 8 + colDep - 1
        indexArr = ligArr * 8 + colArr - 1
        
        
#        print(str(ligDep) + "-" + str(colDep))
#        print(str(ligArr) + "-" + str(colArr))
    
        
        self.positions[indexArr] = self.positions[indexDep]
        self.positions[indexDep] = Piece()  
        
    
#==============================================================================
# Vérification déplacement dans la zone
#==============================================================================

    def listeDeplacementsPossibles(self, nomCase):
        
        indexCase = self.nomCaseToIndex(nomCase)
        
        if self.positions[indexCase].nom == self.positions[indexCase].pieceVide:
            
            return []
        
        if self.positions[indexCase].nom == 'Pion':
            return self.positions[indexCase].listeCoupsPossiblesPion(indexCase, self)
            
        if self.positions[indexCase].nom == 'Tour':
            return self.positions[indexCase].listeCoupsPossiblesTour(indexCase, self)
        
        if self.positions[indexCase].nom == 'Fou':
            return self.positions[indexCase].listeCoupsPossiblesFou(indexCase, self)
        
        if self.positions[indexCase].nom == 'Cavalier':
            return self.positions[indexCase].listeCoupsPossiblesCavalier(indexCase, self)
        
        if self.positions[indexCase].nom == 'Dame':
            return self.positions[indexCase].listeCoupsPossiblesDame(indexCase, self)
        
        if self.positions[indexCase].nom == 'Roi':
            return self.positions[indexCase].listeCoupsPossiblesRoi(indexCase, self)
        

    def listeDeplacementsPossiblesFormatCase(self, nomCase):
        
        return [self.indexToNomCase(index) for index in self.listeDeplacementsPossibles(nomCase)]
                

    def afficherDeplacementsPossibles(self, piece):
        
        #afficher '<>' aux endroits possible
        
        
        pass




#==============================================================================
# Fin du jeu
#==============================================================================

    def isEchecEtMat(self):
        return len(list(filter(lambda piece : piece.nom == 'Roi', self.positions))) < 2
    
    
    def couleurEchecEtMat(self):
        
        if not self.isEchecEtMat():
            return None
        
        return 'blanc' if list(filter(lambda piece : piece.nom == 'Roi', self.positions))[0].couleur == 'noir' else 'noir'


#==============================================================================
# Autres fonctions
#==============================================================================
    
    def nomCaseToIndex(self, nomCase):
        
        lettres = ['A','B','C','D','E','F','G','H']
        lig, col = 8 - int(nomCase[1]), lettres.index(nomCase[0]) + 1
        
        return lig * 8 + col - 1
    
    def indexToNomCase(self, indexCase):
        
        return ['A','B','C','D','E','F','G','H'][indexCase % 8] + str(8 - indexCase // 8)
    
    #print("‎• or <>")
    
    
    

    
    
    
    
