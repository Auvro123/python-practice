list=["lomba theng wala shingho🐅","baitta thota wala giraffe🦒🐱‍🐉"]

while True:
    upodesh=input("enter a command: ")
    if upodesh=='quit':
        break
    if upodesh=='add':
        vlue=input("what I shall add? ")
        list.append(vlue)
    if upodesh=='view':
        for upodesh in list:
            print(upodesh)
    if upodesh=='remove':
        alu=int(input("what shall i remove? "))
        list.pop(alu)