from pulp import LpMaximize,LpMinimize, LpProblem, LpStatus, lpSum, LpVariable

print("Informe a natureza do problema, se é minimização ou maximização.")
print("Maximização tecle 1 ou Minimização tecle 0.")

choice = int(input())

print("Informe os coeficientes da função objetivo. Primeiro de X e depois de Y.")
cx = int(input())
cy = int(input())

if choice == 0:
	model = LpProblem(name="small-problem", sense=LpMinimize)
else:
	model = LpProblem(name="small-problem", sense=LpMaximize)

#Limites de não negatividade
x = LpVariable(name="x", lowBound=0)
y = LpVariable(name="y", lowBound=0)

#Função objetivo
expression = cx* x + cy * y

#Adicionando a função objetivo ao modelo
model += expression

print("Informe o sinal da restrição 1, se é menor-igual ou  maior-igual.")
print("<= tecle 1 e >= tecle 0")
signal1 = int(input())

print("Informe os coeficientes da restrição 1:")
cx = int(input())
cy = int(input())
print("Informe o lado direito da restrição 1:")
right = int(input())
if signal1==1:
	constraint1 = cx * x + cy * y <= right
else:
	constraint1 = cx * x + cy * y >= right


print("Informe o sinal da restrição 2, se é menor-igual ou  maior-igual.")
print("<= tecle 1 e >= tecle 0")
signal2 = int(input())

print("Informe os coeficientes da restrição 2:")
cx = int(input())
cy = int(input())
print("Informe o lado direito da restrição 2:")
right = int(input())
if signal2==1:
	constraint2 = cx * x + cy * y <= right
else:
	constraint2 = cx * x + cy * y >= right
	
print("Informe o sinal da restrição 3, se é menor-igual ou  maior-igual.")
print("<= tecle 1 e >= tecle 0")
signal3 = int(input())

print("Informe os coeficientes da restrição 3:")
cx = int(input())
cy = int(input())
print("Informe o lado direito da restrição 3:")
right = int(input())
if signal3==1:
	constraint3 = cx * x + cy * y <= right
else:
	constraint3 = cx * x + cy * y >= right
		
#Adicionando as restrições no modelo.
model += (constraint1,"red_constraint")
model += (constraint2,"blue_constraint")
model += (constraint3,"green_constraint")

status = model.solve()

print(f"objective: {model.objective.value()}")

for var in model.variables():
  print(f"{var.name}: {var.value()}")
