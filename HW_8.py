##Третья домашка по регулярным выражениям.
##Сдать эту домашку нужно до 18 января 23:59.
##
##Вам нужно сохранить у себя на компьютере  статьи из Википедии, указанные в
##задании. Файл, естественно, должен быть в UTF-8. Программа должна читать
##этот файл и заменять в нём все формы слова A на соответствующие формы слова
##B (слова A и B тоже указаны в задании для Вашего варианта). То, что получится,
##она должна записывать в другой текстовый файл. Все входные и выходные файлы
##сохраните в своем репозитории с кодом.
##Заменяться должны только формы этого слова. Т. е. если Вам нужно заменить
##слово "кит" на слово "кот", слово "китовый" на слово "котовый" заменяться
##не должно. При замене нужно пользоваться функцией re.sub. Если слово было
##написано с большой буквы, то и после замены оно должно быть написано с
##большой буквы.
##
##Вот конкретные статьи и слова для замены:
##1. статья "комар", заменить "комар" на "слон";
##2. статья "викинги", заменить "викинг" на "бурундук";
##3. статья "лингвистика", заменить "язык" на "шашлык";

import re
import os
def path(n): #вместо n надо написать название текста, с которым работаем
    path = os.path.join(os.path.dirname(__file__), n)
    f = open(path, encoding = "UTF-8")
    text = f.read()
    f.close()
    return text
 
def reg(n): #вместо n может быть слово, которое мы собираемся искать в тексте
    reg ='^'+'('+n[0]+'|'+n[0].capitalize()+')'+n[1:]+'(а|у|ом|е|ы|ов|ам|ами|ах|)'  
    return reg

def text_mosquito():
    text = path('Mosquito.txt') 
    main_list = text.split() 
    for i, let in enumerate(main_list):
        if re.search(reg('комар'), let): #вместо "комар" может быть написано "викинг" или "язык"
            main_list[i] = re.sub('Комар', 'Слон', main_list[i])
            main_list[i] = re.sub('комар', 'слон', main_list[i])
    main_text = ' '.join(main_list)       
    return main_text

def text_vikings():
    text = path('Vikings.txt') 
    main_list = text.split() 
    for i, let in enumerate(main_list):
        if re.search(reg('викинг'), let): 
            main_list[i] = re.sub('Викинг', 'Бурундук', main_list[i])
            main_list[i] = re.sub('викинг', 'бурундук', main_list[i])
    main_text = ' '.join(main_list)       
    return main_text

def text_linguistics():
    text = path('Linguistics.txt') 
    main_list = text.split() 
    for i, let in enumerate(main_list):
        if re.search(reg('язык'), let): 
            main_list[i] = re.sub('Язык', 'Шашлык', main_list[i])
            main_list[i] = re.sub('язык', 'шашлык', main_list[i])
    main_text = ' '.join(main_list)       
    return main_text

def main():
    slon = text_mosquito()
    burunduk = text_vikings()
    shashlyk = text_linguistics()
    slon_file = open("./Slon.txt", "w", encoding="utf-8")
    burunduk_file = open("./Burunduk.txt", "w", encoding="utf-8")
    shashlyk_file = open("./Shashlyk.txt", "w", encoding="utf-8")
    slon_file.write(slon)
    slon_file.close()
    burunduk_file.write(burunduk)
    burunduk_file.close()
    shashlyk_file.write(shashlyk)
    shashlyk_file.close()

if __name__ == "__main__":
    main()

