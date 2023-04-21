from prettytable import PrettyTable
from utils import * 

class Node:

   def __init__(self, name):
       self.parent = 0
       self.name = name
       self.edges = []
       self.value = 0
     

class Edge:
   #self ist der Konstruktor
   def __init__(self, edge):
      self.start = edge[0]
      self.end = edge[1]
      self.value = edge[2]


class Graph:

   def __init__(self, node_list, edges):
      self.nodes = []
      for name in node_list:
         self.nodes.append(Node(name))

      for e in edges:
        e = (getNode(e[0],self.nodes), getNode(e[1], self.nodes), e[2])        

        self.nodes[next((i for i,v in enumerate(self.nodes) if v.name == e[0].name), -1)].edges.append(Edge(e))
        self.nodes[next((i for i,v in enumerate(self.nodes) if v.name == e[1].name), -1)].edges.append(Edge((e[1], e[0], e[2])))


   def print(self):
      node_list = self.nodes
      
      t = PrettyTable(['  '] +[i.name for i in node_list])
      for node in node_list:
         edge_values = ['X'] * len(node_list)
         for edge in node.edges:
            edge_values[ next((i for i,e in enumerate(node_list) if e.name == edge.end.name) , -1)] = edge.value           
         t.add_row([node.name] + edge_values)
      print(t)
                  
romania = Graph( ['Or', 'Ne', 'Ze', 'Ia', 'Ar', 'Si', 'Fa',
 'Va', 'Ri', 'Ti', 'Lu', 'Pi', 'Ur', 'Hi',
 'Me', 'Bu', 'Dr', 'Ef', 'Cr', 'Gi'],
[
   ('Or', 'Ze', 71), ('Or', 'Si', 151),
   ('Ne', 'Ia', 87), ('Ze', 'Ar', 75),
   ('Ia', 'Va', 92), ('Ar', 'Si', 140),
   ('Ar', 'Ti', 118), ('Si', 'Fa', 99),
   ('Si', 'Ri', 80), ('Fa', 'Bu', 211),
   ('Va', 'Ur', 142), ('Ri', 'Pi', 97),
   ('Ri', 'Cr', 146), ('Ti', 'Lu', 111),
   ('Lu', 'Me', 70), ('Me', 'Dr', 75),
   ('Dr', 'Cr', 120), ('Cr', 'Pi', 138),
   ('Pi', 'Bu', 101), ('Bu', 'Gi', 90),
   ('Bu', 'Ur', 85), ('Ur', 'Hi', 98),
   ('Hi', 'Ef', 86)
])

class Queue:
    procedure = 'lifo'
    structeredData = list()

    def __init__(self, procedure):
        if (procedure in {'lifo', 'fifo', 'prio'}):
            self.procedure = procedure
            self.structeredData = list()
        else:
            print("Invalid Constructor Parameter")

    def push(self, data):
      if (self.procedure == 'lifo'):
         self.structeredData.insert(0, data)
      elif (self.procedure == 'fifo'):
         self.structeredData.append(data)
      elif (self.procedure == 'prio'):
         total_cost, node = data
         index = 0
         while (index < len(self.structeredData) and int(self.structeredData[index][0]) < total_cost):
               index += 1
         if (index >= len(self.structeredData)):
               self.structeredData.append((total_cost, node))
         else:
               self.structeredData.insert(index, (total_cost, node))

    def pop(self):
        if (not self.structeredData):  # empty Queue
            print('Queue is empty!!')
            return None
        else:
            return self.structeredData.pop(0)

    def contains(self, value):
        for element in self.structeredData:
            if(value == element):
                return True
        return False
    
    def empty(self):
        return (not self.structeredData)

    def contains(self, val):
        return val in self.structeredData

    def print(self):
        for element in self.structeredData:
            print(element, end=' , ')
        print('')


#nachbarn aus der adjazenzmatrix entnehmen
def neighbors(node_name):
   map = []
   for node in romania.nodes:
      if(node.name == node_name):
         for edges in node.edges:
            map.append({
                  "from": edges.start.name,
                  "to": edges.end.name,
                  "cost": edges.value
                })
          
   return map

"""
liste = adj_matrix('Or')
for edge in liste:
        print(edge['cost'])
"""
# minimum total cost - takes the cheapest path

def ucs(start_node,end_node): 
    visited = set()
    queue = Queue('prio')
    start = getNode(start_node,romania.nodes)
    queue.push((0,start))
    paths = {start: [start]}
    while not queue.empty():
        r = queue.pop()
        cost = int(r[0])
        node = r[1]

        if node not in visited:
            visited.add(node)

            if node.name == end_node:
                return paths[node]
            n = neighbors(node.name)
            for neigh in n:
                toNode = getNode(neigh['to'], romania.nodes)
                if toNode not in visited:
                    total_cost = cost + int(neigh['cost'])
                    if toNode not in paths:
                        paths[toNode] = paths[node] + [toNode]
                    queue.push((total_cost,toNode))
   
    

def bfs(start_node, end_node):
    visited = []
    queue = Queue('fifo')
    start = getNode(start_node,romania.nodes)
    end = getNode(end_node,romania.nodes)
    queue.push(start)
    while not queue.empty():
        node = queue.pop()
        if node == end:
            visited.append(node)
            break
        if node not in visited:
            visited.append(node)
           #print(node.name)
            n = neighbors(node.name)
            for neighbour in n:
                neighbor_node = getNode(neighbour['to'], romania.nodes)
                if neighbor_node not in visited:
                    neighbor_node.parent = node
                    queue.push(neighbor_node)
    if end not in visited:
        print("Ziel nicht enthalten!")
        return []
    path = []
    node = end
    while node != start:
        path.insert(0, node)
        node = node.parent
    path.insert(0, start)
    return path            


def dfs(start_node, end_node, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()

    start = getNode(start_node, romania.nodes)
    
    path.append(start)
    visited.add(start)

    if start.name == end_node:
 
        return path
    n = neighbors(start.name)
    for neigh in n:
        new_neigh = getNode(neigh['to'],romania.nodes)
        if new_neigh not in visited:
            result = dfs(neigh['to'], end_node, path, visited)
            if result is not None:
                return result
    path.pop()
    return path





"""
bfs_test = bfs("Bu","Ti")
for t in bfs_test:
    print(t.name)

dfs_test = dfs("Bu", "Ti")

for t in dfs_test:
    print(t.name)
"""

"""
ucs_test = ucs("Bu", "Ti")
print(ucs_test)
for t in ucs_test:
    print(t.name)

"""
