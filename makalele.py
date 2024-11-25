# Exercice 2 :
# L’implémentation en python de l’algorithme BFS
visited = []
queue = []
def bfs(visited, graph, node):
 visited.append(node)
 queue.append(node)
 while queue:
 m = queue.pop(0)
 print (m, est = " ")
 for neighbour in graph[m]:
 if neighbour not in visited:
 visited.append(neighbour)
 queue.append(neighbour)
# Ecrire l'implémentation en python de l’algorithme DFS
visited = set()
def dfs(visited, graph, node):
 if node not in visited:
 print (node)
 visited.add(node)
 for neighbour in graph[node]:
 dfs(visited, graph, neighbour)
# Exercice 3 :
# Ecrire le code pour comparer 2 agents, en termes de complexité de temps, où le 1er agent
# utilise l’algorithme BFS et le 2eme agent déploie le DFS.
# Le graphe a utilisé :
# graphe = {'5' : ['3','7'], '3' : ['2', '4'], '7' : ['8'], '2' : [], '4' : ['8'], '8' : []}
# Le corrigé :
import time
import mesa
class Agent_A(mesa.Agent):
 def __init__(self,ID,model):
 super().__init__(ID,model)
 self.graph = self.model.graphe
 self.node = self.model.start
 self.goal = self.model.end
 def BFS(self,graphe,node,goal):
 visited = []
 file = []
 file.append(node)
 visited.append(node)
 while file:
 m = file.pop(0)
 print(m)
 if m == goal:
 return 1
 for n in graphe[m]:
 if n not in visited:
 file.append(n)
visited.append(n)
 return 0
 def step(self):
 start_time = time.perf_counter()
 self.BFS(self.graph,self.node,self.goal)
 end_time = time.perf_counter()
 execution_time = end_time - start_time
 print(f" BFS est {execution_time}")
class Agent_B(mesa.Agent):
 def __init__(self, ID, model):
 super().__init__(ID, model)
 self.graph = self.model.graphe
 self.node = self.model.start
 self.goal = self.model.end
 self.visited = set()
 self.end_time = 0
 def DFS(self, graphe, node, goal,visited):
 if node not in visited:
 visited.add(node)
 if node==goal:
 self.end_time = time.perf_counter()
 for n in graphe[node]:
 self.DFS(graphe, n, goal, visited)
 def step(self):
 start_time = time.perf_counter()
 self.DFS(self.graph, self.node, self.goal,self.visited)
 execution_time = self.end_time - start_time
 print(f" DFS est {execution_time}")
class Environnement(mesa.Model):
 def __init__(self):
 super().__init__()
 self.graphe = {'5' : ['3','7'],
 '3' : ['2', '4'],
 '7' : ['8'],
 '2' : [],
'4' : ['8'],
 '8' : []}
 self.start = '5'
 self.end = '8'
 self.A = Agent_A(0,self)
 self.B = Agent_B(1,self)
 self.plan = mesa.time.SimultaneousActivation(self)
 self.plan.add(self.A)
 self.plan.add(self.B)
 def step(self):
 self.plan.step()
model = Environnement()
model.step()

# Exercice 1 :
# Soit un environnement contenant deux agent A et B :
#  Ecrire le code de la classe Agent_A ou l’agent A demande à l’agent B de changer sa position
#  Ecrire le code de la classe Agent_B qui calcule sa décision en utilisant l’équation x
# 2 + log(y3
# ), ou x et
# y sont l’abscisse et l’ordonné de l’agent (rendus d’une manière aléatoire), et lui répond selon la parité
# du résultat (OK ! si pair, NO ! sinon)
#  Ecrire le code la classe Environnement qu’utilise la planification simultanée des agents
#  Lancer votre environnement
# Corrigé:
import random
import mesa
import numpy as np
class Agent_A(mesa.Agent):
 def __init__(self, ID, model):
 super().__init__(ID, model)
 def step(self):
 # autre = self.model.plan.agents[1]
 autre = self.random.choice(self.model.plan.agents)
 while autre.unique_id != 1:
 autre = self.random.choice(self.model.plan.agents)
 print("Merci de changer votre position")
class Agent_B(mesa.Agent):
 def __init__(self, ID, model):
 super().__init__(ID, model)
 self.x = random.randint(1, 10)
 self.y = random.randint(1, 10)
 def step(self):
 self.x = random.randint(1, 10)
 self.y = random.randint(1, 10)
 resultat = pow(self.x, 2) + np.log(pow(self.y, 3))
 if int(resultat) % 2:
 print("Ok!")
 else:
 print("NO!")
class Environnement(mesa.Model):
 def __init__(self):
 super().__init__()
 A = Agent_A(0, self)
 B = Agent_B(1, self)
 self.plan = mesa.time.BaseScheduler(self)
 self.plan.add(A)
 self.plan.add(B)
 def step(self):
 self.plan.step()
model = Environnement()
while True:
 model.step()

# Exercice 2 :
# Soit un environnement contenant deux agents rationnels, chacun a un durée de fonctionnement d'une manière
# séquentielle (le 1er agent entre et fait son travail et sort pour céder le reste du travaille au 2
# eme agent).
#  Le 1
# er agent travaille pour 8 heures et effectue un calcul (incrémente une variable i par 1)
#  Le 2
# eme agent fonctionne pour une durée de 9 heures et incrémente la dernière valeur calculée, par
# l'agent, par 1
# Corrigé:
import mesa
class Agent_A(mesa.Agent):
 def __init__(self,ID,model):
 super().__init__(ID,model)
 def step(self):
 self.model.i += 1
class Agent_B(mesa.Agent):
 def __init__(self, ID, model):
 super().__init__(ID, model)
 def step(self):
 self.model.i += 2
class Environnement(mesa.Model):
 def __init__(self):
 super().__init__()
 self.i = 0
 self.A = Agent_A(0,self)
 self.B = Agent_B(1,self)
 self.plan = mesa.time.BaseScheduler(self)
 self.plan.add(self.A)
 self.count = 0
 def step(self):
 self.count += 1
 self.plan.step()
 if self.count==8:
 self.plan.remove(self.A)
 self.plan.add(self.B)
 if self.count == 17:
 self.plan.remove(self.B)
 print(self.i)
model = Environnement()
for j in range(17):
 model.step()
 
#  Meilleur d’abord glouton :
nombre_noeuds = 6
graphe = [[] for i in range(nombre_noeuds)]
def fct(x,y,cout):
 graphe[x].append((y,cout))
 graphe[y].append((x, cout))
fct(0,1,7)
fct(0,2,2)
fct(1,3,4)
fct(1,4,3)
fct(2,5,0)
fct(4,5,0)
print(graphe)
from queue import PriorityQueue
liste = [5,3,7,2,4,8]
def best_first(graphe,node,goal,n):
 visited = [False]*n
 visited[node] = True
 p_queue = PriorityQueue()
 p_queue.put((0,node))
 while p_queue.empty() == False:
 m = p_queue.get()[1]
 print(liste[m])
 if m == goal:
 return 1
 for n,c in graphe[m]:
 if visited[n] == False:
 visited[n] = True
 p_queue.put((c,n))
 return 0
print("%d"%best_first(graphe,0,5,6))