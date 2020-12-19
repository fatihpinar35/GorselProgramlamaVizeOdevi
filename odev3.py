text = "Usak Universtesi"
search = "ver"
result = ""

if text.find(search):
    var1 = text.find(search)-1
    var2 = text.find(search) + len(search) + 1
    result = (text[var1:var2])
    print(result)
