if __name__=="__main__":
    paintCost = 1.00   #Per square foot
    overallCost = 0.0
    noOfWalls = int(input("How many surfaces are there? Please include all of the walls and the ceiling if applicable. "))
    walls = []

    #Asking for wall measurements and adding to list
    for i in range(0, noOfWalls):
        print("\nSurface " + str(i + 1))
        incorrectInput = True
        while incorrectInput:
            shape = input("Is this surface a square, rectangle or triangle?" )
            if shape.lower() == "square" or shape.lower() == "rectangle" or shape.lower() == "triangle":
                incorrectInput = False
        height = int(input("What is the height of this wall in feet? "))
        width = int(input("What is the width of this wall in feet?" ))
        walls.append([height, width, shape])

    for wall in walls:
        if wall[2].lower() == "square" or wall[2].lower() == "rectangle":
            area = wall[0] * wall[1]
        else:
            area = (wall[0] * wall[2]) / 2
        overallCost += (paintCost * area)

    print("\nYour overall cost of paint for this room is " + str(overallCost))


    #paint calculator
    #python program
    #calculate how much paint and cost of paint come up with paint cost
    #to renovate a given room
    #no of walls
    #areas of walls
    #shapes of walls
    #ceiling
    #doors
    #radiators