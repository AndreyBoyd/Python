# считываем файл и меняем английские числительные на русские, результат записываем в новый файл

translator = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open("text_4.txt", "r", encoding="utf-8") as my_file:
    for i in my_file:
        i = i.split(' ', 1)
        new_file.append(translator[i[0]] + '  ' + i[1])
    print(new_file)  # для наглядности выводим полученный список

with open('text_4_new.txt', 'w', encoding="utf-8") as my_file_new:
    my_file_new.writelines(new_file)
