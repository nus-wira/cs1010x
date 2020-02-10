#
# CS1010X --- Programming Methodology
#
# Contest 15.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hungry_games_classes import *
from contest_simulation import *
import random


class Player(Tribute):
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

        # As an example: the following code will make your AI just walk around
        # randomly every turn. You do NOT have to use this code if you don't
        # want to!
        if self.get_exits():
            direction = random.choice(self.get_exits())
            return ("GO", direction)

        # Otherwise, do nothing
        return None


#######################################
# Testing Code
#######################################

# We only execute code inside the if statement if this file is
# not being imported into another file
if __name__ == '__main__':
    def qualifer_map(size, wrap):
        game_config = GameConfig()
        game_config.set_item_count(Weapon, 10)
        game_config.set_item_count(RangedWeapon, 10)
        game_config.set_item_count(Food, 10)
        game_config.set_item_count(Medicine, 10)
        game_config.set_item_count(Animal, 10)
        game_config.steps = 1000

        def spawn_wild_animals(game):
            for i in range(3):
                animal = DefaultItemFactory.create(WildAnimal)
                game.add_object(animal[0])
                GAME_LOGGER.add_event("SPAWNED", animal[0])
        game_config.add_periodic_event(20, spawn_wild_animals, "Spawn Wild Animals")

        return (GameMap(size, wrap=wrap), game_config)

    # Create 6 AI Clones
    tributes = []
    for i in range(6):
        # An AI is represented by a tuple, with the Class as the first element,
        # and the name of the AI as the second
        ai = (Player, "AI" + str(i))
        tributes.append(ai)

    # Qualifier Rounds
    # Uncomments to run more rounds, or modify the rounds list
    # to include more rounds into the simulation
    # (Note: More rounds = longer simulation!)
    rounds = [qualifer_map(4, False),
              #qualifer_map(4, False),
              #qualifer_map(4, False),
              qualifer_map(4, True),
              #qualifer_map(4, True),
              #qualifer_map(4, True),
             ]



    match = Match(tributes, rounds)
    print("Simulating matches... might take a while")

    # Simulate without the graphics
    match.text_simulate_all()

    # Simulate a specific round with the graphics
    # Due to limitation in the graphics framework,
    # can only simulate one round at a time
    # Round id starts from 0
    #match.gui_simulate_round(0)
