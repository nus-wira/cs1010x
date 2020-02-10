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

        HP_THRESHOLD = 70 #for self
        LOW_HP_THRESHOLD = 45 #for self
        HUNGRY_THRESHOLD = 70 #for self
        STRONG_HP_THRESHOLD = 30 #for enemy
        WEP_DMG_THRESHOLD = 15 #for self
        

        #to filter Object lists by Class - includes SubClasses
        def filter_class(lst, cls):
            return list(filter(lambda x: isinstance(x, cls), lst))

        #to filter Object lists by Class - excludes parent/subClasses
        def filter_class_t(lst, cls):
            return list(filter(lambda x: type(x) == cls, lst))

        def get_criteria(x, criteria):
            f = lambda x:x
            if criteria == "food":
                f = lambda x:x.get_food_value()
            elif criteria == "health":
                f = lambda x:x.get_health()
            elif criteria == "medicine":
                f = lambda x:x.get_medicine_value()
            elif criteria == "wild_damage":
                f = lambda x:x.get_damage()
            elif criteria == "wild_atk_prob":
                f = lambda x:x.get_attack_probability()
            elif criteria == "wild_dmg_prob":
                f = lambda x:(x.get_attack_probability()*x.get_damage())
            elif criteria == "wep_damage":
                f = lambda x:(x.max_damage() + x.min_damage())/2
            elif criteria == "ammo":
                f = lambda x:x.get_quantity()
            return f(x)

        #to sort Object lists by criteria
        def sort_obj(lst, criteria):
            lst.sort(key=lambda x:get_criteria(x, criteria), reverse=True)
            return lst
        
        #checking inventory
        inventory = list(self.get_inventory())
        weapons = sort_obj(list(self.get_weapons()), "wep_damage")
        mweapons = filter_class_t(weapons, Weapon) #meleeweapons
        rweapons = filter_class(weapons, RangedWeapon) #rangedweapons
        loaded_rwep = tuple(filter(lambda x: x.shots_left() > 0, rweapons))
        rweapon_types = tuple(map(lambda x:x.get_name(), rweapons))
        ammo = sort_obj(filter_class(inventory, Ammo), "ammo")
        ammotypes = tuple(map(lambda x:x.weapon_type(), ammo))
        comp_rwep_ammo = list(filter(lambda x:x.get_name() in ammotypes, rweapons))
        food = sort_obj(list(self.get_food()), "food")
        food_not_med = filter_class_t(food, Food)
        medicine = sort_obj(list(self.get_medicine()), "medicine")

        #checking health/hunger
        health = self.get_health()
        hunger = self.get_hunger()

        #scans objects at current location, sorted by appropriate criteria
        objects = self.objects_around()
        food_around = sort_obj(list(filter(lambda x:x.get_food_value() > 0,filter_class(objects, Food))), "food")
        med_around = sort_obj(filter_class(objects, Medicine), "medicine")
        wep_around = sort_obj(filter_class(objects, Weapon), "wep_damage")
        mwep_around = filter_class_t(wep_around, Weapon)
        rwep_around = filter_class(wep_around, RangedWeapon)
        ammo_around = sort_obj(filter_class(objects, Ammo), "ammo")
        livingthings = sort_obj(filter_class(objects, LivingThing), "health")
        animals = sort_obj(filter_class(objects, Animal), "health")
        calm = sort_obj(filter_class_t(objects, Animal), "food")
        tributes = sort_obj(filter_class(objects, Tribute), "health")
        wild = filter_class(objects, WildAnimal)
        wild_food = sort_obj(wild, "food")
        wild_dmg = sort_obj(wild, "wild_damage")
        wild_hp = sort_obj(wild, "health")
        wild_att = sort_obj(wild, "wild_atk_prob")
        wild_dmg_prob = sort_obj(wild, "wild_dmg_prob")

        #values to check
        high_tribute_hp = tributes[0].get_health() if tributes else 0
        low_tribute_hp = tributes[-1].get_health() if tributes else 200
        high_wild_dmg = wild_dmg[0].get_damage() if wild else 0
        high_wild_hp = wild_hp[0].get_health() if wild else 0
        low_wild_food = wild_food[-1].get_food_value() if wild else 0
        high_wep = get_criteria(weapons[0], "wep_damage") if weapons else 0
        high_mwep = get_criteria(mweapons[0], "wep_damage") if mweapons else 0
        high_rwep = get_criteria(rweapons[0], "wep_damage") if rweapons else 0

        #bools for situations
        items_av = objects or inventory #items available - in inventory or around
        hungry = hunger > HUNGRY_THRESHOLD
        healthy = health > HP_THRESHOLD
        wep_av =  weapons or wep_around #weapons available
        food_av = food or food_around #food available
        #hungry with no food and no livingthing to kill with a wep
        hungry_nothing = hungry and not food_av and not livingthings and not wep_av
        enemy_nowep = (tributes or wild) and not wep_av
        strong_enemy = high_tribute_hp > STRONG_HP_THRESHOLD or high_wild_hp > STRONG_HP_THRESHOLD
        #strong weapon ready for use
        strong_wep_r = loaded_rwep or high_mwep > WEP_DMG_THRESHOLD

        #run any direction
        def run():
            exits = self.get_exits()
            if exits:
                index = random.randint(0, len(exits)-1)
                direction = exits[index]
                return ("GO", direction)
                
        #loads the highest damage available weapon
        def load_ammo():     
            if comp_rwep_ammo:
                wep = comp_rwep_ammo[0]

                for a in ammo:
                    if wep.get_name() == a.weapon_type():
                        return ("LOAD", wep , a)
                

        if not items_av or hungry_nothing or enemy_nowep:
            return run()
    
        #if hungry
        if hungry and food_av:
            #if food in inventory - save medicine if healthy
            if food_not_med and healthy:
                return ("EAT", food_not_med[0])
            elif food:
                return ("EAT", food[0])
            else:                
                return ("TAKE", food_around[0])
        
        #if unhealthy (<70)
        if not healthy:         
            #if medicine available
            if medicine:
                return ("EAT", medicine[0])
            elif med_around:
                return ("TAKE", med_around[0])

        #if strong enemy around without a strong weapon ready, run
        #high health opponents - should not waste fighting with low damage
        #OR if wild animal could kill in 3 hits, run
        if strong_enemy and not strong_wep_r or 3*high_wild_dmg > health:
            return run()

        
        #if weapons available and livingthing around
        if weapons and livingthings:
            if tributes:
                to_attack = tributes[-1] #weakest tribute
            elif wild:
                to_attack = wild_hp[-1] #weakest wildanimal
            else:
                to_attack = calm[0] #highest food value animal

            #if enemy is strong, prioritise attacking with rangedwep (stronger)
            #saves ammo from weaker enemies
            enemy_hp = to_attack.get_health()
            if enemy_hp > STRONG_HP_THRESHOLD and loaded_rwep:
                return ("ATTACK", to_attack, loaded_rwep[0])

            if mweapons:  
                return ("ATTACK", to_attack, mweapons[0])
        
        
        #take items in order of importance
        if med_around:
            return ("TAKE", med_around[0])
        if food_around:
            return ("TAKE", food_around[0])
        if wep_around:
            return ("TAKE", wep_around[0])
        if ammo_around:
            for a in ammo_around:
                if a.weapon_type() in rweapon_types: #prioritise compatible ammo
                    return ("TAKE", a)
            return ("TAKE", ammo_around[0])
        #load ammo if available compatible ammo type
        if load_ammo(): 
            return load_ammo()
        # As an example: the following code will make your AI just walk around
        # randomly every turn. You do NOT have to use this code if you don't
        # want to!
        if run():
            return run()

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
##    match.gui_simulate_round(0)
