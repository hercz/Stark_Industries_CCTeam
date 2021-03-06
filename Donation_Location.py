__author__ = 'Gazdik_Zsolt'
import datetime

class User_Data(object):

    @staticmethod
    def date_string_is_valid(date_string: str):
        splitted_date = date_string.split(".")
        if not (len(splitted_date) == 3 and splitted_date[0].isdigit() and
            splitted_date[1].isdigit() and splitted_date[2].isdigit()):
            return False
        try:
            datetime.date(int(splitted_date[0]), int(splitted_date[1]), int(splitted_date[2]))
            return True
        except ValueError as vex:
            print("This date is not correct!")
            return False

    def __init__(self):
        
        self.get_Date_of_Event()

        self.get_Start_Time()
        self.get_Zip_Code()
        self.get_City()
        self.get_Address()
        self.get_Beds_Available()
        self.get_Planned_Donor_Number()

    #Inputs, gets


    def get_Date_of_Event(self):
        date_of_event = ""
        while date_of_event == "":
            date_of_event = input("Please enter the date of your birth in format YYYY.MM.DD: ")
            if User_Data.date_string_is_valid(date_of_event) is False:
                print("Please enter a valid date (e. g. 1991.05.26)! ")
                date_of_event = ""
            else:
                self.date_of_event = date_of_event
            if User_Data.date_string_is_valid(date_of_event) is True:
                self.date_of_event_ten_days_before()
                self.date_weekdays()


    def date_of_event_ten_days_before(self):
        today = datetime.date.today()
        date_of_event = datetime.datetime.strptime(self.date_of_event, "%Y.%m.%d").date()
        if (date_of_event - today).days < 10:
            print("Sorry you must organize it at least 10 days from now!!")
            self.get_Date_of_Event()

    def date_weekdays(self):
        date_of_event = datetime.datetime.strptime(self.date_of_event, "%Y.%m.%d").date()
        if datetime.datetime.isoweekday(date_of_event) >5:
            print("Sorry you must organize it on weekdays (Monday-Friday!")
            self.get_Date_of_Event()







    def get_Start_Time(self):
        start_time = ""
        while start_time == "":
            start_time = input("Please enter the start time of event: ")
            while not start_time.isdigit and (24 > start_time >= 0):
                print("Please write in correct form HH!")
                start_time = ""
        self.start_time = start_time

    def get_End_Time(self):
        pass

    def get_Zip_Code(self):
        zip_code = ""
        while zip_code == "":
            zip_code = input("Please enter your ZIP code ")
            if len(zip_code) != 4:
                print("You must enter a valid ZIP code")
                zip_code = ""
            elif zip_code[0] == '0':
                print("Your first character can't be Zero")
                zip_code = ""
            elif not zip_code.isdigit():
                print("You must enter positive numbers ")
                zip_code = ""
            elif len(zip_code) == 4:
                self.zip_code = zip_code

    def get_City(self):
        city = ""
        city_names = ("miskolc", "kazincbarcika", "szerencs", "sarospatak")
        while city == "":
            city = input("Please enter your city name: ")
            if city.lower() not in city_names:
                print("You must fill this and city names must be: Miskolc, Kazincbarcika, Szerencs, Sarospatak")
                city = ""
        self.city = city.lower()


    def get_Address(self):
        address = ""
        while address == "":
            address = input("Please enter your address: ")
            if len(address) > 25:
                print("Address should be less then 25 characters!")
                address = ""
        self.address = address

    def get_Beds_Available(self):
        available_beds = ""
        while available_beds == "":
            available_beds = input("Please enter the number of available beds: ")
            if not available_beds.isdigit():
                print("Please enter a positive intiger!")
                available_beds = ""
            if available_beds == "0":
                print("You should enter a positive intiger!")
                available_beds = ""
        self.available_beds = available_beds

    def get_Planned_Donor_Number(self):
        planned_donor_number = ""
        while planned_donor_number == "":
            planned_donor_number = input("Please enter th planned donor number: ")
            if not planned_donor_number.isdigit():
                print("Please enter a positive intiger!")
                planned_donor_number = ""
            if planned_donor_number == "0":
                print("You should enter a positive intiger!")
                planned_donor_number = ""
        self.planned_donor_number = planned_donor_number

    # FUNCTIONS

    def Registration_ten_days_before_date(self):
        pass

    def Datetime_Only_on_Weekdays(self):
        pass

    def Calculate_Duration_in_Minutes(self):
        pass

    def Maximum_Donor_Number(self):
        pass

    def print_donor(self):
        print(self.planned_donor_number)

if __name__ == "__main__":
    gaspar = User_Data()
    gaspar.print_donor()