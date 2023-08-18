# ITP 115, Spring 2023
# Final Project
# Name: Magen Mozeh
# Email: mozeh@usc.edu
# Section: Koster
# Filename: filename.py (update accordingly)
# Description: roller coaster final project

import helper


# Display the content of a dictionary in alphabetical order by key
def displayDict(optionsDict):
    # Sort the keys of the dictionary
    keysSorted = sorted(optionsDict.keys())

    # Print each key-value pair in the sorted order
    for key in keysSorted:
        print(key, "->", optionsDict[key])


# Get user input, validate it against the keys of optionsDict, and return the valid input
def getUserOption(optionsDict):
    # Get user input, strip whitespace, and convert to uppercase
    userInput = input("Option: ").strip().upper()

    # Validate user input against dictionary keys
    while userInput not in optionsDict.keys():
        userInput = input("Option: ").strip().upper()
    else:
        return userInput


# Display the total number of coasters in the coastersList
def displayNumCoasters(coastersList):
    numCoasters = len(coastersList)
    print("The total number of coasters is", str(numCoasters))


# Display the total number of wooden coasters in the coastersList
def displayNumWoodenCoasters(coastersList):
    woodenCount = 0
    # Iterate through coasters and count the wooden ones
    for coaster in coastersList:
        if coaster["material_type"] == "Wooden":
            woodenCount += 1
    print("The total number of wooden coasters is", str(woodenCount))


# Display detailed information about a single coaster (coasterDict)
def displayCoaster(coasterDict):
    # Print coaster name and park
    print(coasterDict["name"], "[" + coasterDict["park"] + "]")
    # Print coaster speed if available
    if coasterDict["speed"] != "":
        print("\tSpeed =", coasterDict["speed"], "mph")
    # Print coaster height if available
    if coasterDict["height"] != "":
        print("\tHeight =", coasterDict["height"], "ft")
    # Print coaster length if available
    if coasterDict["length"] != "":
        print("\tLength =", coasterDict["length"], "ft")
    # Print number of loops if available and greater than 0
    if coasterDict["num_inversions"] != "" and int(coasterDict["num_inversions"]) > 0:
        print("\tLoops =", coasterDict["num_inversions"])
    # Print coaster status
    print("\tStatus is", coasterDict["status"])


# Display information about the coaster with the most loops
def displayLoopiestCoaster(coastersList):
    loopiestCoaster = helper.getLoopiestCoaster(coastersList)
    displayCoaster(loopiestCoaster)


# Display information about the tallest coaster
def displayTallestCoaster(coastersList):
    tallestCoaster = helper.getTallestCoaster(coastersList)
    displayCoaster(tallestCoaster)


# Create a text file containing amusement park names sorted alphabetically
def makeParksFile(coastersList):
    parkNames = helper.getUniqueParkNames(coastersList)
    numParks = len(parkNames)

    # Create and open a file for writing
    amusementFile = open("amusement_parks.txt", "w")

    amusementFile.write("Amusement parks in alphabetical order:\n")
    # Write park names to the file
    for park in parkNames:
        amusementFile.write(park + "\n")

    print("There are", numParks, "unique parks.")
    print("The park names were saved to amusement_parks.txt")

    # Close the file
    amusementFile.close()


# Search for coasters by a user-provided search phrase
def findCoasters(coastersList):
    # Initialize a counter for the number of coasters found
    numCoasters = 0

    # Get the user's search phrase, remove any leading/trailing whitespace, and convert it to lowercase
    searchPhrase = input("Enter a search phrase: ").strip().lower()

    # Loop through each coaster in the coastersList
    for coaster in coastersList:
        # Check if the search phrase is present in the coaster's name or park (case-insensitive)
        if searchPhrase in coaster["name"].lower() or searchPhrase in coaster["park"].lower():
            # Display detailed information about the coaster if the search phrase is found
            displayCoaster(coaster)
            # Increment the counter for the number of coasters found
            numCoasters += 1

    # If any coasters were found, print the total number and the search phrase
    if numCoasters > 0:
        print("Found", numCoasters, "coasters that contain", "'" + searchPhrase + "'")
    # If no coasters were found, print a message indicating the search phrase was not found
    else:
        print("No coasters contain", "'" + searchPhrase + "'")

