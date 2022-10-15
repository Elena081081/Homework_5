# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

def del_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return ' '.join(text)

text = input('Введите исходный текст: ')
my_text = del_words(text)
print(f'Итоговый текст: {my_text}')

# Введите исходный текст: jgjgjg ;poiiu mvnvhvg абвmvnvnv hgjgjgаааббб абвабв mvmvmvmабв
# Итоговый текст: jgjgjg ;poiiu mvnvhvg hgjgjgаааббб