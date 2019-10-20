#
# CS1010X --- Programming Methodology
#
# Mission 15 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hungry_games_classes import *
from engine import *
import simulation
import random

# Rename XX_AI to YourName_AI
class Wira_AI(Tribute):
    def next_action(self):
        # Next action should return a tuple of what your next action should
        # be. For the full list of tuple that your AI can return, refer to
        # the pdf file

        def filter_class(lst, cls): #filtering objects by class
            return list(filter(lambda x: isinstance(x, cls), lst))
        
        #checking inventory
        inventory = self.get_inventory()
        weapons = self.get_weapons()
        rweapons = filter_class(weapons, RangedWeapon)
        ammo = filter_class(inventory, Ammo)
        food = self.get_food()
        medicine = self.get_medicine()

        #checking health/hunger
        health = self.get_health()
        hunger = self.get_hunger()

        #scans objects at current location
        objects = self.objects_around()
        livingthings = filter_class(objects, LivingThing)
        ammo_around = filter_class(objects, Ammo)
        tributes = filter_class(objects, Tribute)

        
        

        no_items = not objects and not inventory
        hungry_no_food = hunger > 80 and not food
        no_food_around = not filter_class(objects, Food)
        no_livingthing = not livingthings
        no_wep =  not weapons and not filter_class(objects, Weapon)
        hungry_nothing = hungry_no_food and no_food_around and no_livingthing and no_wep
        tribute_nowep = tributes and no_wep
        
        #if nothing around and nothing in inventory OR hungry and no food around, walk
        if no_items or hungry_nothing or tribute_nowep:
            exits = self.get_exits()
            if exits:
                index = random.randint(0, len(exits)-1)
                direction = exits[index]
                return ("GO", direction)
            
    
        #if hungry
        if hunger > 80:
            #if food in inventory
            if food:             
                tpl = tuple(filter(lambda x: type(x) != Medicine, food))
                #if no food that is not medicine
                if not tpl:
                    return ("EAT", food[0])
                else:
                    return ("EAT", tpl[0])
            #if food available to pick up
            elif not no_food_around:
                return ("TAKE", filter_class(objects, Food)[0])
        
        #if low health
        if health < 20:
            #if medicine available
            if medicine:
                return ("EAT", medicine[0])
            elif filter_class(objects, Medicine):
                return ("TAKE", filter_class(objects, Medicine)[0])

        #if weapons available and livingthing around
        if weapons and (livingthings or tributes):
            if tributes:
                to_attack = tributes[0]
            else:
                to_attack = livingthings[0]

            #find best damage non-range weapon and best food value livingthing

            nonrangewep = tuple(filter(lambda x: type(x) != RangedWeapon, weapons))
            
            #if non-range wep available
            if nonrangewep:
                maxdamages = tuple(map(lambda x: x.max_damage(), nonrangewep))

                bestdmg = max(maxdamages)

                for weapon in nonrangewep:
                    if weapon.max_damage() == bestdmg:
                        return ("ATTACK", to_attack, weapon)

            #goes here only if ranged weapon available
            loaded = tuple(filter(lambda x: x.shots_left() > 0, weapons))

            
            #if at least 1 weapon loaded
            if loaded:
                print("test")
                maxdamages = tuple(map(lambda x: x.max_damage(), loaded))
                
                bestdmg = max(maxdamages)
                for weapon in loaded:
                    if weapon.max_damage() == bestdmg:
                        return ("ATTACK", to_attack, weapon)

            #goes here if no loaded weapons against livingthing, not Tribute
            if not tributes:
                
                wep_names = tuple(map(lambda x: x.get_name(), rweapons))        
                if ammo:
                    ammo_weptypes = tuple(map(lambda x: x.weapon_type(), ammo))
                    comp_weptypes = tuple(filter(lambda x: x in wep_names, ammo_weptypes))
                    if comp_weptypes:
                        for e in rweapons:
                            if comp_weptypes[0] == e.get_name():
                                weapon = e
                        return ("LOAD", comp_weptypes[0], weapon)
                elif ammo_around:
                    comp_weptypes = tuple(filter(lambda x: x in wep_names, ammo_around))
                    if comp_weptypes: #prioritises compatible ammo
                        return ("TAKE", filter_class(objects, Ammo)[0])
        
        #goes here only if things around, but did not eat/attack/load ammo - 
        #either due to not being urgent (low health/high hunger),
        #or unavailable resources
        #take items in order of importance
        if filter_class(objects, Medicine):
            return ("TAKE", filter_class(objects, Medicine)[0])
        if filter_class(objects, Food):
            return ("TAKE", filter_class(objects, Food)[0])
        if filter_class(objects, Weapon): 
            return ("TAKE", filter_class(objects, Weapon)[0])
        if filter_class(objects, Ammo): 
            return ("TAKE", filter_class(objects, Ammo)[0])
        
            
        #if nothing else, explore
        # As an example: the following code will make your AI just walk around
        # randomly every turn. You do NOT have to use this code if you don't
        # want to!
        exits = self.get_exits()
        if exits:
            index = random.randint(0, len(exits)-1)
            direction = exits[index]
            return ("GO", direction)

        # Otherwise, do nothing
        return None


