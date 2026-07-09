# Задание 1.1
# Приложение для обучения английскому языку может включать следующие классы:
# * Пользователь;
# * Задания, включают содержимое самого задания, вопросы к нему;
# * Вопросы задания, включают допустимые ответы (правильных ответов может быть несколько);
# * Решения задания, должны указывать на пользователя, задание, содержать информацию о дате и времени,
#   правильности решения, и ответах пользователя.
# Приложение чат может включать следующие классы:
# * Пользователь, включает телефон, электронную почту, логин, пароль, дату и время регистрации, дату рождения;
# * Чат, включает участников чата, сообщения, дату и время создания чата;
# * Сообщение, включает содержимое сообщения, дату и время сообщения, реакции на сообщения.

# Классы на тему игры Stardew Valley
class Player:
    name = 'Player'
    health = 100
    energy = 100
    speed = 0
    tool = None
    boots = None
    level = 1
    slots = 12 # Вместимость рюкзака
    gender = 'man'

class Tool:
    name = 'Топор'
    damage = 10
    level = 1
    cost = 10
    harvestable_resources = ['wood']
    range = 10

class Boots:
    name = 'Ботинки искателя сокровищ'
    armor = 10
    immunity = 50
    cost = 10
    effects = ['light']

player = Player()
print('The player boots are ' + str(player.boots))
print('The player tool is ' + str(player.tool))

boots = Boots()
player.boots = boots
print('The player boots are ' + player.boots.name)

tool = Tool()
player.tool = tool
print('The player tool is ' + player.tool.name)

print('The player tool level is ' + str(player.tool.level))
other_tool = tool
other_tool.level = 2
print('The player tool level is ' + str(player.tool.level))
