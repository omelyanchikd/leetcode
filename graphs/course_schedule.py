class Digraph:
    def __init__(self, V):
        self.V = V
        self.vertices = []
        for v in range(V):
            self.vertices.append([])
        self.marked = [False] * V
        self.in_cycle = [False] * V
        self.cycle = False

    def add_edge(self, v, w):
        self.vertices[v].append(w)

    def adjacent(self, v):
        return self.vertices[v]

    def has_cycle(self):
        for v in range(self.V):
            if not self.marked[v] and not self.cycle:
                self.dfs(v)
        return self.cycle

    def dfs(self, v):
        self.marked[v] = True
        self.in_cycle[v] = True
        for w in self.adjacent(v):
            if self.cycle:
                return
            if not self.marked[w]:
                self.dfs(w)
            elif self.in_cycle[w]:
                self.cycle = True
        self.in_cycle[v] = False

def canFinish(numCourses, prerequisites):
    courses = Digraph(numCourses)
    for prerequisite in prerequisites:
        courses.add_edge(prerequisite[0], prerequisite[1])
    return not courses.has_cycle()

if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1, 0]]
    print(canFinish(numCourses, prerequisites))
