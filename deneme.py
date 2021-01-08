print("""

[1] Çarpma

[2] Bölme

[3] Toplama

[4] Çıkarma

[0] Hesap Makinesinden çık




 """)



giris = input("Seçiminizi Yapınız ; ")


if giris == "1": 
	x = input("birinici Sayı : ")
	x = float(x)
	y = input("ikinci Sayı : ")
	y = float(y)

	print("İşlem Sonucu ;" , x * y)



elif giris == "2": 
	x = input("birinici Sayı : ")
	x = float(x)
	y = input("ikinci Sayı : ")
	y = float(y)

	print("İşlem Sonucu ;" , x // y)



elif giris == "3": 
	x = input("birinici Sayı : ")
	x = float(x)
	y = input("ikinci Sayı : ")
	y = float(y)

	print("İşlem Sonucu ;" , x + y)



elif giris == "4": 
	x = input("birinici Sayı : ")
	x = float(x)
	y = input("ikinci Sayı : ")
	y = float(y)

	print("İşlem Sonucu ;" , x - y)



elif giris == "0" or "Q" or "q":
	quit()



else:
	print("Hatalı Girdin Kanka !!!")





v = input("Entera bas")	
	
