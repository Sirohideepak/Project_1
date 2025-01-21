#python program for addition of two numbers
FN=int(input("Enter First Number : "))
SN=int(input("Enter Second Number : "))
result=FN+SN
#formatting string output

print("Result of",FN," and",SN," =",result)
print("Result of "+str(FN)+" and "+str(SN)+" = "+str(result))
print("Result of %d and %d = %d" % (FN,SN,result))
print("Result of {0} and {1} = {2}".format(FN,SN,result))




