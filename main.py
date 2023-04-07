from game import run_game

def main(players, games = 10000):
  results = [run_game(players) for i in range(games)]

  print("Average turns: ", sum([r["turns"] for r in results]) / games)
  print("Average rounds: ", sum([r["rounds"] for r in results]) / games)


if __name__ == "__main__":
  main(6)