from models.player import Player
from models.academy import Academy

from errors.exceptions import InvalidAttributeError
from errors.exceptions import RegistrationError
from errors.exceptions import AcademyDBError
from errors.exceptions import PlayerDoesNotExistError
from errors.exceptions import EmptyAcademyError

try:
    player = Player("Val",15,"CDM",7.4)
except InvalidAttributeError as err:
    print(err)
# else:
#     print("Player initialization successful")
#     print(player)



try:
    academy = Academy("Val Academy")
    (
        academy
            .add_player(Player("Val",15,"CDM",7.4))
            .add_player(Player("Joe",25,"CM",5.3))
            .add_player(Player("Mike",26,"ST",6.0))
    )
    academy.update_academy_players()
except InvalidAttributeError as err:
    print(err)
except RegistrationError as err:
    print(err)
# else:
#     print(len(academy))
#     print(academy)



try:
    academy = Academy("Val Academy")
    academy.load_academy_players()
except AcademyDBError as err:
    print(err)
# else:
#     print(academy)

try:
    academy = Academy("Val Academy")
    academy.load_academy_players()
    player = academy.find_player("Jinx")
except InvalidAttributeError as err:
    print(err)
except PlayerDoesNotExistError as err:
    print(err)
# else:
#     print(player)

try:
    academy = Academy("Val Academy")
    academy.load_academy_players()
    player = academy.remove_player("Jinx")
except InvalidAttributeError as err:
    print(err)
except PlayerDoesNotExistError as err:
    print(err)
# else:
#     print("Player successfully unregistered.")
# finally:
#     academy.update_academy_players()
#     print(academy)

try:
    academy = Academy("Val Academy")
    academy.load_academy_players()
    average_rating = academy.average_rating()
except EmptyAcademyError as err:
    print(err)
# else:
#     print(academy.average_rating)

try:
    academy = Academy("Val Academy")
    academy.load_academy_players()
    top_player = academy.top_player()
except EmptyAcademyError as err:
    print(err)
else:
    print(top_player)