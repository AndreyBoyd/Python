# подсчитываем количество строк, слов и символов в заданном преподавателем файле text_6.txt

task1 = open("text_6.txt", "r", encoding="utf-8")
my_list = task1.readlines()
# для удобства проверки выводим список который мы будем считать (каждый элемент списка == строка файла)
print(f"Содержимое файла в виде списка с символами перевода строки:\n {my_list}\n")
task1.close()

with open("text_6.txt", encoding="utf-8") as text_6:
    lines = 0
    symbols = 0
    a = 0
    for line in text_6:
        lines += line.count("\n")
        string_to_count = my_list[a]
        string_to_count = string_to_count.split()
        words_count = len(string_to_count)
        print(f"количество слов (групп символов разделёных пробелами) в строке {a+1} = {words_count}")
        a = a + 1
        symbols = len(line)
        print(f"количество символов (с учётом символа перевода строки) в строке {a}  = {symbols}\n")
    print(f"Общее количество строк: {lines + 1}")
