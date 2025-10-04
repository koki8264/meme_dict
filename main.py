from random import choice 
sym =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
quest = int(input("введи нужную длину пароля"))
parol = ""
for i in range(quest):
    rand = choice(sym)
    parol += rand
print(parol)