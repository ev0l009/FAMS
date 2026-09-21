from models.academy import Academy

academy = Academy("Val Academy")
academy.load_academy_players()
print(academy.average_rating())