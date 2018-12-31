from __future__ import print_function

import logging
logging.basicConfig(filename = 'logged_tic.log', level = logging.INFO, 
	format = '%(created)f:%(levelname)s:%(message)s')



choices = []

for x in range (0, 9) :
    choices.append(str(x+1))
    
playerOneTurn = True
winner = False


def printBoard() :
    print( '   =================')
    print( '   || ' + choices[0] + ' || ' + choices[1] + ' || ' + choices[2] + ' || ')
    print( '   =================')
    print( '   || ' + choices[3] + ' || ' + choices[4] + ' || ' + choices[5] + ' || ')
    print( '   =================')
    print( '   || ' + choices[6] + ' || ' + choices[7] + ' || ' + choices[8] + ' || ')
    print( '   =================\n')
    
while not winner :
    printBoard()

    if playerOneTurn :
        print( "   tamashobs <  X  > \n")
    else :
        print( "   tamashobs <  O  > \n")

    try:
        choice = int(input(">> "))
    except:
        print("mocemuli simbolo arasworad aris akrebili scadet tavidan")
        continue
    if choices[choice - 1] == 'X' or choices [choice-1] == 'O':
        print("archeuli ujra dakavebulia !! ")
        continue

    if playerOneTurn :
        choices[choice - 1] = 'X'
    else :
        choices[choice - 1] = 'O'

    playerOneTurn = not playerOneTurn
    def Mult(x):
        return x * 3
    for x in range (0, 3) :
        y=Mult(x)

        logging.warning('Y: {}'.format(y))
        
        if (choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]) :
            winner = True
            printBoard()
        if (choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]) :
            winner = True
            printBoard()

    if((choices[0] == choices[4] and choices[0] == choices[8]) or 
       (choices[2] == choices[4] and choices[4] == choices[6])) :
        winner = True
        printBoard()
    
if(playerOneTurn==0):
    print("mogebulia < X >")
else:
    print("mogebulia < O >")

