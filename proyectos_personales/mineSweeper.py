import random
import os

gameover = False


class cell:
    def __init__(self, isMine: bool, isUnCovered: bool):
        self.isMine = isMine
        self.isUnCovered = isUnCovered

    def unCover():
        isUnCovered = True
        if isMine:
            print("PERDISTE!")
            gameover = True


def getTable():
    # This function will return the lenght and high of the table we want
    while True:
        try:
            size = input( 'What\'s the size you want for this run? (You must enter a "AxB" value, for instance, "10x15"):\n    ' )
            high = int(size[: size.index("x")])
            length = int(size[size.index("x") + 1 :])
            return high, length
        except:
            print( f'The value "{size}" is not valid.\n' )


high, length = getTable()

ObjectsTable = []
for x in range(0, high):
    ObjectsTable.append([])
    for y in range(0, length):
        TrueOrFalse = random.randint(0, 1) == 1
        newCell = cell(TrueOrFalse, False)
        ObjectsTable[x].append( newCell )

UiTable = [ [ str(table.index(cell)+1).rjust(2)+","+ str(ObjectsTable.index(table)+1).ljust(2)+ "[ ]" for cell in ObjectsTable[ObjectsTable.index(table)] ] for table in ObjectsTable ]

for table in UiTable:
    print(table)
def OneOrTwo():
    while True:
        choose = input("\n  What do you want to do? (Uncover: 1, red flag: 2): ")
        if choose == "1" or choose == "2":
            return choose
        print('INVALID INPUT. You must enter "1" or "2"')

    
def choosing(uncoverOrFlag: str):
    if uncoverOrFlag=="1":
        while True:
            coordenades = input('\nEnter the cell you want to uncover (format: "x,y". EXAMPLE: 10,12) put "GB" if you want to go back\n    ')
            if coordenades == "GB":
                return None
            elif coordenades[: coordenades.index(",")].isdigit() and coordenades[coordenades.index(",")+1 :].isdigit():
                x = int( coordenades[: coordenades.index(",")] )
                y = int( coordenades[coordenades.index(",")+1 :] )
                ObjectsTable[x][y].isUnCovered = True

                return "hola"
election = choosing(OneOrTwo())
while election == None:
    election = choosing(OneOrTwo())

for rowY in ObjectsTable:
    for cell in rowY:
        if cell.isUnCovered == True:
            print("y: ", ObjectsTable.index(rowY))
            print("x: ", rowY.index(cell))
            UiTable[ObjectsTable.index(rowY)][rowY.index(cell)]= "Hhh"

for rowY in UiTable:
    print(rowY)
# os.system('cls' if os.name == 'nt' else 'clear') #Esto limpia la terminal