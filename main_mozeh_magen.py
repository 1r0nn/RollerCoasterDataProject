# ITP 115, Spring 2023
# Final Project
# Name: Magen Mozeh
# Email: mozeh@usc.edu
# Section: Koster
# Filename: filename.py (update accordingly)
# Description: roller coaster final project

import helper  # import the helper module
import user_io  # import the user_io module
import extra_credit  # import the extra_credit module

def main():
    print("Roller Coasters from around the world")
    coastersList = helper.makeCoastersList("roller_coasters.csv")  # create a list of coaster dictionaries from the CSV file
    optionsDict = makeOptionsDict()  # create a dictionary of options that the user can select

    while True:
        user_io.displayDict(optionsDict)  # display the available options to the user
        userChoice = user_io.getUserOption(optionsDict)  # get the user's choice

        if userChoice.upper() == "Q":
            break
        elif userChoice.upper() == "A":
            user_io.makeParksFile(coastersList)  # create a parks file from the coaster list
        elif userChoice.upper() == "B":
            user_io.displayNumCoasters(coastersList)  # display the number of coasters
        elif userChoice.upper() == "C":
            user_io.displayNumWoodenCoasters(coastersList)  # display the number of wooden coasters
        elif userChoice.upper() == "D":
            user_io.displayLoopiestCoaster(coastersList)  # display the loopiest coaster
        elif userChoice.upper() == "E":
            user_io.displayTallestCoaster(coastersList)  # display the tallest coaster
        elif userChoice.upper() == "F":
            user_io.findCoasters(coastersList)  # find coasters based on user input
        elif userChoice.upper() == "G":
            extra_credit.displaySeatingTypes(coastersList)  # display unique seating types in alphabetical order
        elif userChoice.upper() == "H":
            extra_credit.displayNumCoastersBySeating(coastersList)  # display the number of coasters for each seating type
        print("")

def makeOptionsDict():
    options = {"A":"Amusement Parks","B":"Number of coasters","C":"Number of wooden coasters",
               "D":"Loopiest coaster","E":"Tallest coaster","F":"Find coasters",
               "G":"Seating types","H":"Number","Q":"Quit"}  # define the available options
    return options

main()
