from random import *

word_list = ['Москва', 'Рязань', 'Можайск', 'Омск', 'Владимир', 'Тверь', 'Углич', 'Тула', 'Руза', 'Воркута', 'Мурманск', 'Киров', 'Иркутск', 'Якутск', 'Красноярск', 'Хабаровск', 'Новосибирск']

#функция получения случайного слова
def get_word(arr):
    i = randint(0, len(arr)-1)
    return arr[i]

