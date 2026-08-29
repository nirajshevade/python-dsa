word = "Niraj"

sp = word.lower().split()
print(sp)

kp = list(word.lower())
print(kp)

str = "Niraj is here"

print(str.casefold())
print(str.find('j'))
print(str.index('j'))
print(str.count('e'))
print(str.startswith('N'))
print(str.isalpha())
print(str.strip())
print(str.replace('is' , 'was'))
print(str.split())