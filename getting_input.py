name = input("What is your name? ")
print("Nice to meet you, ", name)
age = input("What is your age? ")
try:
    age = int(age)
    print("You were born in", 2025-age)
except ValueError:
    print("That is not a proper number")
except NameError:
    print("You are misspelling something")
except:
    print("This will catch all other exceptions")
else:
    print("Thanks for playing fair") #if no exception was run
finally:
    print("This will happen no matter what") #always happens