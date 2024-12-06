from functools import reduce

a, b, c, d, e = map(int, input("Introduce 5 valores separados por espacio: ").split())
elementos=[a, b, c, d, e]
print("Tus valores: ", elementos)
promedio=sum(elementos) / len(elementos)
print("su promedio: ", promedio)
mediana=elementos[2]
print("su mediana: ",mediana)

izq_dre=reduce(lambda x, y: x * y, elementos)
p_multiplicativo=izq_dre**(1/len(elementos))
print("su promedio multiplicativo: ",p_multiplicativo)
maxi=max(elementos)**min(elementos)
print("la potencia del mayor número elevado al menor número: ",max(elementos),"**",min(elementos),"=",maxi)
mini=min(elementos)**(1/3)
print("la raíz cúbica del menor número: ",min(elementos),"**(1/3) =",mini)
