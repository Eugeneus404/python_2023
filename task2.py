string = input('Введите строку:')
message = ''

i = 0

for char in string:
    i+=1
    if (i == 3): 
        print("Третий символ пропущен")
        continue
    if (char == "с"): 
        message = ", есть символ С"    
    if (len(string) == i):
        print("Послений символ не выведен")
        continue    
    print("Символ "+ '%.0f' % i + ": " + char)
    
print("Длина строки: " + '%.0f' % len(string) + message)