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

# Import tkinter for VISUALIZATION
from tkinter import *
from tkinter import messagebox

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

# TKINTER VISUALIZATION
def visualize(solution, isSolvable):
    global matrixSolution, solvable, label0, label1, label2, label3, label4, label5, label6, label7, label8, label9, label10, label11, label12, label13, label14, label15

    # Procedure Play
    def Play():
        if (solvable):
            if (matrixSolution != []):
                # Ambil isi matriks dari list solusi
                curMatrix = matrixSolution.pop(0)

                # Ubah isi label
                label0.config(text=curMatrix.getElmt(0,0), bg='#2F4058')
                label1.config(text=curMatrix.getElmt(0,1), bg='#2F4058')
                label2.config(text=curMatrix.getElmt(0,2), bg='#2F4058')
                label3.config(text=curMatrix.getElmt(0,3), bg='#2F4058')
                label4.config(text=curMatrix.getElmt(1,0), bg='#2F4058')
                label5.config(text=curMatrix.getElmt(1,1), bg='#2F4058')
                label6.config(text=curMatrix.getElmt(1,2), bg='#2F4058')
                label7.config(text=curMatrix.getElmt(1,3), bg='#2F4058')
                label8.config(text=curMatrix.getElmt(2,0), bg='#2F4058')
                label9.config(text=curMatrix.getElmt(2,1), bg='#2F4058')
                label10.config(text=curMatrix.getElmt(2,2), bg='#2F4058')
                label11.config(text=curMatrix.getElmt(2,3), bg='#2F4058')
                label12.config(text=curMatrix.getElmt(3,0), bg='#2F4058')
                label13.config(text=curMatrix.getElmt(3,1), bg='#2F4058')
                label14.config(text=curMatrix.getElmt(3,2), bg='#2F4058')
                label15.config(text=curMatrix.getElmt(3,3), bg='#2F4058')

                emptyX = curMatrix.getEmptySpaceX()
                emptyY = curMatrix.getEmptySpaceY()
                location = emptyX*4 + emptyY
                if (location == 0):
                    label0.config(text='', bg="#DDE8F7")
                elif (location == 1):
                    label1.config(text='', bg="#DDE8F7")
                elif (location == 2):
                    label2.config(text='', bg="#DDE8F7")
                elif (location == 3):
                    label3.config(text='', bg="#DDE8F7")
                elif (location == 4):
                    label4.config(text='', bg="#DDE8F7")
                elif (location == 5):
                    label5.config(text='', bg="#DDE8F7")
                elif (location == 6):
                    label6.config(text='', bg="#DDE8F7")
                elif (location == 7):
                    label7.config(text='', bg="#DDE8F7")
                elif (location == 8):
                    label8.config(text='', bg="#DDE8F7")
                elif (location == 9):
                    label9.config(text='', bg="#DDE8F7")
                elif (location == 10):
                    label10.config(text='', bg="#DDE8F7")
                elif (location == 11):
                    label11.config(text='', bg="#DDE8F7")
                elif (location == 12):
                    label12.config(text='', bg="#DDE8F7")
                elif (location == 13):
                    label13.config(text='', bg="#DDE8F7")
                elif (location == 14):
                    label14.config(text='', bg="#DDE8F7")
                elif (location == 15):
                    label15.config(text='', bg="#DDE8F7")
                
                # Lanjutkan dengan isi matriks dari list solusi selanjutnya
                root.after(500,Play)
        else:
            # Jika persoalan tidak dapat diselesaikan
            messagebox.showinfo('Error Warning', 'Persoalan tidak dapat diselesaikan!')

    # Algoritma Utama
    matrixSolution = solution
    solvable = isSolvable

    # Create Tkinter
    root = Tk()
    root.title = "SOLUTION VISUALIZER"
    root.config(bg="#DDE8F7")

    # Matriks awal
    curMatrix = matrixSolution.pop(0)

    # Setup visualisasi
    label0 = Label(root, text=curMatrix.getElmt(0,0), bg='#2F4058', fg="#DDE8F7", width=3, height=1, font=("Arial", 25))
    label0.grid(row = 0, column = 0, padx = 1, pady = 1)
    label1 = Label(root, text=curMatrix.getElmt(0,1), bg='#2F4058', fg="#DDE8F7", width=3, height=1, font=("Arial", 25))
    label1.grid(row = 0, column = 1, padx = 1, pady = 1)
    label2 = Label(root, text=curMatrix.getElmt(0,2), bg='#2F4058', fg="#DDE8F7", width=3, height=1, font=("Arial", 25))
    label2.grid(row = 0, column = 2, padx = 1, pady = 1)
    label3 = Label(root, text=curMatrix.getElmt(0,3), bg='#2F4058', fg="#DDE8F7", width=3, height=1, font=("Arial", 25))
    label3.grid(row = 0, column = 3, padx = 1, pady = 1)
    label4 = Label(root, text=curMatrix.getElmt(1,0), bg='#2F4058', fg="#DDE8F7", width=3, height=1, font=("Arial", 25))
    label4.grid(row = 1, column = 0, padx = 1, pady = 1)
    label5 = Label(root, text=curMatrix.getElmt(1,1), bg='#2F4058', fg="#DDE8F7", width=3, height=1, font=("Arial", 25))
    label5.grid(row = 1, column = 1, padx = 1, pady = 1)
    label6 = Label(root, text=curMatrix.getElmt(1,2), bg='#2F4058', fg="#DDE8F7", width=3, height=1, font=("Arial", 25))
    label6.grid(row = 1, column = 2, padx = 1, pady = 1)
    label7 = Label(root, text=curMatrix.getElmt(1,3), bg='#2F4058', fg="#DDE8F7", width=3, height=1, font=("Arial", 25))
    label7.grid(row = 1, column = 3, padx = 1, pady = 1)
    label8 = Label(root, text=curMatrix.getElmt(2,0), bg='#2F4058', fg="#DDE8F7", width=3, height=1, font=("Arial", 25))
    label8.grid(row = 2, column = 0, padx = 1, pady = 1)
    label9 = Label(root, text=curMatrix.getElmt(2,1), bg='#2F4058', fg="#DDE8F7", width=3, height=1, font=("Arial", 25))
    label9.grid(row = 2, column = 1, padx = 1, pady = 1)
    label10 = Label(root, text=curMatrix.getElmt(2,2), bg='#2F4058', fg="#DDE8F7", width=3, height=1, font=("Arial", 25))
    label10.grid(row = 2, column = 2, padx = 1, pady = 1)
    label11 = Label(root, text=curMatrix.getElmt(2,3), bg='#2F4058', fg="#DDE8F7", width=3, height=1, font=("Arial", 25))
    label11.grid(row = 2, column = 3, padx = 1, pady = 1)
    label12 = Label(root, text=curMatrix.getElmt(3,0), bg='#2F4058', fg="#DDE8F7", width=3, height=1, font=("Arial", 25))
    label12.grid(row = 3, column = 0, padx = 1, pady = 1)
    label13 = Label(root, text=curMatrix.getElmt(3,1), bg='#2F4058', fg="#DDE8F7", width=3, height=1, font=("Arial", 25))
    label13.grid(row = 3, column = 1, padx = 1, pady = 1)
    label14 = Label(root, text=curMatrix.getElmt(3,2), bg='#2F4058', fg="#DDE8F7", width=3, height=1, font=("Arial", 25))
    label14.grid(row = 3, column = 2, padx = 1, pady = 1)
    label15 = Label(root, text=curMatrix.getElmt(3,3), bg='#2F4058', fg="#DDE8F7", width=3, height=1, font=("Arial", 25))
    label15.grid(row = 3, column = 3, padx = 1, pady = 1)

    emptyX = curMatrix.getEmptySpaceX()
    emptyY = curMatrix.getEmptySpaceY()
    location = emptyX*4 + emptyY
    if (location == 0):
        label0.config(text='', bg="#DDE8F7")
    elif (location == 1):
        label1.config(text='', bg="#DDE8F7")
    elif (location == 2):
        label2.config(text='', bg="#DDE8F7")
    elif (location == 3):
        label3.config(text='', bg="#DDE8F7")
    elif (location == 4):
        label4.config(text='', bg="#DDE8F7")
    elif (location == 5):
        label5.config(text='', bg="#DDE8F7")
    elif (location == 6):
        label6.config(text='', bg="#DDE8F7")
    elif (location == 7):
        label7.config(text='', bg="#DDE8F7")
    elif (location == 8):
        label8.config(text='', bg="#DDE8F7")
    elif (location == 9):
        label9.config(text='', bg="#DDE8F7")
    elif (location == 10):
        label10.config(text='', bg="#DDE8F7")
    elif (location == 11):
        label11.config(text='', bg="#DDE8F7")
    elif (location == 12):
        label12.config(text='', bg="#DDE8F7")
    elif (location == 13):
        label13.config(text='', bg="#DDE8F7")
    elif (location == 14):
        label14.config(text='', bg="#DDE8F7")
    elif (location == 15):
        label15.config(text='', bg="#DDE8F7")
    
    labelTitle = Label(root, text="15-Puzzle Solver Visualization", bg='#DDE8F7', fg="#2F4058", height=1, font=("Arial", 25))
    labelTitle.grid(row = 0, column = 4, padx = 1, pady = 1)
    labelTime = Label(root, text="Oleh:", bg="#DDE8F7", fg="#2F4058", height=1, font=("Arial", 12), justify = "left")
    labelTime.grid(row = 1, column = 4, padx = 1, pady = 1)
    labelCount = Label(root, text="Eiffel Aqila Amarendra - 13520074", bg="#DDE8F7", fg="#2F4058", height=1, font=("Arial", 12), justify = "left")
    labelCount.grid(row = 2, column = 4, padx = 1, pady = 1)

    # Menjalankan visualisasi
    playButton = Button(root, text = "Play", bg = "#2F4058", fg="#DDE8F7", height = 1, width = 4, command = Play)
    playButton.grid(row = 3, column = 4, padx = 1, pady = 1)

    root.mainloop()

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

    while (method < 1 or method > 3):
        print("\nMasukan tidak sesuai!")
        print("Pilihan input method: ")
        print("1. Menggunakan test case yang tersedia")
        print("2. Menggunakan matrix yang dibuat secara acak")
        print("3. Menggunakan file baru")
        method = int(input("Masukkan pilihan file input method (1-2): "))

    if (method == 1):
        print("\nTest case yang tersedia: ")
        print("1. testSolvable1.txt")
        print("2. testSolvable2.txt")
        print("3. testSolvable3.txt")
        print("4. testUnsolvable1.txt")
        print("5. testUnsolvable2.txt")
        testInput = int(input("Masukkan pilihan file (1-5): "))

        while (testInput < 1 or testInput > 5):
            print("\nMasukan tidak sesuai!")
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

        print("\nFile input: " + str(fileName))
    elif (method == 2):
        randomToMatrix(matrix)

        print("\nMenggunakan matriks random")
    else:
        print("\nPastikan file terdapat pada folder test!")
        print("Pastikan pula space kosong ditandai dengan bilangan 16!")
        fileName = input("Masukkan nama file (+ extensionnya): ")
        
        fileName = "./test/" + fileName

        # Read File to Matrix
        readFiletoMatrix(fileName, matrix)

        print("\nFile input: " + str(fileName))

    # Spek Luaran #1: Cetak matriks input (posisi awal)
    print("\nMatriks posisi awal 15-puzzle:")
    matrix.printMatrix()

    # Pemrosesan Branch & Bound
    # Start time
    startTime = time.time()

    nodeCount, stopTime, solution, isSolvable = solve(matrix) 

    # Spek Luaran #6: Cetak waktu eksekusi
    print("Total waktu yang diperlukan: {0:.2f} detik\n".format(stopTime - startTime))

    # Spek Luaran #7: Cetak jumlah simpul yang dibangkitkan
    print("Jumlah simpul yang dibangkitkan (termasuk posisi awal): " + str(nodeCount) + "\n")

    # Visualisasi Pergerakan
    visualize(solution, isSolvable)