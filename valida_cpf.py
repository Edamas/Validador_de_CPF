import numpy as np
cpf = [int(n) for n in input('Digite um CPF: ') if n.isnumeric()]
try:	valido = [len(cpf) , 		(sum(np.multiply(np.arange(10,1,-1),		cpf[0:-2])) * 10) % 11,		(sum(np.multiply(np.arange(11,1,-1),		cpf[0:-1])) * 10) % 11] == [11, 									cpf[-2],									cpf[-1]] and len(set(cpf)) != 1
except:	valido = False
print('CPF válido: ', valido)
