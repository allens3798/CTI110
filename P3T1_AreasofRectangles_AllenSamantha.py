# Get the dimensions of rectangle A
lengthA = int(input('Enter the length of rectangle A: '))
widthA = int(input('Enter the width of rectangle A:  '))

#Get dimensions of rectangle B
lengthB = int(input('Enter the length of rectangle B: '))
widthB = int(input('Enter the width of rectangle B:  '))

#Calculate the areas of the rectangles
areaA = lengthA * widthA
areaB = lengthB * widthB

#Determine which has the great area
if areaA > areaB:
    print('Rectangle A has the greater area.')
elif areaB > areaA:
    print('Rectangle B has the greater area.')
else:
    print('Both rectangles have the same area.')
    
