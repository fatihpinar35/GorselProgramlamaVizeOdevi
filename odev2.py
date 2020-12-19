domaninName = "www.alierbey.com"

for control in range(len(domaninName)) :
    if (domaninName[control:] == ".com"):
        print("Url Adresi Geçerlidir")
        break
    elif (domaninName[control:] == ".net"):
        print("Url Adresi Geçerlidir")
        break
    elif (domaninName[control:] == ".org"):
        print("Url Adresi Geçerlidir")
        break 
else :
    print('Url Adresi Geçersizdir !')