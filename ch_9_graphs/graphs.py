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
        if v1 in self.adj_list and v2 in self.adj_list:
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        
        return False
    

    def remove_vertex(self, vertex):
        if vertex not in self.adj_list:
            return False
        
        edges = self.adj_list[vertex]

        for el in edges:
            try:
                self.adj_list[el].remove(vertex)
            except ValueError:
                pass
        
        del self.adj_list[vertex] 

        return True
    

    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")



if __name__ == '__main__':
    graph = Graph()
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_vertex(8)
    graph.add_vertex('A')

    graph.add_edge(5,6)
    graph.add_edge(6,7)
    graph.add_edge(7,5)
    graph.add_edge('A',8)
    graph.add_edge('A',7)
    graph.add_edge('A',6)
    graph.add_edge('A',5)

    graph.print_graph()

    print('-'*20)
    # graph.remove_edge(5,6)
    # graph.remove_edge(5,6)
    graph.remove_vertex(7)
    graph.remove_vertex(5)
    graph.print_graph()