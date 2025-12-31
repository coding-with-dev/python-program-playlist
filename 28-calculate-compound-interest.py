def calculateCompoundInterest(principleAmount, noOfYear, rateOfInterest):
    amount = principleAmount * ((1+rateOfInterest/100) ** noOfYear)
    return amount - principleAmount

principleAmount = int(input("Enter principle amount : "))
noOfYear = int(input("Enter number of year : "))
rateOfInterest = int(input("Enter rate of interest : "))

compountInterestRes = calculateCompoundInterest(principleAmount, noOfYear, rateOfInterest)
print("Compound Interest Result - ", compountInterestRes)