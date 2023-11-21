def aman(board, baris, kolom, n):
    # Memeriksa apakah ada ratu di baris yang sama di sebelah kiri
    for i in range(kolom):
        if board[baris][i] == 1:
            return False

    # Memeriksa apakah ada ratu di diagonal atas kiri
    for i, j in zip(range(baris, -1, -1), range(kolom, -1, -1)):
        if board[i][j] == 1:
            return False

    # Memeriksa apakah ada ratu di diagonal bawah kiri
    for i, j in zip(range(baris, n, 1), range(kolom, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, kolom, n):
    if kolom >= n:
        return True

    for i in range(n):
        if aman(board, i, kolom, n):
            board[i][kolom] = 1

            if solve_n_queens_util(board, kolom + 1, n):
                return True

            # Backtrack jika penempatan ratu pada posisi saat ini tidak menghasilkan solusi
            board[i][kolom] = 0

    return False

def solve_n_queens(n):
    # Inisialisasi papan catur kosong
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_n_queens_util(board, 0, n):
        print("Solusi tidak ada")
        return

    # Cetak solusi
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()

#N = 8
solve_n_queens(8)
