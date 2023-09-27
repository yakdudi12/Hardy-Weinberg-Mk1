
from tabulate import tabulate

def variables():
    Indivduos = int(input("Ingrese el N° de Inviduos de la población:"))
    H_Dom = int(input("Ingrese El N° H_Dominantes:"))
    H_Het = int(input("Ingrese el N° HETEROCIGOTAS:"))
    H_Rec = int(input("Ingrese el N° H_Rec:"))
    Datos = [H_Dom, H_Het, H_Rec,Indivduos]
    Comprobac = H_Rec + H_Het + H_Dom
    if Indivduos == Comprobac:
        print("Los datos son coherentes")
    else:
        print("Los datos no concuerdan, revisar los números otorgados")
    return  Datos

Datos_pobla = variables()

#Calcular las Frecuencias genotípicas
AA_obs = Datos_pobla[0] / Datos_pobla[3]
Aa_obs = Datos_pobla[1] / Datos_pobla[3]
aa_obs = Datos_pobla[2] / Datos_pobla[3]

#Cálculo de Frecuencias Alélicas
def Frec_Alelicas():
    p = AA_obs + Aa_obs / 2
    q = aa_obs + Aa_obs / 2
    datos_FrAle = [p, q]
    if p + q == 1:
        print("Las Frecuencias alélicas son correctas")
    else:
        print("Las Frecuencias alélicas son incorrectas")
    print("El valor p es:", p)
    print("El valor q es:", q)
    return datos_FrAle

Fr_Ale = Frec_Alelicas()

#Cálculo de las Frecuencias genotípicas Esperadas
AA_esp = Fr_Ale[0] ** 2
Aa_esp = Fr_Ale[0] * Fr_Ale[1] * 2
aa_esp = Fr_Ale[1] ** 2
print("Las Frecuencias genotípicas esperadas son:", AA_obs,Aa_esp,aa_esp)

#Frecuencias genotípicas Esperadas en proporción poblacional
def Fresp_Poblacion():
    poblacion_1 = Datos_pobla[3] / 100
    AA_esp_1 = AA_esp * 100
    Aa_esp_1 = Aa_esp * 100
    aa_esp_1 = aa_esp * 100
    HD_pob = round(AA_esp_1 * poblacion_1)
    HET_pob = round(Aa_esp_1 * poblacion_1)
    HR_pob = round(aa_esp_1 * poblacion_1)
    Datos_esp = [HD_pob, HET_pob, HR_pob]
    return Datos_esp

Fr_gen_esp = Fresp_Poblacion()
print("Número de Individuos Esp (AA,Aa,aa)", Fr_gen_esp)

#Chi-Cuadrado sin importar más librerias
def chi_cuadrado():
    x2_AA = ((Datos_pobla[0] - Fr_gen_esp[0]) ** 2) / Fr_gen_esp[0]
    x2_Aa = ((Datos_pobla[1] - Fr_gen_esp[1]) ** 2) / Fr_gen_esp[1]
    x2_aa = ((Datos_pobla[2] - Fr_gen_esp[2]) ** 2) / Fr_gen_esp[2]
    Sumatoria = x2_AA + x2_Aa + x2_aa
    print("Chi-Square (AA,Aa,aa)", x2_AA, x2_Aa, x2_aa)
    print("Sumatoria:", Sumatoria)

    #Veredicto:
    Valor_p = 3.84
    if Sumatoria <= Valor_p:
        print("La población está en equilibrio de Hardy-Weinberg (p-valor = 3.84; confianza 0.05%)")
    else:
        print("La población No se encuentra en Equilibrio de Hardy-Weinberg (p-valor = 3.84; confianza 0.05%)")

chi_cuadrado()