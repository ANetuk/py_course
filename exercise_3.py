class Player:
    def __init__(self, name, health, energy, speed, tool, boots, level, slots, gender):
        self.name = name
        self.health = health
        self.energy = energy
        self.speed = speed
        self.tool = tool
        self.boots = boots
        self.level = level
        self.slots = slots
        self.gender = gender

    def up_level(self, level, health, energy):
        self.level = level
        self.health = health
        self.energy = energy

    def equip_tool(self, tool):
        self.tool = tool

    def equip_boots(self, boots):
        self.boots = boots

class Tool:
    def __init__(self, name, damage, level, base_cost, harvestable_resources, distance, effects = None):
        self.effects = effects if effects is not None else []
        self.name = name
        self.level = level
        self.damage = damage
        self.base_cost = base_cost
        self.harvestable_resources = harvestable_resources
        self.distance = distance

    def up_level(self, level, damage, base_cost):
        self.level = level
        self.damage = damage
        self.base_cost = base_cost

    def add_effect(self, effect):
        self.effects.append(effect)

    def get_total_cost(self):
        effect_cost = 10
        return self.base_cost + len(self.effects) * effect_cost

class Boots:
    def __init__(self, name, armor, immunity, cost, effects = None):
        self.effects = effects if effects is not None else []
        self.name = name
        self.armor = armor
        self.immunity = immunity
        self.cost = cost

player = Player('Player', 100, 100, 100, None, None, 1, 12, 'Man')
print('The player tool is ' + str(player.tool))
print('The player boots are ' + str(player.boots))
print('The player level is ' + str(player.level))
print('The player health is ' + str(player.health))
print('The player energy is ' + str(player.energy))

axe = Tool('Axe', 10, 1, 10, ['Tree'], 10, [])
player.equip_tool(axe)
print('The player tool is ' + player.tool.name)
print('The axe level is ' + str(axe.level))
print('The axe damage is ' + str(axe.damage))
print('The axe total cost is ' + str(axe.get_total_cost()))

treasureHunterBoots = Boots('Treasure hunter boots', 10, 50, 20, [])
player.equip_boots(treasureHunterBoots)
print('The player boots are ' + player.boots.name)

player.up_level(2, 110, 110)
print('The player level is ' + str(player.level))
print('The player health is ' + str(player.health))
print('The player energy is ' + str(player.energy))

axe.up_level(2, 20, 20)
print('The axe level is ' + str(axe.level))
print('The axe damage is ' + str(axe.damage))
print('The axe total cost is ' + str(axe.get_total_cost()))

axe.add_effect('Swiftness')
print('The axe total cost is ' + str(axe.get_total_cost()))
print('The axe effects are ' + str(axe.effects))
