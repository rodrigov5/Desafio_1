dmax = 0

entrada = input().split(" ") # 4 10.000
n_baterias = int(entrada[0])
dist = float(entrada[1])
bat_pos = []
bat_car = []

for i in range(n_baterias):
    entrada = input().split(" ")
    bat_pos.append(float(entrada[0]))
    bat_car.append(float(entrada[1]))

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

print("%.4f" % tot_tempo)