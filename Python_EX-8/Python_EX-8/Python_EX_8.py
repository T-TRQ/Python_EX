
fname = input("Enter File: ")
if fname != "intro.txt":
    print("This file does not exist.")
hname = open(fname)

di = dict()
for lin in hname:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w,0) + 1

tmp = list()
for k,v in di.items():
    newtup = (v,k)
    tmp.append(newtup)
print(sorted(tmp))
