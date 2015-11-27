from msvcrt import getch
import webbrowser
import os


def print_separator_line():
    print("-" * 50)


def greetings():
    print("Welcome in the blood donor register application!!")
    print_separator_line()


def header_of_menu():
    print_separator_line()
    greetings()


def instructions():
    print("You can step between the menu points via the arrow keys (UP and DOWN).")
    print("If you want to pick an option, press ENTER.")


def main_menu(counter):
    space = " " * 5
    before = [space for i in range(9)]
    arrow = "---> "
    before[counter-1] = arrow
    print("Main menu")
    print(before[0] + "1. Add new donor")
    print(before[1] + "2. Add new donation event")
    print(before[2] + "3. Delete a donor")
    print(before[3] + "4. Delete a donation event")
    print(before[4] + "5. List donor or donation events")
    print(before[5] + "6. Search")
    print(before[6] + "7. Change")
    print(before[7] + "8. Exit")
    print(before[8])
    print()


def first():
    import Donation_User
    Donation_User.UserData2().get_user()


def second():
    import Donation_Location
    Donation_Location.location_app()


def third():
    import User_delete
    User_delete.user_del_app()


def fourth():
    import Location_delete
    Location_delete.loc_del_app()


def fifth():
    import Listing
    Listing.listing()


def sixth():
    import Search
    Search.search_app()


def seventh():
    import Change
    Change.Change().change_within()


def eighth():
    os.system("cls")
    answer_key = ""
    print("Do You want to leave the program really? (Press 'Y' or 'N'!)")
    while answer_key == "":
        answer_key = ord(getch())
        if chr(answer_key) == "y":
            os.system("cls")
            print("But this is so cool program... :(")
            print("Thank for using our Blood Donation Register Software!")
            exit()
        elif chr(answer_key) == "n":
            the_menu()
        else:
            os.system("cls")
            print("Please press 'Y' or 'N'!")
            answer_key = ""


def ninth():
    os.system("cls")
    print("You've found the hidden menu point! You are very cool guy!")
    print("CODECOOL guy! ;)")
    webbrowser.open("https://www.youtube.com/watch?v=_uUBQeJ61nw")

menu_points = [first, second, third, fourth, fifth, sixth, seventh, eighth, ninth]


def the_menu():
    counter = 1
    os.system("cls")
    header_of_menu()
    main_menu(counter)
    instructions()
    while True:
        key = ord(getch())
        if key == 72 and counter > 1:
            counter -= 1
            os.system("cls")
            header_of_menu()
            main_menu(counter)
            instructions()
        elif key == 80 and counter < 9:
            counter += 1
            os.system("cls")
            header_of_menu()
            main_menu(counter)
            instructions()
        elif key == 13:
            menu_points[counter-1]()
            exit()


def ask_answer():
    answer_key = ""
    print("Do you want to go back to the Main Menu? (Press 'Y' or 'N'!)")
    while answer_key == "":
        answer_key = ord(getch())
        if chr(answer_key) == "y":
            the_menu()
        elif chr(answer_key) == "n":
            exit()
        else:
            os.system("cls")
            print("Please press 'Y' or 'N'!")
            answer_key = ""

if __name__ == "__main__":
    the_menu()

# def main_menu():
#     print("Main menu")
#     print("     1. Add new donor")
#     print("     2. Add new donation event")
#     print("     3. Delete a donor")
#     print("     4. Delete a donation event")
#     print("     5. List donor or donation events")
#     print("     6. Search")
#     print("     7. Change")
#     print("     8. Exit \n")


# def check_picked_option(input_str: str):
#     return input_str.isdigit()
#
#
# def valid_picked_option(input_str: str):
#     return int(input_str) in range(1, 10)


# def picked_option():
#     Picked_option_string = ""
#     while Picked_option_string == "":
#         Picked_option_string = input("Pick an option: ")
#         if not check_picked_option(Picked_option_string):
#             print("Your input is not a number, choose from the available menus!")
#             Picked_option_string = ""
#         elif not valid_picked_option(Picked_option_string):
#             print("The menu number is not found, choose from the available menus!")
#             Picked_option_string = ""
#
#     if Picked_option_string == "1":
#         import Donation_User
#         Donation_User.donor_app()
#
#     elif Picked_option_string == "2":
#         import Donation_Location
#         Donation_Location.location_app()
#
#     elif Picked_option_string == "3":
#         import User_delete
#         User_delete.user_del_app()
#
#     elif Picked_option_string == "4":
#         import Location_delete
#         Location_delete.loc_del_app()
#
#     elif Picked_option_string == "5":
#         import Listing
#         Listing.listing()
#
#     elif Picked_option_string == "6":
#         import Search
#         Search.search_app()
#
#     elif Picked_option_string == "7":
#         answer = ""
#         while answer == "":
#             answer = input("Are You sure in your selection?: ")
#             if answer.lower() == "y":
#                 print("Thank for using our Blood Donation Register Software!")
#                 exit()
#             elif answer.lower() == "n":
#                 the_menu()
#             else:
#                 print("Press 'Y' or 'N'!")
#                 answer = ""
#
#     elif Picked_option_string == "8":
#         pass
#
#     elif Picked_option_string == "9":
#         webbrowser.open("https://www.youtube.com/watch?v=_uUBQeJ61nw")
