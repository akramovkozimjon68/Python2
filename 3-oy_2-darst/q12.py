sonlar = [4, 5, 6, 7, 6, 9, 8]
juftlar = []

for son in sonlar:
    if son % 2 == 0:
        juftlar.append(son)
        
print(f"Juft sonlar: {juftlar}")