#boolean operators (or, and, not)
print(True or False)
print(True and False)
# False is considered: 0,0,0 False, None, "", etc

print(5 or 7) #first one that matches
print(5 and 7) #last one that matches
print(None or False or 11 or 12 or 0) #first match
print(None or False or 0 or 0.0)
print(7 and 8 and 0 and 9 and 10) # first one that doesnt match
print(7 and 8 and 9 and 10) # of all match then last one
print("not 7 is =", not 7)
print("not False is =", not False) 
