dmax = 0

n_baterias = int(input("Qual é a quantidade de baterias? "))
dist = float(input("Qual é o comprimento do circuito? "))

bat_pos = []
bat_car = []
for i in range(n_baterias):
    bat_pos.append(float(input(f"Qual a posição da bateria {i + 1}: ")))
    bat_car.append(float(input(f"Qual a carga da bateria {i + 1}: ")))

bat_pos.append(dist)

tempo = 0
aux_tempo = 0

pivo_pos = 0
pivo_tempo = 0
tot_tempo = 0

def calcTime(pos_init, pos_end, carga):
    diff_pos = pos_end - pos_init
    velocity = carga / diff_pos
    return diff_pos / velocity

for i in range(n_baterias):
    tempo = calcTime(bat_pos[i], bat_pos[i+1], bat_car[i])
    aux_tempo = calcTime(bat_pos[pivo_pos], bat_pos[i+1], bat_car[pivo_pos])

    if tempo <= aux_tempo: 
        pivo_pos = i
    else:
        pivo_tempo = aux_tempo

    if tempo <= aux_tempo or i == n_baterias-1:
        tot_tempo += pivo_tempo
        pivo_tempo = tempo

print(f"O tempo minimo possível para o carinho chegar ao final da pista é: {tot_tempo:.3f}")