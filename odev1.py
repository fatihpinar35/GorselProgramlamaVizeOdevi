email = "ali.erbey@ogr.usak.edu.tr"
for control in  email:
    if ( control == "@" ):
        print("e-mail adresiniz doğrudur")
        break
else:
    print("e-mail adresiniz hatalıdır")