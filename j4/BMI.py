w = float(input('inter weight (kg):'))
h = float(input('enter hright (cm):'))
c = ((w) / (h * h * 0.01 * 0.01))
if c < 18.5:
    print('bmi =' ,c,'/ thin' )
elif c >= 18.5 and c <= 24.9:
    print('bmi =' ,c,'/ normal')
elif c >= 25 and c <= 29.9:
    print('bmi =' ,c, ' / befor obesity')
elif c >=30 and c <= 34.9:
    print('bmi =' ,c,'/ fat' )
elif c >= 35:
    print('bmi =',c,'/ you got fat')