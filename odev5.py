veri = "send-100-1-1-1\nreceive-100-1-0\n"
dizi = veri.split("\n")
ekran= 0
def fonksiyon(kod, bol):
   if ((int(bol[0]) >= 0 and int(bol[0]) <= 255) and (int(bol[1]) >= 1 and int(bol[1]) <= 4) and (int(bol[2]) >= 0 and int(bol[2]) <= 1) and ((len(bol) == 4 and int(bol[3]) >= 0 and int(bol[3]) <= 1) or len(bol) == 3)):
      print("Kod Tipi: " + kod)
      if (int(bol[0]) >= 0 and int(bol[0]) <= 50):
         print("Sinyal Gucu: " + bol[0] + " - Cok Zayif")
      elif (int(bol[0]) >= 51 and int(bol[0]) <= 100):
         print("Sinyal Gucu: " + bol[0] + " - Zayif")
      elif (int(bol[0]) >= 101 and int(bol[0]) <= 150):
         print("Sinyal Gucu: " + bol[0] + " - Orta")
      elif (int(bol[0]) >= 151 and int(bol[0]) <= 200):
         print("Sinyal Gucu: " + bol[0] + " - Guclu")
      elif (int(bol[0]) >= 201 and int(bol[0]) <= 255):
         print("Sinyal Gucu: " + bol[0] + " - Cok Guclu")
      else:
         print("Sinyal Gucu: Gecersiz")
      if (int(bol[1]) == 1):
         print("Cihaz: " + bol[1] + " - Televizyon")
      elif (int(bol[1]) == 2):
         print("Cihaz: " + bol[1] + " - Camasir Makinesi")
      elif (int(bol[1]) == 3):
         print("Cihaz: " + bol[1] + " - Buzdolabi")
      elif (int(bol[1]) == 4):
         print("Cihaz: " + bol[1] + " - Firin")
      else:
         print("Cihaz: Gecersiz")
      if (int(bol[2]) == 0):
         print("Durumu: " + bol[2] + " - Off")
      elif (int(bol[2]) == 1):
         print("Durumu: " + bol[2] + " - On")
      else:
         print("Durumu: Gecersiz")
      if (len(bol) == 4):
         if (int(bol[3]) == 0):
            print("Cevap: " + bol[3] + " - Istenmiyor")
         elif (int(bol[3]) == 1):
            print("Cevap: " + bol[3] + " - Isteniyor")
         else:
            print("Cevap: Gecersiz")
   else:
      print("Error: ikinci bolum hatali")
for i in dizi:
   if (len(i) > 0):
      bol = i.split("-")
      kod = bol.pop(0)
      ekran += 1
      if (ekran > 1):
         print("------")
      if (kod == "send"):
         if (len(bol) != 4):
            print("Error: ikinci bolum hatali")
         else:
            fonksiyon(kod + " - Giden", bol)
      elif (kod == "receive"):
         if (len(bol) != 3):
            print("Error: ikinci bolum hatali")
         else:
            fonksiyon(kod + " - Gelen", bol)
      else:
       print("Error: send ya da receive icermiyor")
