def ganti_kata(Masukankalimat, katadicari, diganti) :
    kata = Masukankalimat.split()
    for i in range(len(kata)) :
        if kata [i] == katadicari : 
            kata [i] = diganti
    Masukankalimat = " ".join(kata)       
    return Masukankalimat

Masukankalimat = input("Masukkan kalimat : " )
katadicari = input("Kata yang dicari : ")
diganti = input("Diganti menjadi : ")

kalimat_baru = ganti_kata(Masukankalimat, katadicari, diganti)
print ("Kalimat baru : ", kalimat_baru)
