# eng kotta va eng kchik

sonlar = [4, 5, 6, 7, 6, 9, 8]

katta = sonlar[0]
for son in sonlar:
    if katta < son:
        katta = son
        
print(f"katta: {katta}")