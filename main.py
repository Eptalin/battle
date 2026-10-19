from vocations.vocation import Vocation
from vocations.player_vocations import VOCATIONS
from vocations.enemy_vocations import ENEMY_TYPES

def main():

    # build Player character

    # loop:
        # walk a bit -> random chance of encounter
            # talent flag: decrease encounter chance, shorter distance (Mage: Invisibility)
            # taleng flag: increase encounter chance, longer distance (Fighter: Some kind of charge)

        # if encounter: 
            # randomly select enemy (set level randomly within range around player)
                # talent flag: chance to decrease enemy level (Ranger: Some kind of debilitation)

            # battle
                # if lose:
                    # game over -> display distance covered
            
                # if win:
                    # level up player
    return


if __name__ == "__main__":
    main()