# NOTE: DO NOT remove the 2 lines of code below.
#
# In particular, you will need to modify the `your_AI = XX_AI` line so that
# `XX_AI` is the name of your AI class.
# For instance, if your AI class is called `MyPrecious_AI`, then you have to
# modify that line to:
#
#     your_AI = MyPrecious_AI
#
# Failure to do so will result in the following exception on Coursemology when
# you run the test cases:
#
#     Traceback (most recent call last):
#       in <module>
#     NameError: name 'your_AI' is not defined
#
# You have been warned!
time_limit = 50 # Modify if your AI needs more than 50 moves for task 2
your_AI = Wira_AI # Modify if you changed the name of the AI class



##################
# Simulation Code
##################
##########
# Task 1 #
##########
# Goal:
# 1. Your AI should be able to pick up a Weapon / RangedWeapon
# 2. Your AI should be able to kill chicken
# 3. Your AI should be able to pick up chicken_meat after killing chicken

# Replace XX_AI with the class name of your AI
# Replace gui=True with gui=False if you do not wish to see the GUI
##simulation.task1(Wira_AI("XX AI", 100), gui=True)


##########
# Task 2 #
##########
## 1. Your AI should be able to pick up a Weapon / RangedWeapon
## 2. Your AI should be able to move around and explore
## 3. Your AI should be able to find harmless Tribute and kill him

# Replace XX_AI with the class name of your AI
# Replace gui=True with gui=False if you do not wish to see the GUI

time_limit = 20    # You may change the time limit if your AI is taking too long
simulation.task2(Wira_AI("XX AI", 100), time_limit, gui=True)



#################
# Optional Task
#################
## You can create your own map and see how your AI behaves!

# Define the parameters of the map
def config():
    ## The game should have a 3x3 map
    game_map = GameMap(3)

    ## You can change the numbers to create different kinds of maps for
    ## the optional task.
    game_config = GameConfig()
    game_config.set_item_count(Weapon, 3)
    game_config.set_item_count(Animal, 2)
    game_config.set_item_count(RangedWeapon, 5)
    game_config.set_item_count(Food, 2)
    game_config.set_item_count(Medicine, 1)

    game = GameEngine(game_map, game_config)

    # Add some dummy tributes
    ryan = Tribute("Ryan", 100)
    waihon = Tribute("Wai Hon", 100)
    soedar = Tribute("Soedar", 100)

    game.add_tribute(ryan)
    game.add_tribute(waihon)
    game.add_tribute(soedar)

    # Yes, your AI can fight with himself
    ai_clone = Wira_AI("AI Clone", 100)
    game.add_tribute(ai_clone)

    return game

# Replace XX_AI with the class name of your AI
# Replace gui=True with gui=False if you do not wish to see the GUI
simulation.optional_task(Wira_AI("XX AI", 100), config, gui=False)
