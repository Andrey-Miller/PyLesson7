# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.

print("Введи рифму: ")
#input = 'пара-ра-рам рам-пам-папам па-ра-па-да'.split()
input = input().split()
check = [sum(x in 'АИОУЫЕЕЁЮЯаиоуыеёюя' for x in i) for i in input] #получим список из кол-ва гласных в каждом слове

# если len(set(check)) == 1, значит в получанном списке(например [4, 4, 4]) кол-во гласных во всех словах было одианоковым, 
# если кол-во где-то не совпадало(например [4, 4, 5]), то len(set(check)) !=1  
answer = lambda x: "Парам пам-пам" if x==1 else "Пам парам"

print(answer(len(set(check))))

