# ITP 115, Spring 2023
# Final Project
# Name: Magen Mozeh
# Email: mozeh@usc.edu
# Section: Koster
# Filename: filename.py (update accordingly)
# Description: roller coaster final project

import user_io

# Returns a sorted list of unique seating types from the coasters list
def getSeatingTypes(coastersList):
    seatingTypes = []  # Initialize an empty list for seating types

    # Loop through each coaster in the coasters list
    for coaster in coastersList:
        seating_type = coaster["seating_type"]  # Get the seating type of the coaster

        # Add the seating type to the list if it's not already there
        if seating_type not in seatingTypes:
            seatingTypes.append(seating_type)

    # Return the sorted list of unique seating types
    return sorted(seatingTypes)

# Displays the seating types for the coasters in the coasters list
def displaySeatingTypes(coastersList):
    seatingTypes = getSeatingTypes(coastersList)  # Get the list of unique seating types
    print("The seating types are")

    # Print each seating type
    for seatingType in seatingTypes:
        print("\t"+seatingType)

# Displays the number of coasters for each seating type in the coasters list
def displayNumCoastersBySeating(coastersList):
    seatingTypes = getSeatingTypes(coastersList)  # Get the list of unique seating types
    coastersBySeating = {}  # Initialize an empty dictionary to store the number of coasters per seating type

    # Loop through each seating type
    for seatingType in seatingTypes:
        count = 0  # Initialize a counter for the number of coasters with the current seating type

        # Loop through each coaster in the coasters list
        for coaster in coastersList:
            # Check if the coaster has the current seating type
            if coaster["seating_type"] == seatingType:
                count += 1  # Increment the counter if the coaster has the current seating type

        # Add the current seating type and the number of coasters with that seating type to the dictionary
        coastersBySeating[seatingType] = count

    # Display the dictionary using the user_io.displayDict() function
    user_io.displayDict(coastersBySeating)
