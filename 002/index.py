n1 = 3

result_km = n1 / 1000
result_hm = n1 / 100
result_dam = n1 / 10
result_dm = n1 * 10
result_cm = n1 * 100
result_mm = n1 * 1000

print('A medida de {:.1f}m corresponde a \n {:.3f}km \n {:.2f}hm \n {:.1f}dam \n {}dm \n {}cm \n {}mm'.format(n1, result_km, result_hm, result_dam, result_dm, result_cm, result_mm))