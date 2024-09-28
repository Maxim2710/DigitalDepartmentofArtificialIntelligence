swims, has_wings, has_long_neck = input().split()

if swims == "Нет":
    if has_wings == "Нет":
        if has_long_neck == "Нет":
            print("Кот")
        else:
            print("Жираф")
    else:
        if has_long_neck == "Нет":
            print("Курица")
        else:
            print("Страус")
else:
    if has_wings == "Нет":
        if has_long_neck == "Нет":
            print("Дельфин")
        else:
            print("Плезиозавры")
    else:
        if has_long_neck == "Нет":
            print("Пингвин")
        else:
            print("Утка")
