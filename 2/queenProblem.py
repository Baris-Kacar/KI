import chess
import chess.svg
from chessboard import display
from chess import Move
import time
import random
import math

board = chess.Board("8/8/8/8/8/8/8/8 w - - 0 1")

# Erste Königing setzen
"""board.set_piece_at(16,chess.Piece(chess.QUEEN,chess.WHITE))
board.set_piece_at(9,chess.Piece(chess.QUEEN,chess.WHITE))
board.set_piece_at(34,chess.Piece(chess.QUEEN,chess.WHITE))
board.set_piece_at(27,chess.Piece(chess.QUEEN,chess.WHITE))
board.set_piece_at(20,chess.Piece(chess.QUEEN,chess.WHITE))
board.set_piece_at(13,chess.Piece(chess.QUEEN,chess.WHITE))
board.set_piece_at(6,chess.Piece(chess.QUEEN,chess.WHITE))
board.set_piece_at(23,chess.Piece(chess.QUEEN,chess.WHITE))"""

"""board.set_piece_at(16,chess.Piece(chess.QUEEN,chess.WHITE))
board.set_piece_at(9,chess.Piece(chess.QUEEN,chess.WHITE))
board.set_piece_at(50,chess.Piece(chess.QUEEN,chess.WHITE))
board.set_piece_at(35,chess.Piece(chess.QUEEN,chess.WHITE))
board.set_piece_at(12,chess.Piece(chess.QUEEN,chess.WHITE))
board.set_piece_at(29,chess.Piece(chess.QUEEN,chess.WHITE))
board.set_piece_at(6,chess.Piece(chess.QUEEN,chess.WHITE))
board.set_piece_at(7,chess.Piece(chess.QUEEN,chess.WHITE))"""

"""board.set_piece_at(8,chess.Piece(chess.QUEEN,chess.WHITE))
board.set_piece_at(25,chess.Piece(chess.QUEEN,chess.WHITE))
board.set_piece_at(50,chess.Piece(chess.QUEEN,chess.WHITE))
board.set_piece_at(27,chess.Piece(chess.QUEEN,chess.WHITE))
board.set_piece_at(60,chess.Piece(chess.QUEEN,chess.WHITE))
board.set_piece_at(37,chess.Piece(chess.QUEEN,chess.WHITE))
board.set_piece_at(38,chess.Piece(chess.QUEEN,chess.WHITE))
board.set_piece_at(15,chess.Piece(chess.QUEEN,chess.WHITE))"""

"""board.set_piece_at(8,chess.Piece(chess.QUEEN,chess.WHITE))
board.set_piece_at(25,chess.Piece(chess.QUEEN,chess.WHITE))
board.set_piece_at(26,chess.Piece(chess.QUEEN,chess.WHITE))
board.set_piece_at(3,chess.Piece(chess.QUEEN,chess.WHITE))
board.set_piece_at(5,chess.Piece(chess.QUEEN,chess.WHITE))
board.set_piece_at(14,chess.Piece(chess.QUEEN,chess.WHITE))
board.set_piece_at(31,chess.Piece(chess.QUEEN,chess.WHITE))
board.set_piece_at(36,chess.Piece(chess.QUEEN,chess.WHITE))"""

