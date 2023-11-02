
from ast import Num
from operator import countOf


count = 1
total = 0.0

while True:
    strvalue = input("Enter a number:") 
    if strvalue == "done":        
        print(total, ",", count, ",", avg)
        break    
    try:
        numvalue = float(strvalue)
    except:
        print("Bad data, enter a valid number.")
        continue
    print(count, ")", numvalue)    
    count = count + 1
    total = total + numvalue
    avg = total/count


    

