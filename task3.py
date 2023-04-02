text = input("Введите текст: ")

longWord = max(text.split(), key=len)

d = {}
for i in text.split('\n'):
    for j in i.split():
        d[j] = d.get(j,0) + 1
        
mf = d [ max(d,key = lambda x : d[x]) ]

print("Самое длинное слово: " + longWord)
print("Наиболее встречающееся слово: ", end='')
print(*sorted([ x for x in d if d[x] == mf]),sep = '\n')