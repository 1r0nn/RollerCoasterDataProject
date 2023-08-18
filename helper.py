# ITP 115, Spring 2023
# Final Project
# Name: Magen Mozeh
# Email: mozeh@usc.edu
# Section: Koster
# Filename: filename.py (update accordingly)
# Description: roller coaster final project

# Creates a list of dictionaries for coasters from a CSV file
def makeCoastersList(filenameStr):
    coasters = []  # Initialize the coasters list
    with open(filenameStr, "r") as fileContents:
        header_line = fileContents.readline().strip("\n")  # Read the header line from the file
        keys = header_line.split(",")  # Split the header line into a list of keys

        # Loop through each line in the file
        for line in fileContents:
            line = line.strip("\n")  # Remove newline character
            values = line.split(",")  # Split the line into a list of values
            coaster_dict = {}  # Initialize an empty dictionary for the coaster

            # Create a dictionary for the coaster using the keys and values
            for i in range(len(keys)):
                coaster_dict[keys[i]] = values[i]

            # Add the coaster dictionary to the coasters list
            coasters.append(coaster_dict)

    # Return the list of coaster dictionaries
    return coasters


# Returns a sorted list of unique park names from the coasters list
def getUniqueParkNames(coastersList):
    parkNames = []  # Initialize an empty list for park names

    # Loop through each coaster in the coasters list
    for coaster in coastersList:
        parkExist = coaster.get("park")  # Get the value at the 'park' key

        # Add the park name to the list if it's not already there
        if parkExist not in parkNames:
            parkNames.append(parkExist)

    # Sort the list of park names
    parkNames.sort()

    # Return the sorted list of unique park names
    return parkNames


# Returns the coaster with the most loops from the coasters list
def getLoopiestCoaster(coastersList):
    biggestLoops = 0  # Initialize a variable to store the highest number of loops

    # Loop through each coaster in the coasters list
    for coaster in coastersList:
        loopiestCoaster = coaster["num_inversions"]  # Get the number of inversions for the coaster

        # Check if the number of inversions is a digit
        if loopiestCoaster.isdigit():
            loopiestOfAll = int(loopiestCoaster)  # Convert the number of inversions to an integer

            # Update the highest number of loops and the loopiest coaster if needed
            if loopiestOfAll > biggestLoops:
                biggestLoops = loopiestOfAll
                loopiestHere = coaster

    # Return the coaster with the most loops
    return loopiestHere


# Returns the tallest coaster from the coasters list
def getTallestCoaster(coastersList):
    tallestHeight = 0  # Initialize a variable to store the tallest height

    # Loop through each coaster in the coasters list
    for coaster in coastersList:
        coasterHeight = coaster["height"]  # Get the height of the coaster

        # Check if the height is a digit
        if coasterHeight.isdigit():
            height = int(coasterHeight)  # Convert the height to an integer

            # Update the tallest height and the tallest coaster if needed
            if height > tallestHeight:
                tallestHeight = height
                tallestCoaster = coaster
    # Return the tallest coaster
    return tallestCoaster












