def overallArea(height, width, triangle):
    if triangle:
        area = (height * width) / 2
    else:
        area = height * width
    return area



if __name__=="__main__":
    paintCost = 1.00   #Per square foot
    overallCost = 0.0

    #Asking for amount of surfaces
    noOfSurfaces = int(input("How many surfaces are there? Please include all of the walls and the ceiling if applicable. "))
    surfaces = []
    noOfExtras = int(input("How many surfaces do you not want painted? "))
    extras = []



    #Asking for surface measurements and adding to list
    for i in range(0, noOfSurfaces):
        print("\nSurface " + str(i + 1))
        incorrectInput = True
        while incorrectInput:
            shape = input("Is this surface a square (s), rectangle (r) or triangle (t)? ")
            if shape.lower() == "square" or shape.lower() == "rectangle" or shape.lower() == "triangle" or shape.lower() == "s" or shape.lower() == "r" or shape.lower() == "t":
                incorrectInput = False
            else:
                print("Please answer with one of the 3 shapes above.")
        height = int(input("What is the height of this surface in feet? "))
        width = int(input("What is the width of this surface in feet?" ))
        surfaces.append([height, width, shape])

    for surface in surfaces:
        if surface[2].lower() == "square" or surface[2].lower() == "rectangle" or surface[2].lower() == "s" or surface[2].lower() == "r":
            area = overallArea(surface[0], surface[1], False)
        else:
            area = overallArea(surface[0], surface[1], True)
        overallCost += (paintCost * area)

    #Asking for non-painted surfaces
    for i in range(0, noOfExtras):
        print("\nNon painted surface " + str(i + 1))
        height = int(input("What is the height of this non painted surface in feet? "))
        width = int(input("What is the width of this non painted surface in feet?" ))
        extras.append([height, width])

    for extra in extras:
        area = overallArea(extra[0], extra[1], False)
        overallCost -= (paintCost * area)

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