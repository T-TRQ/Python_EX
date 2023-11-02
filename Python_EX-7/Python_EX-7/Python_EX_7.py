from audioop import reverse


while True:
    filename = input("Enter file name: ")
    try:
        handle = open(filename)
    except:
        print("File does not exist.")
        continue

    diccy = dict()
    
    for line in handle:
        line = line.rstrip()
        words = line.split()
        for word in words:
            diccy[word] = diccy.get(word, 0) + 1
    #print(diccy)
    diclist = list()
    for k,v in diccy.items():
        newtup = (v,k)
        diclist.append(newtup)

    diclist = sorted(diclist, reverse = True)
    for v,k in diclist:
        print(k,v)
    break