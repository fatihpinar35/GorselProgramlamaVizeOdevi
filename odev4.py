total=0
for i in range(100, 999):
    var1 = str(i)[0]
    var2 = str(i)[1]
    var3 = str(i)[2]

    if var1 !=var2 and var1 !=var3 and var2!=var3 :
     print(i)
     total += 1  
print("3 Basamaklı rakamları bir birinden farklı "+str(total)+" sayı vardır.")  
