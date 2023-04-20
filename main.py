from game import run_game

def main(players, games = 10000):
  most_win_tracker = [0 for i in range(players)]
  for i in range(100):
    win_tracker = [0 for i in range(players)]
  
    for i in range(games):
      win_tracker[run_game(players)["winner"]] += 1
    
    most_winner = max( (v, i) for i, v in enumerate(win_tracker) )[1]
    most_win_tracker[most_winner] += 1
    
  print(most_win_tracker)

if __name__ == "__main__":
  main(10)