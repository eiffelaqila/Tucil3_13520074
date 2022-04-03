# CLASS MATRIX
class Matrix:
    # ***** ATRIBUT ***** #
    # rowSize: integer
    # colSize: integer
    # matrix: array of array of integers
    # emptySpaceX: integer -> lokasi baris empty space
    # emptySpaceY: integer -> lokasi kolom empty space
    # countMove: integer -> menunjukan banyak langkah yang telah dilakukan (f(P))
    # previousMove: string
    # cost: int
    
    # ***** METHOD ***** #
    # *** CONSTRUCTOR *** #
    def __init__(self):
        self.rowSize = 4
        self.colSize = 4
        self.matrix = [[0 for i in range(self.rowSize)] for j in range(self.colSize)]
        self.emptySpaceX = 0
        self.emptySpaceY = 0
        self.countMove = 0
        self.previousMove = None
        self.previousMatrix = None
        self.cost = 0
    
    def __lt__(self, other):
        return self.cost < other.cost

    # *** GETTER AND SETTER *** #
    # GET ELMT
    def getElmt(self, i, j):
        return self.matrix[i][j]
    
    # SET ELMT
    def setElmt(self, i, j, value):
        self.matrix[i][j] = value
    
    # GET EMPTYSPACE (X dan Y)
    def getEmptySpaceX(self):
        return self.emptySpaceX

    def getEmptySpaceY(self):
        return self.emptySpaceY

    # SET EMPTYSPACE (X dan Y)
    def setEmptySpaceX(self, i):
        self.emptySpaceX = i

    def setEmptySpaceY(self, j):
        self.emptySpaceY = j
    
    # GET COUNT MOVE
    def getCountMove(self):
        return self.countMove
    
    # SET COUNT MOVE
    def setCountMove(self, value):
        self.countMove = value

    # GET PREVIOUS MOVE
    def getPreviousMove(self):
        return self.previousMove
    
    # SET PREVIOUS MOVE
    def setPreviousMove(self, value):
        self.previousMove = value
    
    # GET PREVIOUS MATRIX
    def getPreviousMatrix(self):
        return self.previousMatrix
    
    # SET PREVIOUS MATRIX
    def setPreviousMatrix(self, value):
        self.previousMatrix = value
    
    # GET PREVIOUS MATRIX
    def getCost(self):
        return self.cost
    
    # SET PREVIOUS MATRIX
    def setCost(self, value):
        self.cost = value
    
    # PENGGESER EMPTY SPACE
    # GESER ATAS
    def atas(self):
        # Search empty space
        emptyX = self.getEmptySpaceX()
        emptyY = self.getEmptySpaceY()

        # Geser empty space ke atas
        if (emptyX != 0):
            # Increment Count Move
            self.setCountMove(self.getCountMove()+1)
            # Set previousMove
            self.setPreviousMove("U")
            # Swap elemen
            elmt = self.getElmt(emptyX, emptyY)
            elmtAtas = self.getElmt(emptyX-1, emptyY)
            self.setElmt(emptyX, emptyY, elmtAtas)
            self.setElmt(emptyX-1, emptyY, elmt)
            self.setEmptySpaceX(emptyX-1)
    
    # GESER BAWAH
    def bawah(self):
        # Search empty space
        emptyX = self.getEmptySpaceX()
        emptyY = self.getEmptySpaceY()

        # Geser empty space ke bawah
        if (emptyX != 3):
            # Increment Count Move
            self.setCountMove(self.getCountMove()+1)
            # Set previousMove
            self.setPreviousMove("D")
            # Swap elemen
            elmt = self.getElmt(emptyX, emptyY)
            elmtBawah = self.getElmt(emptyX+1, emptyY)
            self.setElmt(emptyX, emptyY, elmtBawah)
            self.setElmt(emptyX+1, emptyY, elmt)
            self.setEmptySpaceX(emptyX+1)
    
    # GESER KANAN
    def kanan(self):
        # Search empty space
        emptyX = self.getEmptySpaceX()
        emptyY = self.getEmptySpaceY()

        # Geser empty space ke kanan
        if (emptyY != 3):
            # Increment Count Move
            self.setCountMove(self.getCountMove()+1)
            # Set previousMove
            self.setPreviousMove("R")
            # Swap elemen
            elmt = self.getElmt(emptyX, emptyY)
            elmtKanan = self.getElmt(emptyX, emptyY+1)
            self.setElmt(emptyX, emptyY, elmtKanan)
            self.setElmt(emptyX, emptyY+1, elmt)
            self.setEmptySpaceY(emptyY+1)

    # GESER KIRI
    def kiri(self):
        # Search empty space
        emptyX = self.getEmptySpaceX()
        emptyY = self.getEmptySpaceY()

        # Geser empty space ke kiri
        if (emptyY != 0):
            # Increment Count Move
            self.setCountMove(self.getCountMove()+1)
            # Set previousMove
            self.setPreviousMove("L")
            # Swap elemen
            elmt = self.getElmt(emptyX, emptyY)
            elmtKiri = self.getElmt(emptyX, emptyY-1)
            self.setElmt(emptyX, emptyY, elmtKiri)
            self.setElmt(emptyX, emptyY-1, elmt)
            self.setEmptySpaceY(emptyY-1)
    
    # PRINT MATRIX
    def printMatrix(self):
        print("|=======================================|")
        for i in range(self.rowSize):
            print("|", end='\t')
            for j in range(self.colSize):
                elmt = self.getElmt(i, j)
                if (elmt == 16):
                    print(" ", end='\t')
                else:
                    print(elmt, end='\t')
            print("|")
        print("|=======================================|")