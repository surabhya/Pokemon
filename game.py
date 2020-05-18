# More information about this project can be found in a handout on the class
# website. Be sure to read it before you start programming.



import random 
import pokemon 

# Define a new variable called MOVES that contains a dictionary. As keys, use
# the move variables defined in the pokemon module. The values should be
# 3-tuples. The first value should be a string containing the move name. The
# second value should be the type of the move (use the type variables defined in
# the pokemon module). The third value should be which stat should be targeted
# by the move (HP, attack, defense, or speed... again, use the variables in the
# pokemon module).


MOVES = {pokemon.EMBER:('Ember',pokemon.FIRE,pokemon.HP) , pokemon.GROWL:('Growl',pokemon.NORMAL,pokemon.ATTACK) , pokemon.SCARY_FACE:('Scary Face',pokemon.NORMAL,pokemon.SPEED) , pokemon.SCRATCH:('Scratch',pokemon.NORMAL,pokemon.HP), pokemon.TACKLE:('Tackle',pokemon.NORMAL,pokemon.HP), pokemon.TAIL_WHIP:('Tail Whip',pokemon.NORMAL,pokemon.DEFENSE), pokemon.VINE_WHIP:('Vine Whip',pokemon.GRASS,pokemon.HP), pokemon.WATER_GUN:('Water Gun',pokemon.WATER,pokemon.HP)}

# Define a function called get_all_pokemon that takes one boolean parameter.
# Your function should use the get_new_pokemon function defined in the pokemon
# module to return a list of all possible Pokemon. Use the Pokemon species
# variables defined in the pokemon module as parameters. Additionally, if your
# function's parameter is True, the pokemon returned in the list should be
# wild.

def get_all_pokemon(value):

	if value:
		list_pokemon = [pokemon.get_new_pokemon(pokemon.BULBASAUR,get_move_set(pokemon.BULBASAUR),True), pokemon.get_new_pokemon(pokemon.CHARMANDER,get_move_set(pokemon.CHARMANDER),True), pokemon.get_new_pokemon(pokemon.SQUIRTLE,get_move_set(pokemon.SQUIRTLE),True)]
		return list_pokemon
	else: 
		list_pokemon = [pokemon.get_new_pokemon(pokemon.BULBASAUR,get_move_set(pokemon.BULBASAUR),False), pokemon.get_new_pokemon(pokemon.CHARMANDER,get_move_set(pokemon.CHARMANDER),False), pokemon.get_new_pokemon(pokemon.SQUIRTLE,get_move_set(pokemon.SQUIRTLE),False)]
		return list_pokemon 

# Define a function called get_move_set that takes one parameter, the ID of a
# Pokemon as defined by the variables in the pokemon module, and returns a list
# of move keys as defined by the variables in the pokemon module. The handout
# describes which Pokemon can perform which moves.

def get_move_set(pokemon_id):
	if pokemon_id == pokemon.BULBASAUR:
		moves_bulbasaur = [pokemon.SCARY_FACE,pokemon.TACKLE,pokemon.TAIL_WHIP,pokemon.VINE_WHIP]
		return moves_bulbasaur
	elif pokemon_id == pokemon.CHARMANDER:
		moves_charmander = [pokemon.EMBER,pokemon.GROWL,pokemon.SCRATCH,pokemon.TAIL_WHIP]
		return moves_charmander
	elif pokemon_id == pokemon.SQUIRTLE:
		moves_squirtel = [pokemon.GROWL,pokemon.SCARY_FACE,pokemon.TACKLE,pokemon.WATER_GUN]
		return moves_squirtel

# Define a function called get_npc_move that takes one Pokemon parameter, which
# is the computer's pokemon. Your function should pick a move at random from the
# Pokemon's move list and return its tuple.

def get_npc_move(pokemon):
        pokemon_move_list = pokemon.get_moves()
        rando_move = random.choice(pokemon_move_list)
        return MOVES[rando_move]

# Define a function called get_npc_pokemon that returns a random wild Pokemon.

def get_npc_pokemon():
	pokemon_id = random.choice(pokemon.get_all_pokemon_ids())
	return pokemon.get_new_pokemon(pokemon_id,get_move_set(pokemon_id),True)


# Define a function called get_user_choice that takes two parameters. The first
# parameter should be a list of string options to present to the user. The
# second should be a prompt that single string. Your function should output
# prompt and the choices in the following format and return an index when a user
# has selected a valid option.
# Example: get_user_choice(['Option1', 'Option2', 'Option3'], 'Select one.')
# should output:
# 
# Select one. 
#    0: Option1
#    1: Option2
#    2: Option3
# :: 

def get_user_choice(moves_pokemon,quote):
        while True:
                print quote 
                length = len(moves_pokemon)
                for numbers in range(0,length):
                        print '   ' +str(numbers)+ ': ' + moves_pokemon[numbers]
                user_input= raw_input(":: ")
                if user_input.isdigit():
                        if int(user_input) >= 0 and int(user_input) < length:
                                return int(user_input)



# Define a function called get_user_move that takes one Pokemon parameter and
# uses your get_user_choice function to allow the user to select one of the
# Pokemon's moves. Your function should return the selected move's tuple.

def get_user_move(pokemon):
        moves_pokemon = pokemon.get_moves()
        moves_pokemon_print = []
        for moves in moves_pokemon:
                moves_pokemon_print.append(MOVES[moves][0])
        output = get_user_choice(moves_pokemon_print,str('What will ' + pokemon.get_name().upper() + ' do?'))
        return MOVES[moves_pokemon[output]]

# Define a function called get_user_pokemon that takes no parabmeters. Your
# function should use your get_all_pokemon function to allow the user to select
# a Pokemon. Your function should return the selected Pokemon oject.

