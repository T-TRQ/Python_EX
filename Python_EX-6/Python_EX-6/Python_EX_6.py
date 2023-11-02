from hashlib import new


filename = input("Enter file name: ")
openfile = open(filename)

counts = dict()
for line in openfile:
    line = line.rstrip()
    words = line.split()
    for word in words:
        oldcount = counts.get(word, 0)
        print(word, "old", oldcount)
        newcount = oldcount + 1
        counts[word] = newcount
        print(word, "new", newcount)

print(counts)

