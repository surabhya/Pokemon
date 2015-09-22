"""The pokemon module. Should be in a file called pokemon.py"""

import random

BULBASAUR = 1
CHARMANDER = 4
SQUIRTLE = 7

ATTACK = 0
DEFENSE = 1
HP = 2
SPEED = 3

FIRE = 0
GRASS = 1
NORMAL = 2
WATER = 3

EMBER = 'ember'
GROWL = 'growl'
SCARY_FACE = 'scaryface'
SCRATCH = 'scratch'
TACKLE = 'tackle'
TAIL_WHIP = 'tailwhip'
VINE_WHIP = 'vinewhip'
WATER_GUN = 'watergun'

MAX_HP = 100


def get_multiplier(move_type, pokemon_type):
  return (1.5
  if (
      (move_type == GRASS and pokemon_type == WATER) or
      (move_type == FIRE and pokemon_type == GRASS) or
      (move_type == WATER and pokemon_type == FIRE))
  else 1)


def get_stat_name(stat):
  if stat == ATTACK:
    return 'attack'
  elif stat == DEFENSE:
    return 'defense'
  elif stat == HP:
    return 'hp'
  elif stat == SPEED:
    return 'speed'
  else:
    return None


def get_all_pokemon_ids():
  return [BULBASAUR, CHARMANDER, SQUIRTLE]


def get_new_pokemon(pokemon_id, moves, is_wild):
  return Pokemon(pokemon_id, moves, is_wild)


class Pokemon:
  def __init__(self, pokemon_id, moves, is_wild=False):
    self._HP = MAX_HP
    self._ATTACK = 5.0
    self._DEFENSE = 5.0
    self._MOVES = moves
    self._SPEED = 5.0
    self._TYPE = NORMAL
    self._WILD = is_wild

    if pokemon_id == BULBASAUR:
      self._NAME = 'Bulbasaur'

      self._ATTACK = 10.0
      self._TYPE = GRASS
    elif pokemon_id == CHARMANDER:
      self._NAME = 'Charmander'

      self._SPEED = 10.0
      self._TYPE = FIRE
    elif pokemon_id == SQUIRTLE:
      self._NAME = 'Squirtle'

      self._DEFENSE = 10.0
      self._TYPE = WATER
    else:
      self._NAME = 'Invalid'
      self._HP = -1

  def absorb_damage(self, damage, stat):
    if stat == ATTACK:
      self._ATTACK -= damage
    elif stat == DEFENSE:
      self._DEFENSE -= damage
    elif stat == HP:
      self._HP -= damage
    elif stat == SPEED:
      self._SPEED -= damage

  def attack(self, other_pokemon, move):
    if random.randrange(100) < 85:
      multiplier = get_multiplier(move[1], other_pokemon.get_type())
      other_pokemon.absorb_damage(
          int(round(
              (max(self.get_attack(), 0) /
               max(other_pokemon.get_defense(), 1)) *
              5 *
              multiplier)),
          move[2])
      return True
    return False

  def get_attack(self):
    return self._ATTACK

  def get_defense(self):
    return self._DEFENSE

  def get_hp(self):
    return self._HP

  def get_moves(self):
    return self._MOVES

  def get_name(self):
    return self._NAME

  def get_speed(self):
    return self._SPEED

  def get_type(self):
    return self._TYPE

  def is_fainted(self):
    return self._HP <= 0

  def is_faster_than(self, other_pokemon):
    return (
        self.get_speed() > other_pokemon.get_speed() or
        (self.get_speed == other_pokemon.get_speed() and
         random.choice([True, False])))

  def is_wild(self):
    return self._WILD
