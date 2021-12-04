contaSegundos = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs = int(contaSegundos)
a = total_segs // 86400
segs_restantes_1 = total_segs % 86400
b = segs_restantes_1 // 3600
segs_restantes_2 = total_segs % 3600
c = segs_restantes_2 // 60
segs_restantes_final = segs_restantes_2 % 60
d = segs_restantes_final
print(a, "dias,", b, "horas,", c, "minutos e", d, "segundos")