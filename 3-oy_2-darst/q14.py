sonlar = [4, 5, 6, 7, 6, 9, 8]
yangi_sonlar = []

for son in sonlar:
    if  son in yangi_sonlar:
        print("Bor")
        
    else:
      yangi_sonlar.append(son)
    
print(yangi_sonlar)