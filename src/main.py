# File: main.py
# Fungsi:
# - Mencetak title
# - Menerima input file
# - Membaca file input dan dikonversi menjadi matrix
# - Menyelesaikan matrix 15-puzzle

# Import matrix dan solver
from matrix import *
from solver import *

# Import library time
import time

# Import library random
import random

# Prosedur title()
# Fungsi: Mencetak title
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

# Prosedur readFiletoMatrix()
# Fungsi: Mengonversi file input menjadi matrix
def readFiletoMatrix(fileName, matrix):
    # Algoritma
    
    # Try - Exception: jika file tidak dapat dibaca
    try:
        # Membaca file
        fileRead = open(fileName, 'r')
        
        # Membaca setiap baris file
        matrixLines = fileRead.readlines()

        # Konversi menjadi matrix
        # Inisialisasi i = 0
        i = 0
        
        for matrixLine in matrixLines:
            # Inisialisasi j = 0
            j = 0

            # Membaca setiap angka di dalam baris
            numbers = matrixLine.split()
            for number in numbers:

                # Memasukkan angka ke dalam matrix
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

# Prosedur randomToMatrix()
# Fungsi: membuat matrix yang berisi bilangan random (1..16)
def randomToMatrix(matrix):
    listRandom = list(range(1,17))
    random.shuffle(listRandom)

    idx = 0
    for i in range(matrix.rowSize):
            for j in range(matrix.colSize):
                value = listRandom[idx]
                matrix.setElmt(i, j, value)
                if (value == 16):
                    matrix.setEmptySpaceX(i)
                    matrix.setEmptySpaceY(j)
                idx += 1

# MAIN PROGRAM
if __name__ == "__main__":
    # Cetak title
    title()

    # Inisialisasi/Deklarasi/Konstruksi Matrix
    matrix = Matrix()

    # File Input
    print("Pilihan input method: ")
    print("1. Menggunakan test case yang tersedia")
    print("2. Menggunakan matrix yang dibuat secara acak")
    print("3. Menggunakan file baru")
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
        
        fileName = "./test/" + fileName

        # Read File to Matrix
        readFiletoMatrix(fileName, matrix)

        print()
        print("File input: " + str(fileName))
    elif (method == 2):
        randomToMatrix(matrix)

        print()
        print("Menggunakan matriks random")
    else:
        print("Pastikan file terdapat pada folder test!")
        fileName = input("Masukkan nama file (+ extensionnya): ")
        
        fileName = "./test/" + fileName

        # Read File to Matrix
        readFiletoMatrix(fileName, matrix)

        print()
        print("File input: " + str(fileName))

    print()
    # Spek Luaran #1: Cetak matriks input (posisi awal)
    print("Matriks posisi awal 15-puzzle:")
    matrix.printMatrix()

    # Pemrosesan Branch & Bound
    # Start time
    startTime = time.time()

    nodeCount, stopTime = solve(matrix) 

    # Spek Luaran #6: Cetak waktu eksekusi
    print("Total waktu yang diperlukan: {0:.2f} detik".format(stopTime - startTime))
    print()

    # Spek Luaran #7: Cetak jumlah simpul yang dibangkitkan
    print("Jumlah simpul yang dibangkitkan (termasuk posisi awal): " + str(nodeCount))
    print()