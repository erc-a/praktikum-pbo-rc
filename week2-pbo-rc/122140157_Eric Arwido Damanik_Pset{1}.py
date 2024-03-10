from abc import ABC, abstractmethod
import random

class Parent(ABC):
    def __init__(self, allele_type):
        self.allele_type = allele_type

    @abstractmethod
    def info(self):
        pass

class Father(Parent):
    def __init__(self, allele_type):
        super().__init__(allele_type)

    def info(self):
        return "Father's Allele Type: " + self.allele_type

class Mother(Parent):
    def __init__(self, allele_type):
        super().__init__(allele_type)

    def info(self):
        return "Mother's Allele Type: " + self.allele_type

class Child(Parent):
    def __init__(self, father, mother):
        super().__init__(self.determine_allele_type(father, mother))

    def determine_allele_type(self, father, mother):
        allele_options = [father.allele_type[0] + mother.allele_type[0],
                         father.allele_type[0] + mother.allele_type[1],
                         father.allele_type[1] + mother.allele_type[0],
                         father.allele_type[1] + mother.allele_type[1]]
        return random.choice(allele_options)
    
    def choosing_blood_type(self):
        a = self.allele_type[0]
        b = self.allele_type[1]

        if a == 'A' and b == 'A':
            return "Child's Blood Type: A"
        elif (a == 'A' and b == 'O') or (a == 'O' and b == 'A'):
            return "Child's Blood Type: A"
        elif a == 'A' and b == 'B':
            return "Child's Blood Type: AB"
        elif a == 'B' and b == 'B':
            return "Child's Blood Type: B"
        elif (a == 'B' and b == 'O') or (a == 'O' and b == 'B'):
            return "Child's Blood Type: B"
        elif a == 'O' and b == 'O':
            return "Child's Blood Type: O"
    
    def info(self):
        return "Child's Allele Type: " + self.allele_type


father_allele_type = input("Enter the father's allele type: ")
mother_allele_type = input("Enter the mother's allele type: ")

father = Father(father_allele_type)
mother = Mother(mother_allele_type)
child = Child(father, mother)
print('\n')
print(father.info())
print(mother.info())
print(child.info())
print('\n')
print(child.choosing_blood_type())
