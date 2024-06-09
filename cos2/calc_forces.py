import numpy as np

def tsimul(arxiu): #Abans de simular cal crear un arxiu que l'unic que tingui escrit és un 0
    with open(arxiu, "r") as r: #Cada vegada que NAMD vulgui calcular forçes, pensa obrir l'arxiu
        t0 = float(r.readlines()[0]) #Llegir el valor de temps anterior
    t = t0 +1e-3 #L'hi suma dt per a indicar que estem al següent pas de temps
    with open(arxiu, "w") as w: #Ara obrim l'arxiu anterior i el tornem a escriure de 0
        w.write(str(t)) #Pero ara escribim el nou valor de temps
    return t #I obtenim el valor de temps actual amb el que volem simular la F

def calcular_forces(coords,t):
    max_z = max(atom[3] for atom in coords)
    min_z = min(atom[3] for atom in coords)
    forces = []
    for atom in coords:
        if atom[0] >=577 and atom[0]<=2160: #Si l'atom forma part d'un aigua s'applica força, si no es aigua, no aplicar força
            fx = 0.0
            fy = 0.0
            #Aplicar una força en Z que depen del temps, però té un factor multiplicador que fa que com més lluny esta la molecula menys F nota
            #Quan Z atom és el valor minim, el factor és 1, quan el valor de Z és màx, el factor és 0
            fz = -(max_z - atom[3])/(max_z-min_z)*np.cos(2*np.pi*t/50)**2   # Kcal/mol/A ( 1 Kcal/mol/A = 69.493 pN)
            forces.append([atom[0], 1, fx, fy, fz])  # atomid,si posem 1 reemplaça la F anterior i escriu l'actual , fx, fy, fz
        else:
            fx = 0.0
            fy = 0.0
            fz = 0.0
            forces.append([atom[0], 1, fx, fy, fz])
    return forces

def llegir_coords(arxiu):
    with open(arxiu, 'r') as r:
        lines = r.readlines()
    coords = []
    for line in lines[:-3]:  #Triar linies que ens interesen
        parts = line.split()
        atomid = int(parts[0])
        x, y, z = float(parts[2]), float(parts[3]), float(parts[4])
        coords.append([atomid, x, y, z])
    return coords

def arxiu_forces(arxiu, forces):
    with open(arxiu, 'w') as w:
        for force in forces:
            w.write(f"{force[0]} {force[1]} {force[2]} {force[3]} {force[4]}\n") #force[0] = atomID, force[1] = replace force[2,3,4] = fx,fy,fz
        w.write("0.0\n")  # Energía d'interacció

t = tsimul("tmp/temps.dat")
coords = llegir_coords("tmp/coords.dat")
forces = calcular_forces(coords,t)
arxiu_forces("tmp/forces.dat",forces)