def get_user_pokemon():
	pokemons_info = get_all_pokemon(False)
	pokeman_name=[]
	for info in pokemons_info:
		pokeman_name.append(info.get_name())
	output = get_user_choice(pokeman_name,'Select a Pokemon.')
	return pokemons_info[output]


# Define a function called print_hp_meter that takes one Pokemon parameter and
# prints out its hit points (HP). The meter should be thirty characters long and
# adjust based on the percentage of the Pokemon's HP that remains. You can use
# the MAX_HP variable in the pokemon module. The HP meter should be output in
# the following format:
# [               xxxxxxxxxxxxxxx] (50/100)

def print_hp_meter(pokemon):
        present_hp = pokemon.get_hp()
        amount_x = int(((30*present_hp)/100))
        num_space = 30 - amount_x
        if pokemon.is_wild():
                print 'Wild '+ pokemon.get_name().upper()+ ': [' + ' '*num_space + 'x'*amount_x + '] (' + str(int(present_hp)) + '/' + str(100) + ')'
        else:
                print  pokemon.get_name().upper()+ ': [' + ' '*num_space + 'x'*amount_x + '] (' + str(int(present_hp)) + '/' + str(100) + ')'


# Define a function called print_move_result that takes three parameters. The
# first parameter should be a boolean value indicating whether or not the move
# was successful. The second parameter should be a Pokemon object, the Pokemon
# on which the move was performed. The third parameter should be the 3-tuple
# that defines the move itself. If the move was unsuccessful, your function
# should print out: "But it failed!" Your function should print out an
# explanation of the result of running the move. If the move included a damage
# multiplier (according to the get_multiplier function defined in the pokemon
# module), then your function should print out "It's super effective!". Then it
# should print out: "[Wild ]POKEMON NAME's STAT fell!" where "Wild" appears if
# the Pokemon is wild, POKEMON NAME is the name given by the Pokemon object, and
# STAT is the name of the stat effected by the move.

def print_move_result(is_sucess,pokemon_info,moves_tup): 
        if not is_sucess:
                print "But it failed!" 
        else:
                 damage = pokemon.get_multiplier(moves_tup[1],pokemon_info.get_type())
                 if damage == 1.5:
                         if pokemon_info.is_wild():
                                 print 'It\'s super effective!'
                                 print 'Wild ' + pokemon_info.get_name().upper() +'\'s ' + pokemon.get_stat_name(moves_tup[2]).upper() + ' fell!'
                         else:
                                 print 'It\'s super effective!'
                                 print  pokemon_info.get_name().upper() +'\'s ' + pokemon.get_stat_name(moves_tup[2]).upper() + ' fell!'
                 elif damage == 1:
                         if pokemon_info.is_wild():
                                 print  'Wild ' + pokemon_info.get_name().upper() +'\'s ' + pokemon.get_stat_name(moves_tup[2]).upper() + ' fell!'
                         else:
                                 print  pokemon_info.get_name().upper() +'\'s ' + pokemon.get_stat_name(moves_tup[2]).upper() + ' fell!'
                        

# Define a function called play that runs a Pokemon battle. The user should
# select a Pokemon and so should the computer player. Then the user and and
# computer player should each select moves until one Pokemon faints. Your
# function should also output the appropriate messages according to the handout.
# Remember: you can use all of the functions and variables defined in the
# pokemon module!

def play():
        user_pokemon = get_user_pokemon()
        computer_pokemon= get_npc_pokemon()
        print 'WILD ' + computer_pokemon.get_name().upper()  + ' appeared! Go! ' + user_pokemon.get_name().upper() + ' !'
        if user_pokemon.is_faster_than(computer_pokemon):
                   while True:
                        print_hp_meter(user_pokemon)
                        print_hp_meter(computer_pokemon)

                        user_move = get_user_move(user_pokemon)
                        computer_move = get_npc_move(computer_pokemon)
                        
                        did_attack_user = user_pokemon.attack(computer_pokemon,user_move)
                        print user_pokemon.get_name().upper() + ' used ' + user_move[0].upper() + '!'
                        print_move_result(did_attack_user,computer_pokemon,user_move) 
                        if computer_pokemon.is_fainted():
                                print 'Wild ' + computer_pokemon.get_name().upper() + ' fainted!' 
                                break

                        
                        did_attack_computer = computer_pokemon.attack(user_pokemon,computer_move)
                        print  'Wild ' + computer_pokemon.get_name().upper() + ' used ' + computer_move[0].upper() + '!'
                        print_move_result(did_attack_computer,user_pokemon,computer_move)
                        if user_pokemon.is_fainted():
                                print user_pokemon.get_name().upper() + ' fainted!' 
                                break
        else:
                while True:
                        print_hp_meter(user_pokemon)
                        print_hp_meter(computer_pokemon)

                        user_move = get_user_move(user_pokemon)
                        computer_move = get_npc_move(computer_pokemon)

                        did_attack_computer = computer_pokemon.attack(user_pokemon,computer_move)
                        print  'Wild ' + computer_pokemon.get_name().upper() + ' used ' + computer_move[0].upper() + '!'
                        print_move_result(did_attack_computer,user_pokemon,computer_move)
                        if user_pokemon.is_fainted():
                                print user_pokemon.get_name().upper() + ' fainted!' 
                                break

                        did_attack_user = user_pokemon.attack(computer_pokemon,user_move)
                        print user_pokemon.get_name().upper() + ' used ' + user_move[0].upper() + '!'
                        print_move_result(did_attack_user,computer_pokemon,user_move) 
                        if computer_pokemon.is_fainted():
                                print 'Wild ' + computer_pokemon.get_name().upper() + ' fainted!' 
                                break
play() 