def test(i):
    if i == 1:
        board.set_piece_at(16,chess.Piece(chess.QUEEN,chess.WHITE))
        board.set_piece_at(9,chess.Piece(chess.QUEEN,chess.WHITE))
        board.set_piece_at(34,chess.Piece(chess.QUEEN,chess.WHITE))
        board.set_piece_at(27,chess.Piece(chess.QUEEN,chess.WHITE))
        board.set_piece_at(20,chess.Piece(chess.QUEEN,chess.WHITE))
        board.set_piece_at(13,chess.Piece(chess.QUEEN,chess.WHITE))
        board.set_piece_at(6,chess.Piece(chess.QUEEN,chess.WHITE))
        board.set_piece_at(23,chess.Piece(chess.QUEEN,chess.WHITE))

    if i == 2:
        board.set_piece_at(16,chess.Piece(chess.QUEEN,chess.WHITE))
        board.set_piece_at(9,chess.Piece(chess.QUEEN,chess.WHITE))
        board.set_piece_at(50,chess.Piece(chess.QUEEN,chess.WHITE))
        board.set_piece_at(35,chess.Piece(chess.QUEEN,chess.WHITE))
        board.set_piece_at(12,chess.Piece(chess.QUEEN,chess.WHITE))
        board.set_piece_at(29,chess.Piece(chess.QUEEN,chess.WHITE))
        board.set_piece_at(6,chess.Piece(chess.QUEEN,chess.WHITE))
        board.set_piece_at(7,chess.Piece(chess.QUEEN,chess.WHITE))
    if i == 3:
        board.set_piece_at(8,chess.Piece(chess.QUEEN,chess.WHITE))
        board.set_piece_at(25,chess.Piece(chess.QUEEN,chess.WHITE))
        board.set_piece_at(50,chess.Piece(chess.QUEEN,chess.WHITE))
        board.set_piece_at(27,chess.Piece(chess.QUEEN,chess.WHITE))
        board.set_piece_at(60,chess.Piece(chess.QUEEN,chess.WHITE))
        board.set_piece_at(37,chess.Piece(chess.QUEEN,chess.WHITE))
        board.set_piece_at(38,chess.Piece(chess.QUEEN,chess.WHITE))
        board.set_piece_at(15,chess.Piece(chess.QUEEN,chess.WHITE))
    if i == 4:
        board.set_piece_at(8,chess.Piece(chess.QUEEN,chess.WHITE))
        board.set_piece_at(25,chess.Piece(chess.QUEEN,chess.WHITE))
        board.set_piece_at(26,chess.Piece(chess.QUEEN,chess.WHITE))
        board.set_piece_at(3,chess.Piece(chess.QUEEN,chess.WHITE))
        board.set_piece_at(5,chess.Piece(chess.QUEEN,chess.WHITE))
        board.set_piece_at(14,chess.Piece(chess.QUEEN,chess.WHITE))
        board.set_piece_at(31,chess.Piece(chess.QUEEN,chess.WHITE))
        board.set_piece_at(36,chess.Piece(chess.QUEEN,chess.WHITE))
    

#schauen wo meine damen sind
#print(board.piece_map().keys())
"""
alle damen felder
for square in chess.SQUARES:
    piece = board.piece_at(square)
    if piece is not None:
        # Den Feldnamen der Figur ausgeben
        print(chess.square_name(square))
"""

#
#print(board.piece_at(7))
#print(ord('a'))
#print(chr(97))
#print(chess.square_rank(16))

