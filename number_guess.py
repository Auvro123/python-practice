import random
secret_number=(random.randint(1,100))
while True:
    number=int(input("guess the random number between 1-100:"))
    if secret_number==number:
        print("you did it")
        break
    elif secret_number>number:
        print("your number is smaller")
    else:
        print("your number is bigger")