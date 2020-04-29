from Classe_Node import Node
class BinaryTree :
    def __init__(self,root):
        self.__root = root

    def get_root(self):
        return self.__root

    def isRoot(self,node):
        return node == self.__root

    def size(self,node):
        if node == None :
            return "vide"
        return self.size(Node.get_right())+self.size(Node.get_left()) + 1
        # prends la veleur des noeuds de gauche puis de droite en ajoutant 1 pour compter la racine de l'arbre

    def printValues(self, node):
        if node is None:
            return ""
        else:
            return self.printValues(node.getLeft()) + self.printValues(node.getRight()) + " " + str(node.getVal())

    def sumValues(self,node):
        if node == None :
            return 0
        return self.sumValues(Node.get_right())+self.sumValues(Node.get_left())+Node.get_value()

    def numberLeaves(self,node):
        if node == None :
            return "Pas de feuilles"
        elif Node.get_right()==None and Node.get_left()==None :
            return self.numberLeaves(Node.get_left())+self.numberLeaves(Node.get_right())

    def numberinternalNode(self,node):
        if node == None :
            return 0
        return ((self.size(Node.get_right())+self.size(Node.get_left())) - (self.numberLeaves(Node.get_left())+self.numberLeaves(Node.get_right())))

    def height(self,node):
        if node == Node :
            return "Hauteur de 0"

    def belongs(self,node,val):
        if node == None:
            return False
        elif Node.get_value()==val:
            return True
        return self.belongs(Node.get_left(),val) or self.belongs(Node.get_right(),val)


    def ancestors(self, node,val):
        if node == None :

            return False
        if Node.get_value()== val:
            return True

        elif self.ancestors(Node.get_left(),Node.get_value()) or self.ancestors(Node.get_right(),val ) :# On parcourt l'ensemble des noeuds de l'arbre comme pour belongs
            print(node)

    def descendant(self,node,val):
        if node == None :
            return False
        if val == Node.get_value():
            self.printValues(Node.get_left()) #affichage de tous les noeuds de gauche
            self.printValues(Node.get_right()) #affichage de tous les noeuds de droite
            return True
        else :
            return self.descendant(Node.get_left(),val) or self.descendant(Node.get_right(),val)

    def prefixe(selfs):




if __name__ == '__main__':

    #création des noeuds de l'arbre
    noeud12 = Node(12)
    noeud5 = Node(5)
    noeud17 = Node(17)
    noeud6 = Node(6)
    noeud4 = Node(4)
    noeud19 = Node(19)
    noeud3 = Node(3)
    noeud18 = Node(18)
    noeud21= Node(21)

    #création de la racine de l'arbre
    arbre_binaire = BinaryTree(noeud12)

    #définition des fils/feuilles
    noeud12.set_left(noeud5)
    noeud12.set_right(noeud17)
    noeud5.set_left(noeud4)
    noeud5.set_right(noeud6)
    noeud17.set_right(noeud19)
    noeud4.set_left(noeud3)
    noeud19.set_left(noeud18)
    noeud19.set_right(noeud21)

    print(arbre_binaire.isRoot(12))
    print(arbre_binaire.descendant(12,5))


