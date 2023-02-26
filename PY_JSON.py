import json

#Создать список и сделать Json объект

nums = [3,4,6,7,86,4,45,67,564,55]
"""
filename = 'nums.json'

with open(filename, 'w') as file:
    #Для создания JSON строки
    json.dump(nums, file)
"""
"""
filename = 'nums.json'
with open(filename) as file:
    # Для чтения JSON строки
    nums_new = json.load(file)
print(nums_new)
"""

"""
Считает данные введеные пользователем
Если он есть приветствует
иначе записывает
"""

def get_username():
    """Получает имя пользователя если оно есть"""
    filename = 'user.json'
    try:
        with open(filename) as file:
            # Для чтения JSON строки
            user = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return user

def greet_user():

    """Приветствие пользователя"""
    username = get_username()
    if username:
        print("Hello " + username)
    else:
        username = input("Введите ваше имя: ")
        filename = 'user.json'

        with open(filename, 'w', encoding="utf-8") as file:
            #Для создания JSON строки и отключение ASCII
            json.dump(username, file, ensure_ascii=False)
            print("Мы вас запомнили: "+ username)

greet_user()