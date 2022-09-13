from hexgame import HexGame

h = HexGame(11, 0)
winner = h.start_game()
print("winner: %d" % winner)
h.show_winner(winner)
