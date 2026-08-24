import random
sectet_number=(random.randint(1,100))
while True:
    number=int(input("guess the random number between 1-100:"))
    if sectet_number==number:
        print("you did it")
        break
    elif sectet_number>number:
        print("your number is smaller")
    else:
        print("your number is bigger")