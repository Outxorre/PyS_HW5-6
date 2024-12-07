result = []

def divider(a, b):
    if a < b:
        raise ValueError("a меньше b")
    if b > 100:
        raise IndexError("b больше 100")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, (): 15, 8: 4}

for key, value in data.items():
    try:
        res = divider(key, value)
        result.append(res)
    except (ValueError, IndexError, ZeroDivisionError, TypeError) as e:
        print(f"Проблема с ={key}, числом={value}: {e}")

print(result)


#Снова ошибка, и тут на помощь приходит.. ОНЛАЙН КОМПИЛЯТОР (Всё работает)