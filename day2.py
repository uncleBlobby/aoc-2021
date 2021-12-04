# read datalines in input file
with open('inputData') as f:
    lines = f.readlines()

# close input file
f.close()

## PART 1 SOLUTION

# init variables to store movements

position = 0
depth = 0

for i in range(0, len(lines)):
    
    # first character in string indicates direction (f = forward, d = down, u = up)
    # last character in string (-2 position) identifies magnitude
    firstChar = lines[i][0]
    magnitude = int(lines[i][-2])
    if(firstChar == 'f'):
        position+=magnitude
    if(firstChar == 'd'):
        depth+=magnitude
    if(firstChar == 'u'):
        depth-=magnitude

print("Part 1 Answer:", position * depth)

## PART 2 SOLUTION

# init variables to store movements and aim
position = 0
depth = 0
aim = 0

for i in range(0, len(lines)):
    
    # first character in string indicates direction (f = forward, d = down, u = up)
    # last character in string (-2 position) identifies magnitude
    firstChar = lines[i][0]
    magnitude = int(lines[i][-2])
    if(firstChar == 'f'):
        position+=magnitude
        depth+=magnitude*aim
    if(firstChar == 'd'):
        aim+=magnitude
    if(firstChar == 'u'):
        aim-=magnitude
    
print("Part 2 Answer:", position * depth)