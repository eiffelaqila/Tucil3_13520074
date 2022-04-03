# File: solver.py
# Program untuk menyelesaikan permainan 15-Puzzle Game
# Menggunakan algoritma branch and bound

# Import matrix.py
from matrix import *

# Import copy untuk fungsi deepcopy
import copy

# Import heap queue
from heapq import *

# Fungsi untuk menghitung total KURANG() sebagai cost(Root)
def totalKurang(matrix):
    # Menjumlahkan seluruh KURANG() untuk setiap ubin

    # Inisialisasi sum = 0
    sum = 0

    print("Nilai fungsi Kurang(i):")
    print("ELMT(i)\tKURANG(i)")

    for i in range (matrix.rowSize):
        for j in range (matrix.colSize):
            kurangElmt = kurang(matrix,i,j) 
            print(str(matrix.getElmt(i,j)) + ":\t" + str(kurangElmt))
            sum += kurangElmt
    return sum

# Fungsi untuk menghitung KURANG()
def kurang(matrix, i, j):
    # Definisi KURANG():
    # banyaknya ubin bernomor j sedemikian sehingga j < i
    # dan POSISI(j) > POSISI(i)

    # Inisialisasi count = 0
    count = 0

    for x in range (matrix.rowSize):
        for y in range (matrix.colSize):
            if ((x*matrix.rowSize + y) > (i*matrix.rowSize + j)):
                if (matrix.getElmt(x,y) < matrix.getElmt(i,j)):
                    count += 1
    return count

# Fungsi untuk mengembalikan nilai X
def statusX(matrix):
    # X = 1 jika sel kosong berada pada posisi awal pada sel yang diarsir
    # X = 0 jika tidak

    # Sel kosong berada di sel yang diarsir
    if ((matrix.getEmptySpaceX() + matrix.getEmptySpaceY()) % 2 == 1):
        return 1
    # Sel kosong tidak berada di sel yang diarsir
    else:
        return 0

# Fungsi untuk menghitung cost(P)
def cost(matrix):
    # cost simpul P: c(P) = f(P) + g(P)
    return (matrix.getCountMove() + costG(matrix))

# Fungsi untuk menghitung g(P)
def costG(matrix):
    # g(P): jumlah ubin tak kosong yang tidak terdapat pada susunan akhir

    # Inisialisasi count = 0
    count = 0

    for x in range (matrix.rowSize):
        for y in range (matrix.colSize):
            if ((x*matrix.rowSize + y) != matrix.getElmt(x,y)-1):
                count += 1
    return count

# Fungsi untuk memeriksa apakah matrix merupakan solusi/goal state
def isSolution(matrix):
    return (costG(matrix) == 0)

# PRINT PATH
def printPath(matrix):

    # Mencetak rute pergerakan matrix
    if (matrix.getPreviousMatrix() != None):
        printPath(matrix.getPreviousMatrix())
    matrix.printMatrix()
    print()

# ALGORITMA UTAMA SOLVER BRANCH AND BOUND
def solve(matrix):
    # PEMERIKSAAN APAKAH MATRIX DAPAT DISOLVE

    # Luaran 2:
    print()
    costRoot = totalKurang(matrix) + statusX(matrix)
    
    # Luaran 3:
    print()
    print("Nilai dari TOTALKURANG(i) + X: " + str(costRoot))
    matrix.setCost(costRoot)

    # Luaran 4:
    print()
    if (costRoot % 2 == 1):
        print("Status tujuan permainan tidak dapat dicapai.")
        return 0
    
    # Pembuatan heap sebagai priority queue (antrian)
    print("Memproses persoalan...")
    priorityQueue = []

    # Masukkan matriks (simpul) akar ke dalam antrian
    heappush(priorityQueue, matrix)

    # Inisialisasi jumlah node
    nodeCount = 1

    # Jika antrian kosong, stop
    # Jika tidak kosong, pilih simpul dengan cost terendah (berdasarkan priority queue)
    while priorityQueue:
        
        # Ambil simpul dengan cost terendah
        minMatrix = heappop(priorityQueue)
        # print("Yang dipilih: ")
        # print("Prev. Move: {}".format(minMatrix.getPreviousMove()))
        # minMatrix.printMatrix()
        # print()

        # Pemeriksaan solusi, jika ditemukan, stop
        if (isSolution(minMatrix)):
            # Luaran 5:
            print("Proses Pencarian")
            printPath(minMatrix)
            return nodeCount
        
        # Jika belum ditemukan, bangkitkan semua anak-anaknya
        else:
            # Search empty space
            emptyX = minMatrix.getEmptySpaceX()
            emptyY = minMatrix.getEmptySpaceY()

            # Geser empty space ke atas
            if ((emptyX != 0) and (minMatrix.getPreviousMove() != "D")):
                matrixExpandAtas = copy.deepcopy(minMatrix)
                matrixExpandAtas.atas()
                matrixExpandAtas.setPreviousMatrix(minMatrix)

                costAtas = cost(matrixExpandAtas)
                matrixExpandAtas.setCost(costAtas)
                # matrixExpandAtas.printMatrix()
                # print()
                heappush(priorityQueue, matrixExpandAtas)
                # print(nodeCount)
                # print("U")
                nodeCount += 1

            # Geser empty space ke kanan
            if ((emptyY != 3) and (minMatrix.getPreviousMove() != "L")):
                matrixExpandKanan = copy.deepcopy(minMatrix)
                matrixExpandKanan.kanan()
                matrixExpandKanan.setPreviousMatrix(minMatrix)
                
                costKanan = cost(matrixExpandKanan)
                matrixExpandKanan.setCost(costKanan)
                # matrixExpandKanan.printMatrix()
                # print()
                heappush(priorityQueue, matrixExpandKanan)
                # print(nodeCount)
                # print("R")
                nodeCount += 1

            # Geser empty space ke bawah
            if ((emptyX != 3) and (minMatrix.getPreviousMove() != "U")):
                matrixExpandBawah = copy.deepcopy(minMatrix)
                matrixExpandBawah.bawah()
                matrixExpandBawah.setPreviousMatrix(minMatrix)
                
                costBawah = cost(matrixExpandBawah)
                matrixExpandBawah.setCost(costBawah)
                # matrixExpandBawah.printMatrix()
                # print()
                heappush(priorityQueue, matrixExpandBawah)
                # print(nodeCount)
                # print("D")
                nodeCount += 1
            
            # Geser empty space ke kiri
            if ((emptyY != 0) and (minMatrix.getPreviousMove() != "R")):
                matrixExpandKiri = copy.deepcopy(minMatrix)
                matrixExpandKiri.kiri()
                matrixExpandKiri.setPreviousMatrix(minMatrix)
                
                costKiri = cost(matrixExpandKiri)
                matrixExpandKiri.setCost(costKiri)
                # matrixExpandKiri.printMatrix()
                # print()
                heappush(priorityQueue, matrixExpandKiri)
                # print(nodeCount)
                # print("L")
                nodeCount += 1