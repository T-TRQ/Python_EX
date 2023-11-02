
while True:    
    fhandle = input("State file name: ")
    try:
        openfile = open(fhandle)
    except:
        print("File name could not be found.", fhandle)
        continue
    for line in openfile:
        linestrip = line.rstrip()
        print(linestrip.upper())
    break


