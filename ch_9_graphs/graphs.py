class Graph:
    def __init__(self):
        self.adj_list = {}
    


    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        
        return False
    

    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list:
            edges1 = self.adj_list[v1]
            for e_idx1, e in enumerate(edges1):
                if e == v2:
                    edges1.pop(e_idx1)
        if v2 in self.adj_list:
            edges2 = self.adj_list[v2]
            for e_idx2, e in enumerate(edges2):
                if e == v1:
                    edges2.pop(e_idx2)
        
        return True


    
    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")



if __name__ == '__main__':
    graph = Graph()
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)

    graph.add_edge(5,6)
    graph.add_edge(6,7)
    graph.add_edge(7,5)

    graph.print_graph()

    print('-'*20)
    graph.remove_edge(5,6)
    graph.remove_edge(5,6)
    graph.remove_edge(7,5)
    graph.remove_edge(7,6)
    graph.print_graph()