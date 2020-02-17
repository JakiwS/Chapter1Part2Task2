students = int(input('Введите количество студентов '))
apples = int(input('Введите количество яблок '))
handed = apples // students
basket = apples % students
print ('Яблок у каждого студента', + handed)
print ('Осталось в корзине яблок', + basket)