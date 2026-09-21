from models.player import Player
from models.academy import Academy

from errors.exceptions import InvalidAttributeError
from errors.exceptions import RegistrationError

# try:
#     player = Player("Val",15,"CDM",7.4)
# except InvalidAttributeError as err:
#     print(err)
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
else:
    print(len(academy))
    print(academy)