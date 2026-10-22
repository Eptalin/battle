import random

from characters.enemy import Enemy 


# Generate an enemy object.
def generate_enemy(enemy_pool, player_level):
    # Select an enemy type from the list and randomly set their level.
    enemy_type = random.choice(enemy_pool)
    enemy_level = set_enemy_level(player_level)

    return Enemy(enemy_type, enemy_level)


# Randomly set the enemy's level using the player level as a base.
def set_enemy_level(player_level):
    n = random.random()
    
    if n > .95:
        # 5% chance of super strong enemy
        return player_level + 2
    
    if n > .75:
        # 20% chance of strong enemy
        return player_level + 1
    
    if n < .05 and player_level > 2:
        # 5% chance of super weak enemy (min Lvl.1)
        return player_level - 2
    
    if n < .25 and player_level > 1:
        # 20% chance of weak enemy (min Lvl.1)
        return player_level - 1

    # 50% chance of normal strength enemy
    return player_level