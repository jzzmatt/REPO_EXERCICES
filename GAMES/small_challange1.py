'''
Write a program that
Initialize 3 separate list of Words:
 - Animal that live in Water
 - Animal that fly
 - Animal that live on land

 Each Category should have at least 10 words
 Ask the user to select an appropriate category
 write a fct that pulls a random word from the correct category,
 then returns that word for the user
'''

import random
import sys


class Animal_Game(object):
    all_animal = {}

    def __init__(self):
        self.flying = []
        self.water = []
        self.ground = []


    @property
    def get_flying_categories(self):
        return self.flying

    @get_flying_categories.setter
    def get_flying_categories(self, add_animal):
        self.flying.append(add_animal)
        self.all_animal.setdefault("flying_type", self.get_flying_categories)


    @property
    def get_water_categories(self):
        return self.water

    @get_water_categories.setter
    def get_water_categories(self, add_animal):
        self.water.append(add_animal)
        self.all_animal.setdefault("water_type", self.get_water_categories)


    @property
    def get_ground_categories(self):
        return self.ground

    @get_ground_categories.setter
    def get_ground_categories(self, add_animal):
        self.ground.append(add_animal)
        self.all_animal.setdefault("ground_type", self.get_ground_categories)


    def get_categories(self):
        return [k for k in self.get_all_animal().keys()]


    @classmethod
    def get_all_animal(cls):
        '''

        :return: the the Dict of all animal
        '''
        return cls.all_animal




class Menu():

    def __init__(self, animalClass = Animal_Game()):

        self.animalClass = animalClass

        self.choices = {"1": self.animalClass.get_categories(),
                        "2": self.animalClass.get_all_animal(),
                       }

    def display_menu(self):
        print('''
        ANIMAL CATEGORIES

        1. Show Animal Categories
        2. Show All Animal
        4. Adding Animal
        3. Quit

        ''')



    def run(self):

        while True:
            self.display_menu()
            userinput = input("Enter: ")

            if userinput == "4":
                while True:
                    adding = input("Do you Want to Add an Animal? Y or N: ").lower()
                    if adding != "y":
                        break

                    else:

                        print('''
                            Please Select a Categories:
                            [w] Water Animal
                            [f] Flying Animal
                            [g] Ground Animal
                        ''')
                        choose_cat = input("> ").lower()

                        if choose_cat not in ["w", "f", "g"]:
                            print("Refere to the Menu..")
                            continue

                        if choose_cat == "w":
                            self.animalClass.get_water_categories = input("adding an animal: ").lower()


                        if choose_cat == "f":
                            self.animalClass.get_flying_categories = input("adding an animal: ").lower()


                        if choose_cat == "g":
                            self.animalClass.get_ground_categories = input("adding an animal: ").lower()


            elif userinput != "3":
                 print(self.choices.get(userinput))

            else:
                print("Quitting....")
                break



if __name__ == "__main__":
    Menu().run()