class Queen:
    notPossibleMoves = []
    transModel = []
    initialState = None
    arrVisited = []
    totalFitness = 0
    populationsArr = []
    
    #genetic algorithm
    population = []

    def __init__(self, initialState = None, transModel = None):
        if initialState is None:
            self.initialState = [0,0,0,0,0,0,0,0]

        if transModel is None:
            for i in range(0,64):
                if i not in self.notPossibleMoves and i not in self.transModel:
                    self.transModel.append(i)
    
    def checkNotInArray(self, i):
        if i not in self.notPossibleMoves:
            self.notPossibleMoves.append(i)
    
    def possibleMoves(self):
        self.notPossibleMoves = []
        for i in range(0, 64):
            if board.piece_at(i) != None:
                self.checkRowQueen(i,True)
                self.checkColumnQueen(i,True)
                self.checkDiagonalQueen(i,True)
        
        return self.notPossibleMoves
   
    def actions(self, state):
        # aktion um den zustand zu ändern
        # Figur bewegen
        #move = Move.from_uci(state)
        #board.push(move)
        board.set_piece_at(state,chess.Piece(chess.QUEEN,chess.WHITE))
    
    def checkRowQueen(self, state,justNotPossibleMoves = False):
        # überprüft wie viele threads in der zeile sind
        # mit Parameterwert True werden mit der Methode checkNotInFunction in das Array notPossibleMoves alle werte geschrieben die nicht mehr möglich sind
        counter = 0
        rowNumber = chess.square_rank(state) 
        
        rowBeginning = (rowNumber * 8)
        rowEnd = (((rowNumber + 1) * 8) -1)

        
        
        #print("rowNumber: " + str(rowNumber))
        #print("rowBeginning: " + str(rowBeginning))
        #print("rowEnd: " + str(rowEnd))

        #ZEILE ÜBERPRÜFEN
        test = False
        for cnt in range(rowBeginning , rowEnd + 1):
            
            if board.piece_at(cnt) != None :
                
                    test = True
                    counter = counter + 1 
                    #print("Row Collision mit: " + str(cnt) + " = COUNTER:  " + str(counter))
            if justNotPossibleMoves == True:
                #print(justNotPossibleMoves)
                self.checkNotInArray(cnt)
        
    

        if test == True:
            return counter -1
        else:
            return 0
    
    def checkColumnQueen(self, state, justNotPossibleMoves = False):
        # überprüft wie viele threads in der spalte sind
        # mit Parameterwert True werden mit der Methode checkNotInFunction in das Array notPossibleMoves alle werte geschrieben die nicht mehr möglich sind
        columnBegin = state
        columnEnd = state
        counter = 0
        while columnBegin > 0:
            if (columnBegin - 8) >= 0:
                columnBegin = columnBegin-8
            if columnBegin >= 0 and columnBegin <= 7:
                break

        while columnEnd <= 63:
            if (columnEnd + 8 ) <= 63:
                columnEnd = columnEnd + 8
            if columnEnd >= 56 and columnEnd <= 63:
                break
        
        test = False
        
        for cnt in range(columnBegin , columnEnd + 1, 8):
                if board.piece_at(cnt) != None:
                    test = True
                    counter = counter + 1
                    #print("counter : " + str(counter))
                    self.arrVisited.append(cnt)
                    #print(self.arrVisited)
                    #print("Column Collision mit: " + str(cnt) + " = COUNTER:  " + str(counter))
                if justNotPossibleMoves == True:
                    self.checkNotInArray(cnt)
        #print("BEFORE RETURN COUNTER: " + str(counter))

        if test == True:
            #print("RETURN COUNTER: " + str(counter))
            return counter - 1
        else:
            return 0
    
    def LBU(self, state, justNotPossibleMoves = False):
        counter = 0
        yBorderLeft = []
        yBorderRight = []
        xBorderUnder = []
        xBorderAbove = []


        leftBeginUnder = state
        rightEndAbove = state
      

        for cnt in range(0,57,8):
            yBorderLeft.append(cnt)
        for cnt in range(7,64,8):
            yBorderRight.append(cnt)
        for cnt in range(0,8,1):
            xBorderUnder.append(cnt)
        for cnt in range(56,64,1):
            xBorderAbove.append(cnt)
        
        
        if leftBeginUnder not in yBorderLeft:
            while leftBeginUnder not in yBorderLeft:
                if ((leftBeginUnder - 8) - 1) < 0:
                    break
                leftBeginUnder = (leftBeginUnder - 8) - 1
        
        if rightEndAbove not in yBorderRight:
            while rightEndAbove not in yBorderRight:
                if ((rightEndAbove +8) +1) > 63:
                    break
                rightEndAbove = (rightEndAbove + 8) + 1
        
        checkFirst = False
        #schaut diagonal von unten links nach oben rechts ob eine dame gesetzt ist
        if justNotPossibleMoves == True:
                self.checkNotInArray(leftBeginUnder)

        #print("LeftBeginUnder: " + str(leftBeginUnder))
        #print("rightEndAbove: " + str(rightEndAbove))
        #print()

        while (leftBeginUnder + 1) + 8 < rightEndAbove + 1:
            
            if board.piece_at(leftBeginUnder) is not None:
                checkFirst = True
                counter = counter + 1
                #print("LBU: " + str(leftBeginUnder) + " :::: " + str(counter) )
            leftBeginUnder = (leftBeginUnder + 8) +1

            if justNotPossibleMoves == True:
                self.checkNotInArray(leftBeginUnder)
        
        #print("KOLLISION MIT DIAGONAL: " + str(leftBeginUnder) + " -" + str(counter))

        if checkFirst == True:
            counter = counter - 1
        return counter
    
    def LBA(self, state, justNotPossibleMoves = False):
             # überprüft wie viele threads in der diagonale sind
        # mit Parameterwert True werden mit der Methode checkNotInFunction in das Array notPossibleMoves alle werte geschrieben die nicht mehr möglich sind
        counter = 0
        yBorderLeft = []
        yBorderRight = []
        xBorderUnder = []
        xBorderAbove = []


        leftBeginUnder = state
        rightEndAbove = state
        leftBeginAbove = state 
        rightEndUnder = state

        for cnt in range(0,57,8):
            yBorderLeft.append(cnt)
        for cnt in range(7,64,8):
            yBorderRight.append(cnt)
        for cnt in range(0,8,1):
            xBorderUnder.append(cnt)
        for cnt in range(56,64,1):
            xBorderAbove.append(cnt)
        
        
        if leftBeginAbove not in yBorderLeft:
            while leftBeginAbove not in yBorderLeft:
                if ((leftBeginAbove + 8) - 1) > 63:
                    break
                leftBeginAbove = (leftBeginAbove + 8 ) - 1

        if rightEndUnder not in yBorderRight:
                while rightEndUnder not in yBorderRight:
                    if ((rightEndUnder - 8) +1) < 0:
                        break
                    rightEndUnder = (rightEndUnder - 8) + 1
        
        checkSecond = False
        #print("LeftBeginAbove: " + str(leftBeginAbove))
        #print("rightEndAbove: " + str(rightEndUnder))
        # print()
        # schaut diagonal von oben links nach unten rechts ob eine dame gesetzt ist
        if justNotPossibleMoves == True:
                self.checkNotInArray(leftBeginAbove)

        test = False
        while (leftBeginAbove - 8 ) + 1 >= rightEndAbove :
            if board.piece_at(leftBeginAbove) is not None: 
                #print(leftBeginAbove)
                checkSecond = True
                counter = counter + 1
                
                #print("LBA: " + str(leftBeginAbove) + " :::: " + str(counter))
            
            #print(leftBeginUnder)
            
            
            #print("T: " + str(leftBeginAbove))
            if justNotPossibleMoves == True:
                self.checkNotInArray(leftBeginAbove)

            leftBeginAbove = (leftBeginAbove - 8) + 1
            
     
        if board.piece_at(leftBeginAbove) is not None: 
                #print(leftBeginAbove)
                
                checkSecond = True
                counter = counter+1
                #print("LBA: " + str(leftBeginAbove) + " :::: " + str(counter))

        #print("KOLLISION MIT DIAGONAL: " + str(leftBeginUnder) + " ::::: " + str(counter))
        
        if checkSecond == True:
            counter = counter - 1

        #print(self.notPossibleMoves)
        return counter


    def checkDiagonalQueen(self, state, justNotPossibleMoves = False):
        # überprüft wie viele threads in der diagonale sind
        # mit Parameterwert True werden mit der Methode checkNotInFunction in das Array notPossibleMoves alle werte geschrieben die nicht mehr möglich sind
   

        #leftbeginAbove#############################rightEndAbove
        #########################################################
        #########################################################
        #########################################################
        #########################################################
        #########################################################
        #########################################################
        #########################################################
        #########################################################
        #########################################################
        #leftBeginUnder#############################rightEndUnder

        c = self.LBA(state)
        d = self.LBU(state)

        #print(self.notPossibleMoves)
        return c + d
    
    def heuristic(self, state):
        # pairs of threatening queens 
        # state sollte ein integer sein!!!


        #board.piece_at(1) prüft ob sich das Feld belegt ist wenn nein dann None

        #zeile in der sich die queen befindet
        rowThreadingCount = self.checkRowQueen(state)
        columnThreadingCount = self.checkColumnQueen(state)
        diagonalThreadUA = self.checkDiagonalQueen(state)
        
        #zähle die Threads zusammen
        
        counter = rowThreadingCount  + columnThreadingCount + diagonalThreadUA

        return counter
        #return rowThreadingCount
    
    def cost(self, state, action):
        # berechnet die kosten der aktion
        # previousCost sind die Kosten von der letzten platzierung der Dame und expectedCost sind die Kosten
        # von der aktuellen position wenn ich die Dame auf das Feld setzen möchte. Wenn die Kosten höher sind 
        # als davor dann soll ein neues feld gesucht werden
        previousCost = self.heuristic(state)
        exceptedCost = self.heuristic(action)
        return previousCost + exceptedCost
    
    def boardASCII(self):
        #ASCII vom Board ausgeben
        print(board)
    
    def threadeningLBUCount(self):
            val = 64
            t = False
            counter = 0
            while t == False:
                if (val-8) >= 0:
                    val = val -8
                else:
                    val = val + 1
                #print(val)

                counter = counter + queen.LBU(val)
                #print("Bei " + str(val) + " wurden so viele Threadings entdeckt : " + str(cnt) )
                if val == 7:
                    t = True

            return counter
    def threadeningLBACount(self):
            val = 0
            t = False
            counter = 0
            while t == False:
                if (val + 1) < 8:
                    val = val + 1
                else:
                    val = val + 8
                #print(val)

                counter = counter + queen.LBA(val)
                #print("Bei " + str(val) + " wurden so viele Threadings entdeckt : " + str(cnt) )
                if val == 63:
                    t = True
                
            return counter
    
    def threadeningRowCount(self):
            counter = 0
            spalteX = []

            for i in range(0,64):
                if board.piece_at(i) != None:
                    if chess.square_rank(i) not in spalteX:
                        if queen.checkRowQueen(i) >= 1:
                            counter = queen.checkRowQueen(i) + counter
                    spalteX.append(chess.square_rank(i))
            return counter
    def threadeningColumnCount(self):
           counter = 0
           for i in range(0,8):
                #spalte 1 bis 7 geben um pro spalte zuschauen
                counter  = queen.checkColumnQueen(i) + counter
           return counter

    def countOfThreadeningQueens(self):
            
            counter = self.threadeningLBUCount() + self.threadeningRowCount() + self.threadeningLBACount() + self.threadeningColumnCount()

            return counter

    def fitnessFunctionPercentage(self, val):
        # val ist die anzahl der threatenings

        

        if self.totalFitness != 0:
            val = round((val / self.totalFitness) * 100, 2)

            return val

    def fitnessFunction(self, setTotalFitnessCalc = False):               
                fitness = self.threadeningLBUCount() + self.threadeningRowCount() + self.threadeningLBACount() + self.threadeningColumnCount()
                return 28 - (fitness)
    
    def setTotalFitnessCalc(self, fitness):
        # berechnet die gesamsumme der fitness
        #print(str(self.totalFitness) + " + (28 - " + str(fitness) + " )")
        #self.totalFitness = self.totalFitness + (28 -  fitness)
        fitnessVal = 0
        for i in self.populationsArr:
            fitnessVal = fitnessVal + int(i["fitness"])

        #print(fitnessVal)
        self.totalFitness = fitnessVal

    def is_valid_state(self, state):
            # Überprüfen, ob das gegebene state eine gültige Lösung für das 8-Damen-Problem ist
            n = len(state)
            if len(set(state)) != n:
                return False
            if len(set(i+state[i] for i in range(n))) != n:
                return False
            if len(set(i-state[i] for i in range(n))) != n:
                return False
            return True
    
    def generate_valid_state(self):
    # zufällige generierte states
        while True:
            state = random.sample(range(8), 8)
            if self.is_valid_state(state):
                return state

    
    def populations(self, k):
        randValArr = []
        for i in range(k):
            randValArr.append(self.generate_valid_state())
        return randValArr

    

    def printPopulations(self):
         for i in self.populationsArr:
              fitness = int(i["fitness"])
              fitnessPercentage = float(self.fitnessFunctionPercentage(fitness))
              i["fitnessPercentage"]  = fitnessPercentage
              print("\nPopulationnumber: " + str(i["populationNumber"]))
              print("Fitness: " + str(i["fitness"]))
              print("TotalFitness: "  + str(self.totalFitness))
              print("Fitnesspercentage: " + str(fitnessPercentage) + " % ")
    

    def printAndCheckBestOnBoard(self,popNewArr):
        fitness = 0
        populationNumber = 0
        sieg  = False
        for i in popNewArr:
            fitness = i["fitness"]
            if fitness == 28:
                populationNumber = int(i["populationNumber"])
                sieg = True
                break
        



        columnCounter = 0
        check = 0
        
        for i in popNewArr:
            queens = i["population"]
            if int(i["populationNumber"]) == populationNumber and sieg == True:
                for j in queens:
                    if columnCounter == 8:
                            columnCounter = 0
                            
                    board.set_piece_at((( 8 * j) + columnCounter),chess.Piece(chess.QUEEN,chess.WHITE))
                    
                    columnCounter = columnCounter + 1

                
        for i in popNewArr:
             if int(i["populationNumber"]) == populationNumber and sieg == True:
                print()
                print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
                print("Gewonnen hat: " +str(i["populationNumber"]))
                print("Population: " +str(i["population"]))
                print("Mit einer Fitness von: "+ str(i["fitness"]))
                print("Mit einer Fitness Percentage: " + str(i["fitnessPercentage"]))
                break

       
        print()

    def selection(self):
            popArr = self.populationsArr
            #print(self.populationsArr)
            popNewArr = []
            solutionArr = []
            for i in range(0, len(self.populationsArr)):
                rand = random.randrange(0,len(self.populationsArr))
                #print(rand)
                popNewArr.append(popArr[rand])
            

            #print(popNewArr)
            newRand = 0
            ungerade = False
            for i in range(0,len(popNewArr)):
                population1 = None
                population2 = None
                if (len(popNewArr) % 2) != 0 and i == len(popNewArr[len(popNewArr)-1]):
                    newRand = random.randrange(0,len(popNewArr))
                    ungerade = True

                if i == len(popNewArr) - 1 and ungerade == True:
                    
                    population1 = popNewArr[len(popNewArr)-1]["population"]
                    population2 = popNewArr[newRand]["population"]
                    #print("Pop1: " + str(population1))
                    #print("Pop2: " + str(population2))
                    #print("LAST: " + str( len(popNewArr)-1))
                    #print("NEWRAND: " + str(newRand))
                    arr = self.crossover(population1, population2)
            
                    popNewArr[len(popNewArr)-1]["population"] = arr[0]
                    popNewArr[newRand]["population"] = arr[1]

                    #print("AFTER CROSS " + str(popNewArr[len(popNewArr)-1]["population"]))
                    #print(popNewArr[newRand]["population"])
                else:
                    newRand = random.randrange(0,len(popNewArr))
                    newRand2 = newRand
                    while newRand == newRand2:
                        newRand2 = random.randrange(0,len(popNewArr))
                    population1 = popNewArr[newRand]["population"]
                    population2 = popNewArr[newRand2]["population"]

                    arr = self.crossover(population1,population2)

                    popNewArr[newRand]["population"] = arr[0]
                    popNewArr[newRand2]["population"] = arr[1]


                rand = random.randrange(0,len(popNewArr))
               
            popNewArr = self.mutation(popNewArr)
            self.printAndCheckBestOnBoard(popNewArr)

    def crossover(self, arr1, arr2):
        splitt = random.sample(range(1, 7), 1)
        tmpArr1 = []
        tmpArr2 = []
        for i in range(0,8):
            if i <= splitt[0]:
                #print(arr1)
                #print(arr2)
                #print("SPLITT: " + str(splitt))
                tmpArr1.append(arr1[i])
                tmpArr2.append(arr2[i])
            else:
                tmpArr1.append(arr2[i])
                tmpArr2.append(arr1[i])

        arr1 = tmpArr1
        arr2 = tmpArr2
         
        return [arr1, arr2]

    def mutation(self, arr):
        randomVal = random.randrange(8)
        rand = random.randrange(8)

        while randomVal == rand:
            rand = random.randrange(8)
        for i in arr:
            #print("BEFORE: " + str(i["population"]))
            newArr = i["population"]
            newArr[randomVal] = rand
            i["population"] = newArr
            #print("aFter: " + str(i["population"]))
        return arr

    def orderPopulationArray(self):
        # ordnet das assoziative array nach fitnessfunction größe 
        self.populationsArr.sort(key=lambda x: x["fitnessPercentage"], reverse=True)

    def setQueens(self, populationsAnzahl, Test = False):
         popuArr = self.populations( populationsAnzahl)
         arr = []
         counter = 0
         columnCounter = 0
         populationNumber = 0
         print(popuArr)
         for i in popuArr:
            new_arr = arr.copy()
            
            #print("Counter: " + str(counter))
            if Test == False:
                for j in i:
                    new_arr.append(j)
                    if columnCounter == 8:
                        columnCounter = 0
                        
                    #print("COLUMNCOUNTER: " + str(columnCounter) + " j: " + str(j))
                    
                    board.set_piece_at((( 8 * j) + columnCounter),chess.Piece(chess.QUEEN,chess.WHITE))
                    columnCounter = columnCounter + 1
                
                #print(arr)
                self.populationsArr.append({
                            "populationNumber" : populationNumber , 
                            "fitness" : self.fitnessFunction(),
                            "population" : new_arr,
                            "fitnessPercentage" : 0
                })
                #print(self.populationsArr)

                print("PopulationNumber: " + str(populationNumber))
                self.boardASCII()

                self.setTotalFitnessCalc(self.fitnessFunction())
                        #print(self.populationsArr)
                        #self.fitnessFunctionPercentage(populations)
                print()
                #print("HIER: "+ str(self.populationsArr))
                board.clear()

                counter = counter + 1  
                populationNumber = populationNumber +1

                queen.orderPopulationArray()         

            else:
                for i in range(1,5):
                    test(i)
                    self.boardASCII()
                
                    self.populationsArr.append({
                        "populationNumber" : populationNumber , 
                        "fitness" : self.fitnessFunction(),
                        "population" : arr,
                        "fitnessPercentage" : 0
                    })

                    self.setTotalFitnessCalc(self.fitnessFunction())
                    #print(self.populationsArr)
                    #self.fitnessFunctionPercentage(populations)
                    print()
                    
                    board.clear()

                    counter = counter + 1  
                    populationNumber = populationNumber +1
         
         #self.printPopulations()
         self.selection()

         #print(selected)
         #board.set_piece_at(8,chess.Piece(chess.QUEEN,chess.WHITE))

    def geneticAlgorithm(self):
        
        return 

    

queen = Queen()

#print("Fitness: " + str(queen.fitnessFunction()))
#print("Threadening: "  +str(queen.countOfThreadeningQueens()))
#print("TotalFitness: " + str(queen.totalFitness))
#print("TotalFitness: " + str(queen.populations(1)))


# test
#queen.setQueens(1, True)

queen.setQueens(100)

#arr1 = [3,2,7,5,2,4,1,1]
#arr2 = [2,4,7,4,8,5,5,2]
#print(queen.crossover(arr1,arr2))


#print("BEFORE: " + str(arr1))
#rint("AFTER:  " + str(queen.mutation(arr1)))



#queen.possibleMoves()
#print(queen.heuristic(17))
#print(queen.fitnessFunction())
#print(queen.geneticAlgorithm(100,100,1000))

# Fen ist eine Notation um die Posititon der Schachfiguren auf einem Schabrett darzustellen
valid_fen = board.fen()
game_board = display.start()

n = 0
while True:
    #valid_fen = board.fen()
    #n = (n + 8) 
    #board.set_piece_at(n,chess.Piece(chess.QUEEN,chess.WHITE))
    
    display.check_for_quit()
    display.update(valid_fen, game_board)
    time.sleep(0.5)
    
display.terminate()
