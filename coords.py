import matplotlib.pyplot as plt
import numpy as np

nom_arxius = ["trajectoria_cos2.txt", "trajectoria_pulsos.txt"]
for arxiu in nom_arxius:
    #Carregar dades de l'arxiu
    coords = np.loadtxt(arxiu)

    # Extreure les columnes amb cada valor de t,x,y,z
    frames = coords[:, 0]
    x = coords[:, 1]
    y = coords[:, 2]
    z = coords[:, 3]

    #Graficar Z vs Frame
    plt.plot(frames, z, label='Z')
    plt.xlabel("Frame (#)")
    plt.ylabel("Z (Ang)")
    plt.title("Trajectoria en z vs Frame per a " + arxiu)
    plt.show()

    dt = []
    dz = []
    
    #1a derivada (Velocitat en z)
    i=0
    imax=len(x)-1
    while i<imax:
        difft=frames[i+1]-frames[i]
        diffz=z[i+1]-z[i]
        dz.append(diffz/difft)
        dt.append(frames[i])
        i=i+1


    dt2 = []
    dz2 = []
    
    #2a derivada (Acceleració en z)
    j=0
    jmax=len(dt)-1
    while j<jmax:
        difft2=dt[j+1]-dt[j]
        diffz2=dz[j+1]-dz[j]
        dz2.append(diffz2/difft2)
        dt2.append(frames[j])
        j=j+1
    #Graficar v_z vs Frame
    plt.plot(dt, dz)
    plt.xlabel("Frame (#)")
    plt.ylabel("df/dx (Ang/Frame)")
    plt.title("1a derivada de z vs Frame per a " + arxiu)
    plt.show()
    #Graficar a_z vs Frame
    plt.plot(dt2, dz2)
    plt.xlabel("Frame (#)")
    plt.ylabel("df2/dx2 (Ang/Frame^2)")
    plt.title("2a derivada de z vs Frame per a " + arxiu)
    plt.show()

