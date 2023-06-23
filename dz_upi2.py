data_list = []

while True:
    fio = input("Введите ФИО преподавателя (для выхода введите 'q'): ")
    if fio == 'q':
        break
    predmet = input("Введите название предмета: ")
    otsenka = input("Введите оценку: ")
    data_zacheta = input("Введите дату зачёта: ")

    data_list.append({'ФИО': fio, 'Предмет': predmet, 'Оценка': otsenka, 'Дата зачёта': data_zacheta})

    print("Данные успешно добавлены в список.")


for data in data_list:
    print(data['ФИО'])

print("Сохраненные данные:")
print(data_list)