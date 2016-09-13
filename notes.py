
import random

print(random.randint(1, 20))


tommys_age = input("How old are you?: ")
tommys_age = int(tommys_age)
michaels_age = 26

# Boolean

print(tommys_age > michaels_age)

if tommys_age > michaels_age:
    print("you are older than michael")
elif tommys_age == michaels_age:
    print("you are the same age as michael")
else:
    print("you are NOT older than michael")
