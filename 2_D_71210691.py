def hitung_mobil():
    jumlahSol = 0
    jumlahSur = 0
    jumlahJog = 0
    jumlahMag = 0

    done = False
    while not done:
        daerah = input("Masukkan asal mobil (ketik 'done' untuk keluar) : ")
        
        if daerah == 'done':
            done = True
        elif daerah == "Solo":
            jumlahSol += 1
        elif daerah == "Surabaya":
            jumlahSur += 1
        elif daerah == "Jogja":
            jumlahJog += 1
        elif daerah == "Magelang":
            jumlahMag += 1

    print(f"Jumlah mobil dari Solo : {jumlahSol}")
    print(f"jumlah mobil dari Surabaya : {jumlahSur}")
    print(f"jumlah mobil dari Jogja : {jumlahJog}")
    print(f"jumlah mobil dari Magelang : {jumlahMag}")

hitung_mobil()
