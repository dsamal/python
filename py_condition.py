__author__ = 'DEBASISH'
#Conditions in Python

print "Welcome! Here we will try few conditional statements in Python"
name = raw_input("What's your Name")
age = input("What is your Age")
if age >= 60:
    print "Hmmm Seems like ", name, " is a retired Person"
elif age >= 40 & age < 60:
    print "Hmmm Seems like ", name, " is an experienced professional"
elif age >= 20 & age < 40:
    print "Hmmm Seems like ", name, " is a young guy"
elif age < 10:
    print "Oh..", name, " is a baby"
else:
    print "Oh..", name, "is a grown up boy"
