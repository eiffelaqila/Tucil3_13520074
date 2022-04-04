# File: solver.py
# Fungsi:
# - menyelesaikan permainan 15-Puzzle Game menggunakan algoritma branch and 

# Import matrix.py
from matrix import *

# Import copy untuk fungsi deepcopy
import copy

# Import heap queue
from heapq import *

# Import time
import time

# Fungsi totalKurang()
# Fungsi: menghitung total KURANG() sebagai cost(Root)
def totalKurang(matrix):
    # Inisialisasi sum = 0
    sum = 0

    print("\nNilai fungsi Kurang(i):")
    print("|===============================|")
    print("|ELMT(i)\t| KURANG(i)\t|")
    print("|===============|===============|")

    for i in range (matrix.rowSize):
        for j in range (matrix.colSize):
            kurangElmt = kurang(matrix,i,j) 
            print("|" + str(matrix.getElmt(i,j)) + "\t\t|" + str(kurangElmt) + "\t\t|")
            sum += kurangElmt
    
    print("|===============================|")
    return sum

# Fungsi kurang()
# Fungsi: Menghitung KURANG()
def kurang(matrix, i, j):
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
def printPath(matrix,solution):

    # Mencetak rute pergerakan matrix
    if (matrix.getPreviousMatrix() != None):
        printPath(matrix.getPreviousMatrix(),solution)
    matrix.printMatrix()
    solution.append(matrix)

# ALGORITMA UTAMA SOLVER BRANCH AND BOUND
def solve(matrix):
    # list solusi
    solution = []

    # Pemeriksaan apakah persoalan dapat diselesaikan atau tidak
    # Spek Luaran #2: Cetak nilai fungsi Kurang(i)
    costRoot = totalKurang(matrix) + statusX(matrix)
    
    # Spek Luaran #3: Cetak nilai sum of KURANG(i) + X
    print("\nNilai dari TOTALKURANG(i) + X: " + str(costRoot) + "\n")
    matrix.setCost(costRoot)

    # Spek Luaran #4: Jika persoalan tidak dapat diselesaikan, keluar pesan
    if (costRoot % 2 == 1):
        solution.append(matrix)

        # Stop time
        stopTime = time.time()

        print("Status tujuan permainan tidak dapat dicapai.\n")

        return 1, stopTime, solution, False
    
    # Pembuatan heap sebagai priority queue (antrian)
    print("Memproses persoalan...")
    print("Persoalan yang kompleks terkadang membutuhkan waktu yang cukup lama...")
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

        # Pemeriksaan solusi, jika ditemukan, stop
        if (isSolution(minMatrix)):
            # Stop time
            stopTime = time.time()

            # Spek Luaran #5: Menampilkan urutan matriks dari awal ke akhir
            print("\nUrutan Matrix dari Posisi Awal ke Goal State:\n")
            printPath(minMatrix,solution)
            
            return nodeCount, stopTime, solution, True
        
        # Jika belum ditemukan, bangkitkan semua anak-anaknya
        else:
            # Search empty space
            emptyX = minMatrix.getEmptySpaceX()
            emptyY = minMatrix.getEmptySpaceY()

            # Geser empty space ke atas
            if ((emptyX != 0) and (minMatrix.getPreviousMove() != "D")):
                # Expand matriks
                matrixExpandAtas = copy.deepcopy(minMatrix)
                matrixExpandAtas.atas()
                matrixExpandAtas.setPreviousMatrix(minMatrix)
                
                # Perhitungan cost
                costAtas = cost(matrixExpandAtas)
                matrixExpandAtas.setCost(costAtas)

                # Masukkan ke dalam antrian
                heappush(priorityQueue, matrixExpandAtas)
                nodeCount += 1

            # Geser empty space ke kanan
            if ((emptyY != 3) and (minMatrix.getPreviousMove() != "L")):
                # Expand matriks
                matrixExpandKanan = copy.deepcopy(minMatrix)
                matrixExpandKanan.kanan()
                matrixExpandKanan.setPreviousMatrix(minMatrix)
                
                # Perhitungan cost
                costKanan = cost(matrixExpandKanan)
                matrixExpandKanan.setCost(costKanan)
                
                # Masukkan ke dalam antrian
                heappush(priorityQueue, matrixExpandKanan)
                nodeCount += 1

            # Geser empty space ke bawah
            if ((emptyX != 3) and (minMatrix.getPreviousMove() != "U")):
                # Expand matriks
                matrixExpandBawah = copy.deepcopy(minMatrix)
                matrixExpandBawah.bawah()
                matrixExpandBawah.setPreviousMatrix(minMatrix)
                
                # Perhitungan cost
                costBawah = cost(matrixExpandBawah)
                matrixExpandBawah.setCost(costBawah)
                
                # Masukkan ke dalam antrian
                heappush(priorityQueue, matrixExpandBawah)
                nodeCount += 1
            
            # Geser empty space ke kiri
            if ((emptyY != 0) and (minMatrix.getPreviousMove() != "R")):
                # Expand matriks
                matrixExpandKiri = copy.deepcopy(minMatrix)
                matrixExpandKiri.kiri()
                matrixExpandKiri.setPreviousMatrix(minMatrix)
                
                # Perhitungan cost
                costKiri = cost(matrixExpandKiri)
                matrixExpandKiri.setCost(costKiri)
                
                # Masukkan ke dalam antrian
                heappush(priorityQueue, matrixExpandKiri)
                nodeCount += 1