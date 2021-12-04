# read datalines in input file
with open('inputData') as f:
    lines = f.readlines()

#close input file
f.close()

totalFullBits = []
totalEmptyBits = []
countMembers = 0
commonBit = []
leastCommonBit = []

for i in range(1, len(lines[0])):
    totalFullBits.append(0)
    totalEmptyBits.append(0)
    commonBit.append(0)
    leastCommonBit.append(0)

for i in range(0, len(lines)):
    #print(lines[i])
    for j in range(0, len(lines[i])):
        if(lines[i][j] == '1'):
            totalFullBits[j]+=1
        if(lines[i][j] == '0'):
            totalEmptyBits[j]+=1
    countMembers+=1

print("Total Full Bits (by position):", totalFullBits)
print("Total Empty Bits (by position):", totalEmptyBits)
print("Total Readings:", countMembers)

# find most common bit (0 or 1 in totalFullBits)...
# if totalFullBits[i] > (countMembers / 2) then commonBit = 1



for i in range(0, len(totalFullBits)):
    if(totalFullBits[i] > totalEmptyBits[i]):
        commonBit[i] = 1
        leastCommonBit[i] = 0
    else:
        commonBit[i] = 0
        leastCommonBit[i] = 1

#print(commonBit)

def convertArrayToString(array):
    outString = ''
    for i in array:
        outString += str(i)
    
    return outString

commonBitString = convertArrayToString(commonBit)
leastCommonBitString = convertArrayToString(leastCommonBit)
commonBitDec = int(commonBitString, 2)
leastCommonBitDec = int(leastCommonBitString, 2)
print("Gamma Binary:", commonBitString)
print("Gamma Dec:", commonBitDec)
print("Epsilon Binary:", leastCommonBitString)
print("Epsilon Dec:", leastCommonBitDec)

print("Power Consumption:", commonBitDec * leastCommonBitDec)
