from random import randrange
import math

GIVE_LEFT = 1
GIVE_RIGHT = 2
GIVE_CENTER = 3
PASS = [4,5,6]

def run_game(active_players: int) -> int:
  if active_players < 2:
    print("Error: can not run game with fewer than 2 players")
    return 0
  
  players: list = [3] * active_players
  current_player: int = 0
  turn: int = 0
  
  while active_players > 1:
    dice_ct: int = min(3, players[current_player])
    for i in range(dice_ct):
      roll: int = randrange(1, 7)
      
      if (roll in PASS):
        continue
      
      players[current_player] -= 1
      if (players[current_player] == 0):
        active_players -= 1
      
      if (roll == GIVE_CENTER):
        continue
      
      shift: int = 1 if roll == GIVE_RIGHT else -1
      receiving_player: int = (current_player + shift) % len(players)
      
      if (players[receiving_player] == 0):
        active_players += 1
      players[receiving_player] += 1
 
    turn += 1
    current_player = (current_player + 1) % len(players)
      
  
  return {
    "turns": turn,
    "rounds" : math.ceil(turn / len(players)),
    "winner": next((i for i, x in enumerate(players) if x), None)
  }
  