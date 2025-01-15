def overallArea(height, width, triangle):
    if triangle:
        area = (height * width) / 2
    else:
        area = height * width
    return area

def measurementCheck():
    while True:
        height = int(input("What is the height of this surface in feet? "))
        if height < 1:
            print("A surface can't be less than 1 foot in height")
        else:
            break

    while True:
        width = int(input("What is the width of this surface in feet?" ))
        if width < 1:
            print("A surface can't be less than 1 foot in width")
        else:
            break

    return height, width

def surfacesCheck(inputStr):
    while True:
        noOfSurfaces = int(input(inputStr))
        if noOfSurfaces < 1:
            print("There can't be less than one surface")
        else:
            break

    return noOfSurfaces


if __name__=="__main__":
    whiteCost = 1.00   #Per square foot
    yellowCost = 1.10
    blueCost = 1.20
    overallCost = 0.0

    #Asking for amount of surfaces
    while True:
        colour = input("What colour paint would you like? We have white (w), yellow (y) and blue (b) ")
        match colour:
            case "white" | "w":
                chosenCost = whiteCost
                break
            case "yellow" | "y":
                chosenCost = yellowCost
                break
            case "blue" | "b":
                chosenCost = blueCost
                break
            case _:
                print("That is not one of the colours that we have")
                continue


    surfacesStr = "How many surfaces are there? Please include all of the walls and the ceiling if applicable "
    noOfSurfaces = surfacesCheck(surfacesStr)
    surfaces = []

    extrasStr = "How many surfaces do you not want painted? "
    noOfExtras = surfacesCheck(extrasStr)
    extras = []



    #Asking for surface measurements and adding to list
    for i in range(0, noOfSurfaces):
        print("\nSurface " + str(i + 1))
        while True:
            shape = input("Is this surface a square (s), rectangle (r) or triangle (t)? ")
            if (shape.lower() == "square") | (shape.lower() == "rectangle") | (shape.lower() == "triangle") | (shape.lower() == "s") | (shape.lower() == "r") | (shape.lower() == "t"):
                break
            else:
                print("Please answer with one of the 3 shapes above")
        height, width = measurementCheck()
        surfaces.append([height, width, shape])


    for surface in surfaces:
        if surface[2].lower() == "triangle" or surface[2].lower() == "t":
            area = overallArea(surface[0], surface[1], True)
        else:
            area = overallArea(surface[0], surface[1], False)
        overallCost += (chosenCost * area)




    #Asking for non-painted surfaces
    for i in range(0, noOfExtras):
        print("\nNon painted surface " + str(i + 1))
        height, width = measurementCheck()
        extras.append([height, width])

    for extra in extras:
        area = overallArea(extra[0], extra[1], False)
        overallCost -= (chosenCost * area)

    print("\nYour overall cost of paint for this room is " + str(overallCost))


    #paint calculator
    #python program
    #calculate how much paint and cost of paint come up with paint cost
    #to renovate a given room
    #no of surfaces
    #areas of surfaces
    #shapes of surfaces
    #ceiling
    #doors
    #radiators