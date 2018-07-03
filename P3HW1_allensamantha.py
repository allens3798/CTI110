#CTI-110
#P3HW1 - Age Classifier
#Samantha Allen
#July 3rd, 2018


#Are you an infant, child, teenage, or adult?

age = int(input('Enter the persons age: '))

# if person is 1 or younger
if age <=1: print ("The person is an infant")
          
# if person is older than 1 but younger than 13
if age >1 and age <13: print ("The person is a child")

# if person is at least 13, but less than 20
elif age >=13 and age <20: print ("The person is a teenager")

# if person is 20 or older
elif age > 20: print ("The person is an adult")
          
