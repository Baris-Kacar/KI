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
] )
class Queue:
   
   def __init__(self, n):
      self.arrSize = n
      self.lifo = [] #array erstellen
      self.fifo = [] 
      self.prio = []

   def pop(self, fifo, lifo, prio):
      emptyQueue = self.empty()
      if not emptyQueue["fifo"]:
         if fifo != 0:
            fifoNode = self.fifo[0]
            del self.fifo[0]
            return fifoNode
      if not emptyQueue["lifo"]:
         if lifo != 0:
            lifoNode = self.lifo[-1]
            del self.lifo[-1]
            return lifoNode
      if not emptyQueue["prio"]:
         if prio != 0:
            prioNode = self.prio[-1]
            del self.prio[-1]
            return prioNode

   def insert(self, fifo, lifo, prio, node):
      emptyQueue = self.empty()

      if fifo != 0:
         if emptyQueue["fifo"] == False and len(self.fifo) == self.arrSize: #array voll
            self.fifo.append(node)
            self.pop(1,0,0)
         else: # array leer
            self.fifo.append(node)
      
      if lifo != 0:
         if emptyQueue["lifo"] == False and len(self.lifo) == self.arrSize: # array voll
            self.lifo.append(node)
            self.pop(0,1,0)
         else:
            self.lifo.append(node)
      
      if prio != 0:
         if emptyQueue['prio'] == False and len(self.prio) == self.arrSize: # array voll
            j = len(self.prio) - 1
            while j >= 0:
               self.prio[j-1] = self.prio[j]
               j -= 1
            self.pop(0,0,1)
            self.prio.insert(0,node)
         else:
            self.prio.insert(0,node)
      
   def empty(self):
      fifoFull = False
      lifoFull = False
      prioFull = False

      if len(self.fifo) == 0:
         fifoFull = True
      if len(self.lifo) == 0:
         lifoFull = True
      if len(self.prio) == 0:
         prioFull = True

      return {"fifo":fifoFull,"lifo": lifoFull,"prio": prioFull}

# Folie 12
