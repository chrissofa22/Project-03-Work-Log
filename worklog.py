import sys
import os

from newlog import NewLog
from searchlog import Search

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def terminal():
    clear()
    log = None
    while log is None:
        log = input('''Work Log Terminal. Enter from options 1-3:
      1 Add New Log
      2 Lookup Previous Log
      3 Quit
      \n> ''')
        if log not in ['1', '2', '3']:
            clear()
            print("Invalid input:")
            log = None
    if log == '1':
        NewLog().new()
        clear()
        input("Input Saved. Enter any key to continue:")
    if log == '2':
        menu()
        terminal()
    if log == '3':
        clear()
        print("Terminal Quit")
        sys.exit()
    terminal()

def menu():
        clear()
        option = None
        while option is None:
            option = input('''Enter previous log option:
        1 Find by Date
        2 Find by Time Spent
        3 Find by Exact Search
        4 Find by Pattern
        5 Exit To Terminal
> ''')
            if option not in ['1', '2', '3', '4', '5']:
                clear()
                print("Error. Enter log option:")
                option = None
        if option == '1':
            Search().date()
        if option == '2':
            Search().time()
        if option == '3':
            Search().exact()
        if option == '4':
            Search().pattern()
        if option == '5':
            pass

if __name__ == "__main__":
    terminal()
