import datetime
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class NewLog():
    def new(self):
        ltask = None
        ltime = None
        lnotes = None
        clear()
        print("New log input.")
        while ltask is None:
            try:
                ltask = input("Enter task:\n> ")
            except TypeError:
                clear()
                print("Enter take name:\n> ")
                ltask = None
            if ltask.isspace() is True or ltask == '':
                clear()
                print("Please enter a valid task:")
            for letter in ltask:
                if letter == ',':
                    clear()
                    print("Enter only alphabetical characters:")
                    ltask = None
        while ltime is None:
            try:
                ltime = int(input("Enter time:\n> "))
            except ValueError:
                clear()
                print("Enter valid whole number:")
                ltime = None
            if ltime not in range(1, 1440):
                clear()
                print("Enter minute value under 24 hours:")
                ltime = None
        while lnotes is None:
            try:
                lnotes = input("Enter notes:\n> ")
            except TypeError:
                clear()
                print("Enter notes information:\n ")
                lnotes = None
            for letter in lnotes:
                if letter == ',':
                    clear()
                    print("Enter only alphabetical characters.")
                    lnotes = None
        ldate = datetime.datetime.now()
        ldate2 = ','.join([ltask, str(ltime),
                               lnotes, str(ldate)])
        try:
            with open("worklog.csv", 'x') as csvfile:
                csvfile.write("Task Name,Time Spent,Notes Information,Date")
            with open("worklog.csv", 'a') as csvfile:
                csvfile.write("\r\n"+ldate2)
        except FileExistsError:
            with open("worklog.csv", 'a') as csvfile:
                csvfile.write("\r\n"+ldate2)
