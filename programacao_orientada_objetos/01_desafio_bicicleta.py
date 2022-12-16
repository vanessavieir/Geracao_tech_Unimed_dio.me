# from distutils import core
# from pyparsing import anyOpenTag

# from sklearn import model_selection


# class bicicleta:
    
#     def __init__(self,cor,modelo,ano,valor):
#         self.cor=cor
#         self.modelo=modelo
#         self.ano=ano
#         self.valor=valor


salario = int(input()) 
Novo_salario=0
reajuste=0
percentual=0

def calculo_salario(Novo_salario,reajuste):
    Novo_salario=salario

if (salario>=0 and salario<=600.00 ):
  
    
elif (salario>600.01 and salario<=900.00):
        
        
elif (salario>900.00 and salario<=1500):
  
    
elif (salario>1500.01 and salario<=2000):
   
   
else: 
    reajuste=(salario*0.5)
    

print(f"Novo salario:{int(lucro)}")
print(f"Reajuste ganho:{reajuste}")
print(f'Em percentual:{int(percentual)}%')
