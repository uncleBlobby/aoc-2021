# open input file
inputFile = open("inputData")

# read datalines in input file
with open('inputData') as f:
    lines = f.readlines()

# close input file
f.close()

# convert array of strings to array of integers for comparison
# will produce false results by comparing strings
for i in range(0, len(lines)):
    lines[i] = int(lines[i])

# part 1
total = 0   # initialize variable to hold total increases
for i in range(0, len(lines)):  # loop through the range in integer array of lines
        if lines[i]> lines[i - 1]:      # compare integers, increment count if second is larger
            total+=1

# part 2
total2 = 0  # initialize variable to hold total increases
for i in range(0, len(lines)):  # loop through the range in integer array of lines
    if(len(lines) - i < 4):     # break out of loop if there are not enough remaining integers to form final group of 3
        break
    if (lines[i] + lines[i+1] + lines[i+2] < lines[i+1] + lines[i+2] + lines[i+3]):     # compare three integer windows, increment count if second set is larger
        total2+=1

# Display results
print("The answer for Part 1:", total)
print("The answer for Part 2:", total2)

