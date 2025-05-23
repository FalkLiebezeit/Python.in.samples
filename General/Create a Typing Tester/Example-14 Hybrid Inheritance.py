# Hybrid Inheritance

class GrandParent:
    def grandparent_info(self):
        print('Inside Grand Parent class method')

class Parent1(GrandParent):       # Base class
    def parent1_info(self):
        print('Inside Parent1 class method')

class Parent2(GrandParent):       # Base class
    def parent2_info(self):
        print('Inside Parent2 class method')

class Child(Parent1, Parent2):  # Child class of Parent
    def child_info(self):
        print('Inside Child class method')

# Create object of Child classes
obj1 = Child()

# Access Parent class info using Child class object
obj1.grandparent_info()
obj1.parent1_info()
obj1.parent2_info()
obj1.child_info()
