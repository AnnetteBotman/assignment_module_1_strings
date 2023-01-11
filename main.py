# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# Dit is een opdracht over de UEFA-cup finale tussen Nederland en Soviet Unie in 1988
score_player_1 = "Ruud Gullit"
score_player_2 = "Marco van Basten"
goal_0 = 32
goal_1 = 54
scorers = score_player_1 + " " + \
    str(goal_0) + ', ' + score_player_2 + " " + str(goal_1)
# creates a variable of the players that scored en the minute in which that happened.
print(scorers)
report = (f"{score_player_1} scored in the {goal_0}nd minute\n{score_player_2} scored in the {goal_1}th minute")
print(report)

player = "Adri van Tiggelen"
first_name = player[0:player.find(' ')]
print(first_name)

last_name = player[player.find(' ') + 1:]
print(last_name)

last_name_len = len(last_name)
print(last_name_len)

name_short = player[0] + ". " + last_name
print(name_short)

chant = str.strip((first_name+"! ") * len(first_name))
print(chant)

good_chant = chant[-1] != ''
print(good_chant)
