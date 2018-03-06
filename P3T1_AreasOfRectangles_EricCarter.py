#CTI 110
#P3T1_AreasOfRectangles_EricCarter
#Eric Carter
#03/06/2018

# Get the dimensions of rectangle 1.
length1_eac = int(input('Enter the length of rectangle 1: '))
width1_eac = int(input('Enter the width of rectangle 1: '))

# Get the dimensions of rectangle 2.
length2_eac = int(input('Enter the length of rectangle 2: '))
width2_eac = int(input('Enter the width of rectangle 2: '))

#Calculate the areas of the rectangles.
area1 = length1_eac * width1_eac
area2 = length2_eac * width2_eac

# Determine which has the greater area.
if area1 > area2:
    print('Rectangle 1 has the greater area.')
elif area2 > area1:
    print('Rectangle 2 has the greater area.')
else:
    print('Both have the same area.')
    
