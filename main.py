def gauss_seidel(a, b, parameter_toleransi=1e-5, max_iterasi=200):
    n = len(b)  # simpan jumlah elemen vektor b
    x = [0] * n  # Inisialisasi x dengan nol

    for iterasi in range(max_iterasi):
        x_lama = x.copy()  # Simpan nilai x sebelumnya

        for i in range(n): #loop proses setiap variabel
            if a[i][i] == 0:  # memeriksa elemen diagonal dari matrik a
                print("Tidak Konvergen")
                return None

            # Hitung nilai baru x[i]
            sum1 = sum(a[i][j] * x[j] for j in range(n) if j != i) #menghitung jumlah dari hasil perkalian
            x[i] = (b[i] - sum1) / a[i][i]

        # Output iterasi
        print(f"Iterasi ke-{iterasi + 1}: x = {x[0]}, y = {x[1]}, z = {x[2]}")

        # Cek kondisi konvergensi
        if all(abs(x[i] - x_lama[i]) < parameter_toleransi for i in range(n)):
            return x, iterasi + 1  # konvergen, kembalikan x dan jumlah iterasi

    print("Tidak Konvergen")
    return None, 0

# Set persamaan linear untuk pers_1
pers_1 = [
    [9, 3, 1],  # 9x + 3y + z = 13
    [2, -5, 1], # 2x - 5y + z = 6
    [-6, 0, 8]  # -6x + 8z = 2
]
b1 = [13, 6, 2]

# Set persamaan linear untuk pers_2
pers_2 = [
    [1, 1, 6],  # x + y + 6z = 8
    [4, 2, -2], # 4x + 2y - 2z = 4
    [1, 5, -1]  # x + 5y - z = 5
]
b2 = [8, 4, 5]

# Set persamaan linear untuk pers_3
pers_3 = [
    [-3, 4, 5], # -3x + 4y + 5z = 6
    [0, 2, -1], # 2y - z = 1
    [-2, 2, -4] # -2x + 2y - 4z = -3
]
b3 = [6, 1, -3]

# Urutan Iterasi
print("Hasil untuk pers_1:")
hasil_1, iterasi_1 = gauss_seidel(pers_1, b1)
if hasil_1:
    print("Hasil akhir: x =", hasil_1[0], ", y =", hasil_1[1], ", z =", hasil_1[2])

print("\n--------------------------------------------------------------------------------")

print("\nHasil untuk pers_2:")
hasil_2, iterasi_2 = gauss_seidel(pers_2, b2)
if hasil_2:
    print("Hasil akhir: x =", hasil_2[0], ", y =", hasil_2[1], ", z =", hasil_2[2])

print("\n--------------------------------------------------------------------------------")

print("\nHasil untuk pers_3:")
hasil_3, iterasi_3 = gauss_seidel(pers_3, b3)
if hasil_3:
    print("Hasil akhir: x =", hasil_3[0], ", y =", hasil_3[1], ", z =", hasil_3[2])

print("\n--------------------------------------------------------------------------------")

# Summary akhir untuk hasil semua persamaan
print("Summary Hasil Akhir:")
if hasil_1:
  print(f"\nPers_1: x = {hasil_1[0]}, y = {hasil_1[1]}, z = {hasil_1[2]}")
  print(f"Jumlah Iterasi: {iterasi_1} iterasi")
  print("Berhasil Konvergen")
else:
  print("Pers_1 Tidak Konvergen")

if hasil_2:
    print(f"\nPers_2: x = {hasil_2[0]}, y = {hasil_2[1]}, z = {hasil_2[2]}")
    print(f"Jumlah Iterasi: {iterasi_2} iterasi")
    print("Berhasil Konvergen")
else:
  print("\nPers_2 Tidak Konvergen")

if hasil_3:
    print(f"\nPers_3: x = {hasil_3[0]}, y = {hasil_3[1]}, z = {hasil_3[2]}")
    print(f"Jumlah Iterasi: {iterasi_3} iterasi")
    print("Berhasil Konvergen")
else:
  print("\nPers_3 Tidak Konvergen")