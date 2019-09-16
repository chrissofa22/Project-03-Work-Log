import os
import csv
import re

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Search():
    def __init__(self):
        with open('worklog.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            self.entries = list(reader)
            self.proxy = []

    def show(self, entry):
        print('''
        Task Name: {}
        Time Spent: {}
        Notes Information: {}
        Date: {}
        '''.format(entry['Task Name'], entry[' Time Spent'], entry[' Notes Information'],
                   entry[' Date']))

    def date(self):
        clear()
        search = input(("Enter a date:\n> "))
        for entry in self.entries:
            if entry[' Date'] not in self.proxy:
                self.proxy.append(entry[' Date'])
        dates = sorted(self.proxy)
        for date in dates:
            print(" "*8 + date)
        search = input('> ')
        clear()
        print("Listed logs:")
        for entry in self.entries:
            if entry[' Date'] == search:
                Search().show(entry)
        input('\nENTER to redirect to MENU. ')

    def time(self):
        clear()
        search = input(("Enter time spent:\n> "))
        for entry in self.entries:
            if entry[' Time Spent'] not in self.proxy:
                self.proxy.append(entry[' Time Spent'])
        times = sorted(self.proxy)
        for time in times:
            print(" "*8 + time)
        search = input("\n> ")
        clear()
        print("Listed logs:")
        for entry in self.entries:
            if entry[' Time Spent'] == search:
                Search().show(entry)
        input('ENTER to redirect to MENU. ')

    def exact(self):
        clear()
        search = input(("Enter exact info:\n> "))
        print("Listed logs:")
        for entry in self.entries:
            if entry['Task Name'] == search:
                Search().show(entry)
            elif entry[' Notes Information'] == search:
                Search().show(entry)
        input('ENTER to redirect to MENU. ')

    def pattern(self):
        clear()
        search = input(("Enter a pattern:\n> "))
        search_proxy = r'' + search
        print("Listed logs:")
        for entry in self.entries:
            if (re.search(search_proxy, entry['Task Name']) or
                re.search(search_proxy, entry[' Notes Information'])):
                Search().show(entry)
        input('ENTER to redirect to MENU. ')
