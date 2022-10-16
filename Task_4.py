# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример: aaaaaaabbbbbbcccccccccd = > 7a6b9c1d
# или 11a3b7c1d = > aaaaaaaaaaabbbcccccccd

with open('file_4_1.txt', 'r') as data:
    my_text1 = data.read()

def encode(text1):
    str_code = ''
    count = 1
    for i in range(len(text1) - 1):
        if text1[i] == text1[i+1]:
          count += 1
        else:
            str_code = str_code + str(count) + text1[i]
            count = 1
    if count > 1 or (text1[len(text1) - 2] != text1[-1]):
        str_code = str_code + str(count) + text1[-1]
    return str_code

str_code = encode(my_text1)
print(f'Сжатие данных: {str_code}')

with open('file_4_2.txt', 'r') as data:
    my_text2 = data.read()

def decode(text2):
    str_decode = ''
    count = ''
    for i in text2:
        if i.isdigit():
            count += i
        else:
            str_decode = str_decode + i * int(count)
            count = ''
    return str_decode

str_decode = decode(my_text2)
print(f'Восстановление данных: {str_decode}')
