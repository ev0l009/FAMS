from models.academy import Academy

academy = Academy("Val Academy")
academy.load_academy_players()
players = list(academy.players.values())
print(players)