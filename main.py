A = int(input('Введите ваш возраст '))
p=0
n=0
while A >= 0:
    if  A in range(6):  
        p=p+1
    elif A in range(6,19):
        ans=str(input("Студак есть? "))
        if ans == 'da':
            n=n+100 * 0.8
            print("Итог: ",n)
        else:
            n=n+100
            print("Итог: ",n)
    else:
        ans=str(input("Студак есть? "))
        if ans == 'da':
            n=n+150 * 0.8
            print("Итог: ",n)
        else:
            n=n+150
            print("Итог: ",n)
    A = int(input('Введите ваш возраст '))
    if A == 'stop':
        break
print("Конечный Итог: ",n)
