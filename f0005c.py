els_sz1 = 2
mas_sz2 = 3

eredmény = els_sz1 + mas_sz2
tipp = input('Mennyi'+ str(els_sz1) + '+' + str(mas_sz2) + '?')
tipp = int(tipp)
if tipp == eredmény:
  print('Na menjél...')
else:
  print('Ez nem jó...')