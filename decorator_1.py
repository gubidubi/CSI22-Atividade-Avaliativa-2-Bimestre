



class TypeComponent: #Componente
    def getDescription(self):
        return self.__class__.__name__
    def getTotalCost(self):
        return self.__class__.cost

class Pizza(TypeComponent): #Componente concreto
    cost = 0.0

class Decorator(TypeComponent): #Decorator
    def __init__(self, TypeComponent):
        self.component = TypeComponent

    def getTotalCost(self):
        return self.component.getTotalCost() + TypeComponent.getTotalCost(self)

    def getDescription(self):
        return self.component.getDescription() + ' ' + TypeComponent.getDescription(self)

class Cheese(Decorator):
    cost = 3.00
    def __init__(self, TypeComponent):
        Decorator.__init__(self, TypeComponent)

class Ham(Decorator):
    cost = 2.45
    def __init__(self, TypeComponent):
        Decorator.__init__(self, TypeComponent)

class Chicken(Decorator):
    cost = 2.00
    def __init__(self, TypeComponent):
        Decorator.__init__(self, TypeComponent)

class Bacon(Decorator):
    cost = 2.50
    def __init__(self, TypeComponent):
        Decorator.__init__(self, TypeComponent)

class Pepperoni(Decorator):
    cost = 3.00
    def __init__(self, TypeComponent):
        Decorator.__init__(self, TypeComponent)

class Tomato(Decorator):
    cost = 1.50
    def __init__(self, TypeComponent):
        Decorator.__init__(self, TypeComponent)

class Oregano(Decorator):
    cost = 0.50
    def __init__(self, TypeComponent):
        Decorator.__init__(self, TypeComponent)

class Shimeji(Decorator):
    cost = 3.00
    def __init__(self, TypeComponent):
        Decorator.__init__(self, TypeComponent)

class Basil(Decorator):
    cost = 0.75
    def __init__(self, TypeComponent):
        Decorator.__init__(self, TypeComponent)

margherita = Cheese(Tomato(Basil(Pizza())))
print(margherita.getDescription() + ": $" + str(margherita.getTotalCost()))

vegan = Shimeji(Tomato(Oregano(Pizza())))
print(vegan.getDescription() + ": $" + str(vegan.getTotalCost()))

pepperoni = Pepperoni(Cheese(Oregano(Pizza())))
print(pepperoni.getDescription() + ": $" + str(pepperoni.getTotalCost()))

cheeken = Cheese(Chicken(Oregano(Pizza())))
print(cheeken.getDescription() + ": $" + str(cheeken.getTotalCost()))

ham_and_bacon = Bacon(Ham(Tomato(Basil(Pizza()))))
print(ham_and_bacon.getDescription() + ": $" + str(ham_and_bacon.getTotalCost()))