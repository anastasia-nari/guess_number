from random import randint

number = randint(1, 100)
print('Угадайте число от 1 до 100')

while True:
  guess = int(input('Ваше число:'))
  
  if guess < number:
    print ('Ваше число меньше того, что загадоно.')
  if guess > number:
    print ('Ваше число больше того, что загадоно.')
  if guess == number:
    break
print("Вы отгадали число!")
  

