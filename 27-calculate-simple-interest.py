def simpleInterest(principleAmount, noOfYear, rateOfInterest):
    return (principleAmount*noOfYear*rateOfInterest)/100

principleAmount = int(input("Enter principle amount :"))
noOfYear = int(input("Enter number of year :"))
rateOfInterest = int(input("Enter rate of interest :"))

simpleInterestRes = simpleInterest(principleAmount, noOfYear, rateOfInterest)
print("Simple Interest Result - ", simpleInterestRes)