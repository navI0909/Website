print("Здравствуйте люди")
phone=input("Какой марки ваш телефон ")
if phone=="Xiaomi":
    print("У меня точно такой же марки телефон")
print("Правила:")
print("Нужно называть слова с одинаковыми буквами которые заканчиваются на любую букву и начинать на оконченную букву того слова")
words=["рубль","юань","биткоин"]
print("Эти слова нельзя использовать")
print(*words)

while True:
    word=input("Ваше слово ")
    if word in words:
        print("Вы проиграли,это слово уже присутствуют в списке")
        break
    else:
        words.append(word)
        
