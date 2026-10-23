numbers = [10, 45, 23, 78, 56, 78, 100, 12,101]

engKatta = numbers[0]

for son in numbers:
    if son > engKatta:
        engKatta ,ikkinchiKatta = son,engKatta
    
    if son < engKatta and son > ikkinchiKatta:
        ikkinchiKatta = son

print(ikkinchiKatta)
