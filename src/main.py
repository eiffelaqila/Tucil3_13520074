from matrix import *
from solver import *
import time

# FUNGSI DAN PROSEDUR MAIN PROGRAM

# PROSEDUR CETAK TITLE
def title():
    print("                                                                   ")
    print(" ██╗███████╗      ██████╗ ██╗   ██╗███████╗███████╗██╗     ███████╗")
    print("███║██╔════╝      ██╔══██╗██║   ██║╚══███╔╝╚══███╔╝██║     ██╔════╝")
    print("╚██║███████╗█████╗██████╔╝██║   ██║  ███╔╝   ███╔╝ ██║     █████╗  ")
    print(" ██║╚════██║╚════╝██╔═══╝ ██║   ██║ ███╔╝   ███╔╝  ██║     ██╔══╝  ")
    print(" ██║███████║      ██║     ╚██████╔╝███████╗███████╗███████╗███████╗")
    print(" ╚═╝╚══════╝      ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝╚══════╝")
    print("                                                                   ")
    print("        ███████╗ ██████╗ ██╗    ██╗   ██╗███████╗██████╗           ")
    print("        ██╔════╝██╔═══██╗██║    ██║   ██║██╔════╝██╔══██╗          ")
    print("        ███████╗██║   ██║██║    ██║   ██║█████╗  ██████╔╝          ")
    print("        ╚════██║██║   ██║██║    ╚██╗ ██╔╝██╔══╝  ██╔══██╗          ")
    print("        ███████║╚██████╔╝███████╗╚████╔╝ ███████╗██║  ██║          ")
    print("        ╚══════╝ ╚═════╝ ╚══════╝ ╚═══╝  ╚══════╝╚═╝  ╚═╝          ")
    print("                                                                   ")
    print("                                BY:                                ")
    print("                 EIFFEL AQILA AMARENDRA - 13520074                 ")
    print("                                                                   ")
    print("===================================================================")
    print("                                                                   ")

# PROSEDUR READ FILE TO MATRIX
def readFiletoMatrix(fileName, matrix):
    try:
        # READ FILE
        fileRead = open(fileName, 'r')
        
        # READLINE
        matrixLines = fileRead.readlines()

        # SETUP MATRIX
        # Inisialisasi i = 0
        i = 0
        for matrixLine in matrixLines:
            # Inisialisasi j = 0
            j = 0

            numbers = matrixLine.split()
            for number in numbers:
                numInt = int(number)
                matrix.setElmt(i, j, numInt)
                # Jika empty space ditemukan
                if (numInt == 16):
                    matrix.setEmptySpaceX(i)
                    matrix.setEmptySpaceY(j)
            
                # Inkremen j
                j += 1
            
            # Inkremen i
            i += 1        

    except Exception as e:
        print('Error opening: ' + fileName)
        print()
        exit(0)

# MAIN PROGRAM
if __name__ == "__main__":
    # Cetak title
    title()

    # Inisialisasi/Deklarasi/Konstruksi Matrix
    matrix = Matrix()

    # File Input
    print("Pilihan input method: ")
    print("1. Menggunakan test case yang tersedia")
    print("2. Menggunakan file baru")
    method = int(input("Masukkan pilihan file input method (1-2): "))

    print()
    if (method == 1):
        print("Test case yang tersedia: ")
        print("1. testSolvable1.txt")
        print("2. testSolvable2.txt")
        print("3. testSolvable3.txt")
        print("4. testUnsolvable1.txt")
        print("5. testUnsolvable2.txt")
        testInput = int(input("Masukkan pilihan file (1-5): "))
        if (testInput == 1):
            fileName = "testSolvable1.txt"
        elif (testInput == 2):
            fileName = "testSolvable2.txt"
        elif (testInput == 3):
            fileName = "testSolvable3.txt"
        elif (testInput == 4):
            fileName = "testUnsolvable1.txt"
        elif (testInput == 5):
            fileName = "testUnsolvable2.txt"
        else:
            fileName = "testSolvable1.txt"
    else:
        print("Pastikan file terdapat pada folder test!")
        fileName = input("Masukkan nama file (+ extensionnya): ")
    
    fileName = "../test/" + fileName

    # Read File to Matrix
    readFiletoMatrix(fileName, matrix)

    print()

    # Spek Luaran #1: Cetak matriks input (posisi awal)
    print("Matriks posisi awal 15-puzzle:")
    matrix.printMatrix()

    # Pemrosesan Branch & Bound
    startTime = time.time()
    nodeCount = solve(matrix)

    stopTime = time.time()
    print("Total waktu yang diperlukan: {0:.2f} detik".format(stopTime - startTime))
    print()
    print("Jumlah simpul yang dibangkitkan (termasuk posisi awal): " + str(nodeCount))
    print()