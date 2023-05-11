print("Здравствуйте")
print("Вам нужно угодать слово по буквам")
secret_word="слово"
user_letters=[]

while True:
    user_letter=input("Ваша буква ")
    user_letters.append(user_letter)
    if user_letter in secret_word:
        print("Вы отгадали букву,поздравляю")
    else:
        print("К сожелению ваша буква не присутствует в слове")
    for secret_letter in secret_word:
        if secret_letter in user_letters:
            print(secret_letter)
        else:
            print("*")
