secund = int(input("Sekund: "))

soat = secund // 3600

secund = secund % 3600

daqiqa = secund // 60

secund = secund % 60

print(f"soatg: {soat}\nminut: {daqiqa}\nminut: {secund}")
