class Graph:
    def __init__(self, vertices: list[int], edges: list[tuple[int, int]]) -> None:
        self.vertices = vertices
        self.edges = edges
        self.visited_order = []   # Список для хранения порядка обхода вершин

    def __iter__(self):
        # Делаем граф итерируемым для использования в циклах for
        if not self.visited_order:
            self.dfs()
        return iter(self.visited_order)

    def dfs(self) -> list[int]:
        visited = set()   # Посещённые вершины
        self.visited_order = []
        
        def dfs_step(vertex):
            if vertex not in visited:
                visited.add(vertex)   # отмечаем вершину как посещённую
                self.visited_order.append(vertex)
                
                # Ищем соседей вершины
                neighbors = []
                for edge in self.edges:
                    if edge[0] == vertex:
                        neighbors.append(edge[1])
                    elif edge[1] == vertex:
                        neighbors.append(edge[0])
                
                # Обходим соседей
                for neighbor in neighbors:
                    dfs_step(neighbor)
        
        # Обходим все компоненты графа
        for vertex in self.vertices:
            if vertex not in visited:
                dfs_step(vertex)
        
        return self.visited_order