def print_separator_line():
    print("-" * 32)


def greetings():
    print("Welcome in the blood donor register application!!")
    print_separator_line()


def Main_Menu():
    #print("If you want to use Donor registration application, type in: user")
    print("Main menu")
    print("     1. I want to add a new guy, bro!!")
    print("     2. How about a new donation event? Yeah! That's what i want!")
    print("     3. Genie make a donor disappear!")
    print("     4. Obama destroy event protocol..")
    print("     5. Show me everyone and everything The way I want!")
    print("     6. Search and...? SEARCH")
    print("     7. Exit \n")

    #print("\n Choose what you want: ")
    #print("If you want to use Donation event registration application, type in: loc")

if __name__ == "__main__":
    print_separator_line()
    greetings()
    Main_Menu()
    Picked_option_string = ""
    while Picked_option_string == "":
        #Main_Menu()
        Picked_option_string = input("Pick an option: ")
        if not (Picked_option_string == "1" or Picked_option_string == "2" or Picked_option_string == "3" or \
                Picked_option_string == "4" or Picked_option_string == "5" or Picked_option_string == "6" or \
                Picked_option_string == "7"):
            print("Your input is invalid, choose from the available menus!")
            Picked_option_string = ""
    if Picked_option_string == "1":
        import Donation_User as user

        print_separator_line()
        print("Welcome in Donor registration application!")
        print()
        person = user.User_Data()
        print()
        print_separator_line()
        print("The user main data: ")
        print()
        print(person.data_dictionary()['name'], '\n',
              str(person.data_dictionary()['weight']), ' kg\n',
              person.data_dictionary()['date of birth'], ' - ', person.data_dictionary()['age'], ' years old\n',
              person.data_dictionary()['e-mail'])
        print()
        print("Thank for your registration (and your blood)!")
    if Picked_option_string == "2":
        import Donation_Location as location

        print_separator_line()
        print("Welcome in Donation event registration application!")
        print()
        location = location.User_Data()
        print()
        print("Thank for your registration (and your blood)!")

    if Picked_option_string == "3":
        pass

    if Picked_option_string == "4":
        pass

    if Picked_option_string == "5":
        pass

    if Picked_option_string == "6":
        pass

    if Picked_option_string == "7":
        exit()
