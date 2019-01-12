#  5. Пользователь вводит две буквы.
#  Определить, на каких местах алфавита они стоят и сколько между ними находится букв.


def place_rus(b):
    if b <= 6 + 1071:
        return b - 1071  # а-е
    elif b == 1105:
        return 7  # ё
    else:
        return b - 1070  # ж-я


choice = input('Выберите алфавит: 1 - русский, 2 - латинский --> ')
if choice == '1':

    b1, b2 = input('Введите буквы в русском алфавите, от а до я, подряд без разделителей: ')
    ord_b1 = ord(b1)
    ord_b2 = ord(b2)

    if (1072 > ord_b1 or ord_b1 == 1104 or ord_b1 > 1105) or \
       (1072 > ord_b2 or ord_b2 == 1104 or ord_b2 > 1105):
        print('Обе буквы должны быть в диапазоне от а до я включительно')
        exit()

    place_b1 = place_rus(ord_b1)
    place_b2 = place_rus(ord_b2)
    print(f'Буква {b1} стоит на {place_b1}-м месте, {b2} - на {place_b2}-м,'
          f' между ними {abs(place_b2 - place_b1) - 1} букв')

elif choice == '2':

    b1, b2 = input('Введите буквы в латинском алфавите, от a до z, подряд без разделителей: ')
    ord_b1 = ord(b1)
    ord_b2 = ord(b2)

    if (97 > ord_b1 or ord_b1 > 122) or \
       (97 > ord_b2 or ord_b2 > 122):
        print('Обе буквы должны быть в диапазоне от a до z включительно')
        exit()

    place_b1 = ord_b1 - 96
    place_b2 = ord_b2 - 96
    print(f'Буква {b1} стоит на {place_b1}-м месте, {b2} - на {place_b2}-м,'
          f' между ними {abs(place_b2 - place_b1) - 1} букв')

else:
    print('Введен неверный вариант, не 1 и не 2')
