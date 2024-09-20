print("Actividad 9 Clases Version 3")
print("Andres Rivera Mat: 22308051281295")

#zona de clase
class Operadores0777:
    #zona de funciones
    def suma0777(self,E,N):
        s0777 = E + N
        print(f"La suma de {E} + {N} = {s0777}")
    def resta0777(self,A,B):
        r0777 = A - B
        print(f"La resta de {A} - {B} = {r0777}")
    def multi0777(self,C,D):
        m0777 = C * D
        print(f"El producto de {C} * {D} = {m0777}")
    def div0777(self,F,G):
        d0777 = F / G
        print(f"El resultado de {F} / {G} = {d0777}")
    def mod0777(self,J,K):
        md0777 = J % K
        print(f"El residuo de {J} % {K} = {md0777}")
    def exp0777(self,L,M):
        e0777 = L ** M
        print(f"El producto de {L} ** {M} = {e0777}")
    def coc0777(self,O,P):
        c0777 = O // P
        print(f"El cociente de {O} // {P} = {c0777}")        
#zona de creacion del objeto
operarivera=Operadores0777()

#zona de uso de objetos
print("Funcion suma")
operarivera.suma0777(5,4)
print("Funcion Resta")
operarivera.resta0777(6,2)
print("Funcion Multiplicacion")
operarivera.multi0777(8,4)
print("Funcion Division")
operarivera.div0777(10,3)
print("Funcion Modulo")
operarivera.mod0777(9,2)
print("Funcion Exponente")
operarivera.exp0777(10,3)
print("Funcion Cociente")
operarivera.coc0777(10,3)