import random 
print(3)
print(22*22/11)
print(341/31+213*23)
print(12+25+213*23)
age=int(input("Сколько вам лет"))
if age==13:
    print("Мне тоже 13")
if age>13:
    print("Значит вы старше меня")
if age<13:
    print("Значит вы младше меня")
print("привет я компютер")
name=input("как тебя зовут ")
print("Здравствуй "+name)
print("Тебе нужно угадать число от 1 до 10")
secret_number=random.randint(1,10)
tries=3
while True:
    print("Кол-во попыток "+str(tries))
    tries-=1
    number=int(input("Ваше число "))
    if secret_number==number:
        print("Вы выиграли в этой схватке")
        break
    if secret_number>number:
        print("Ваше число меньше чем загадонное")
    if secret_number<number:
        print("Ваше число больше чем загадонное")
    if tries==0:
        print("К сожелению Иван вы проиграли")
        break
