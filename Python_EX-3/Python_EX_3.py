while True:
    hours = input("Hours worked:")
    rate = input("Enter rate:")
    def computepay(hours, rate):
        try:            
            fhours = float(hours)
            frate = float(rate)
        except:
            fhours = -1
            frate = -1
        if (fhours > 40):
            ot = (fhours - 40)
            regt = (fhours - ot)
            regpay = (regt * frate)
            otpay = (ot) * (frate * 1.5)
            totpay = (regpay + otpay)
            print("Regular pay:", regpay, "Overtime pay:", otpay)
            print("Total pay:", totpay)
            return totpay            
        if  fhours < 0 or frate < 0:
            print("Please enter a valid number.")        
        else:
            print("No overtime.")
            pay = (fhours * frate)
            return pay
    x = computepay(hours, rate)
    print("Pay:", x)
    if x != None:
        break

    