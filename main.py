from models.player import Player
from models.academy import Academy

from errors.exceptions import InvalidAttributeError
from errors.exceptions import RegistrationError
from errors.exceptions import AcademyDBError
from errors.exceptions import PlayerDoesNotExistError
from errors.exceptions import EmptyAcademyError

main_menu_text: str = (
    "Welcome to Football Academy Management Service (FAMS).\n\n"
    "1. Academy Info\n"
    "2. Add player\n"
    "3. Remove player\n"
    "4. Find player\n"
    "5. Get top Player\n"
    "6. Get average rating\n"
    "7. Save academy session\n"
    "8. Clear academy records\n"
    "9. Exit\n\n"
    "Select an option to proceed: "
)

add_player_text: str = (
    "=============================\n"
    "     Player Registration\n"
    "=============================\n\n"
    "Enter the required player details.\n"
)

remove_player_text: str = (
    "=============================\n"
    "     Remove player\n"
    "=============================\n\n"
    "Enter player name.\n"
)

find_player_text: str = (
    "=============================\n"
    "     Find player\n"
    "=============================\n\n"
    "Enter player name.\n"
)

top_player_text: str = (
    "=============================\n"
    "     Top player\n"
    "=============================\n\n"
)

average_rating_text: str = (
    "=============================\n"
    "     Average Rating\n"
    "=============================\n\n"
)

clear_academy_records_text: str = (
    "WARNING!!! This will delete all your data. You won't be able to retrieve deleted data.\n"
    "1. Proceed\n"
    "Press 1 and Enter to proceed or just Enter to go back"
)

def return_to_menu() -> str:
    input("\nPress Enter to return to main menu")
    return "0"

def run_academy():
    opt: str = "0"
    attempts: int = 3

    academy = Academy("Val FA")

    academy.load_academy_players()

    opt = "0"
    while opt != "9":
        opt = input(main_menu_text)
        if opt == "1":
            print()
            print(academy)
            opt = return_to_menu()

        elif opt == "2":
            print()
            print(add_player_text)

            try:
                academy.add_player(
                    Player(
                        input("Player name: "), 
                        input("Player age: "), 
                        input("Playing position: "), 
                        input("Player rating: ")
                    )
                )
            except InvalidAttributeError as err:
                print(err)
            except RegistrationError as err:
                print(err)
            else:
                print("Player registration successful.")
            finally:
                opt = return_to_menu()


        elif opt == "3":
            print()
            print(remove_player_text)

            try:
                player = academy.remove_player(
                    input("Input player name: ")
                )
            except InvalidAttributeError as err:
                print(err)
            except PlayerDoesNotExistError as err:
                print(err)
            else:
                print("Player successfully unregistered.")
            finally:
                opt = return_to_menu()


        elif opt == "4":
            print()
            print(find_player_text)

            try:
                player = academy.find_player(
                    input("Input player name: ")
                )
            except InvalidAttributeError as err:
                print(err)
            except PlayerDoesNotExistError as err:
                print(err)
            else:
                print(player)
            finally:
                opt = return_to_menu()


        elif opt == "5":
            print()
            print(top_player_text)

            try:
                top_player = academy.top_player()
            except EmptyAcademyError as err:
                print(err)
            else:
                print(top_player)
            finally:
                opt = return_to_menu()


        elif opt == "6":
            print()
            print(average_rating_text)

            try:
                average_rating = academy.average_rating()
            except EmptyAcademyError as err:
                print(err)
            else:
                print(f"APAR: {average_rating}")
            finally:
                opt = return_to_menu()


        elif opt == "7":
            try:
                academy.save_academy_players()
            except AcademyDBError as err:
                print(err)
            else:
                print("Academy Data Updated!")
            finally:
                opt = return_to_menu()


        elif opt == "8":
            print(clear_academy_records_text)
            opt = input("Select an option: ")            
            if opt == "1":
                academy.clear_academy_records()
                print("Successfully cleared academy data.")
            print("\nReturning to menu...")
            opt = return_to_menu()

        attempts -= 1
        if attempts > 0:
            print(
                "Please select a valid option.\n"
                f"Tries remaining: {attempts}"
            )
            continue
        opt = "9"
    print("Exiting FAMS")

run_academy()