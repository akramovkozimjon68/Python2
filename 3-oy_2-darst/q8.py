# list - royhat 

sonlar = [1, 2, 5, 7, 9, "salom"]

print(sonlar)
print(*sonlar)

#qo`shish

sonlar.append(4)
print(sonlar)

# o`chrish joylashgan o`rni

del sonlar[3]
print(sonlar)

# qiymat bo`yicha ochrish
sonlar.remove(4)
print(sonlar)

ismlar = []

ismlar.append("Ali")
ismlar.append('Kozimjon')


#elemerni berilgan index bo`yicha joylash
isimlar.insert(0, "Muhamadjon")
print(ismlar)
