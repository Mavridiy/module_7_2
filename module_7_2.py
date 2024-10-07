def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for index_line, string in enumerate(strings, start=1):  # Получаем текущую позицию в файле (байт начала строки)
            byte_position = file.tell()  # Записываем строку в файл
            file.write(string + '\n')  # Добавляем запись в словарь
            strings_positions[(index_line, byte_position)] = string

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
