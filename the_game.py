from actors import Creature, Supervisor, Boss, Hero
import random

class Room:
    def __init__(self, name, monster, loot, clear):
        self.name = name
        self.monster = monster
        self.loot = loot
        self.clear = clear

def main():
    print_header()
    # create_character()
    game_loop()


def print_header():
    print('*********************************')
    print('       OFFICES AND BOSSES')
    print('*********************************')
    print()


def take_elevator(current_floor, has_key = False):
    if has_key == False:
        print('Find the keycard to take the elevator to the next level')
        return current_floor
    else:
        print("going up")
        print("<elevator music")
        return current_floor + 1


def game_loop():
    creatures = [
        Creature('Copy Boy', 5),
        Creature('Pam from Accounting', 1),
        Creature('Jeannie', 12),
        Supervisor('Office Manager', 50, scaliness=2, breaths_fire=False),
        Boss('Lumbergh', 1000),
    ]

    hero = Hero('Peter', 75)

    items = [
        'stapler',
        'coffee mug',
        'white board',
        'laptop',
        'notebook',
        'nerf gun',
        'printer',
        'key card'
    ]

    rooms = [
        'Corner Office',
        'Break Room',
        'Mop Closet',
        'Lobby',
        'Cubicle',
        'Office'
    ]

    while True:

        active_creature = random.choice(creatures)
        room_choice = random.choice(rooms)
        loot = random.choice(items)
        active_room = Room(room_choice, active_creature, loot, False)
        key_card = False

        print('You enter the {} and inside is a {} of level {} '
              .format(active_room.name, active_creature.name, active_creature.level))
        print()

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
                rooms.remove(active_room.name)
                items.remove(loot)
                if loot == 'key card':
                    key_card = True
                print("The hero defeated {}".format(active_creature.name))
                print("The {} dropped {}.".format(active_creature.name, loot))
            else:
                print("The hero has been defeated by the powerful {}".format(active_creature.name))
        elif cmd == 'r':
            print('The hero has become unsure of his abilities and flees!!!')
        elif cmd == 'l':
            print('The hero {} takes in the surroundings and sees:'
                  .format(hero.name))
            for c in creatures:
                print(" * {} of level {}".format(
                    c.name, c.level
                ))
        else:
            print("OK, exiting game... bye!")
            break

        if not creatures:
            print("You've defeated all the creatures, well done!")
            break

        print()

if __name__ == '__main__':
    main()