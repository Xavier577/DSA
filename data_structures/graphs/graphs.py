# E = {(a,b) , (a,d) , (c,b), (c,f), (d,b), (e,c),  (f,e) }
import json
edges = [('a', 'b'), ('a', 'd'), ('c', 'b'), ('c', 'f'), ('d', 'b'), ('e', 'c'), ('f', 'e')]

"""
101 + 10

List1: [1] -> [2] -> [3] //321
List2: [4] -> [5] -> [6] //654
List3: [5] -> [7] -> [9] //975
"""

class UndirectedGraph:
    def __init__(self):
        self.a_list = {}
        
    def add_edge(self, v1, v2):
        if v1 in self.a_list:
            self.a_list[v1].append(v2)
        else:
            self.a_list[v1] = [v2]
            
        if v2 in self.a_list:
            self.a_list[v2].append(v1)
        else:
            self.a_list[v2] = [v1]
            
        return self
    
    def __str__(self):
        return json.dumps(self.a_list)
    

uG = UndirectedGraph()

for edge in edges:
    vX, vY = edge
    uG.add_edge(vX, vY)
       
     
print(uG)


            
        