class Graph:
    def __init__(self, edges):
        self.edges = edges
        #transform list into a dict
        self.graphdict = {}
        for start,end in self.edges:
            if start in self.graphdict:
                self.graphdict[start].append(end)
            else:
                self.graphdict[start]=[end]
    
    def get_paths(self, start, end, path=[]):
        path = path+[start]
        if start == end:
            return [path]
        
        if start not in self.graphdict:
            return []
        
        
        

if __name__=='__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    route_graph = Graph(routes)
    start = "Mumbai"
    end = "Mumbai"
    print(f"Paths between {start} and {end}:", route_graph.get_paths(start, end))