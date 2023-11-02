hours = input("Hours worked:")
rate = input("Enter rate:")

try:
    fhours= float(hours)
    frate = float(rate)
except:
    fhours = -1
    frate = -1

if (fhours | frate < 0):
    print("Please enter a valid number.")
elif (fhours > 40):
    ot = (fhours - 40)
    regt = (fhours - ot)
    regpay = (regt * frate)
    otpay = (ot) * (frate * 1.5)
    print("Regular pay:", regpay, "Overtime pay:", otpay)
    print("Total pay:", regpay + otpay)
else:
    print("No overtime.")
    pay = (fhours * frate)
    print("pay:", pay)

