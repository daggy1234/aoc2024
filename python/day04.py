def parser(test: bool):
    graph = {}
    lines = open(f"./data/day04/{"test" if test else "inp"}.txt", "r").readlines()
    for i,l in enumerate(lines):
        lproc = l.strip()
        for j,c in enumerate(lproc):
            graph[(i,j)] = c
    return graph, (len(lines), len(lproc))




def part_1(test: bool = False):
    sequence = ['X', 'M', 'A', 'S']
    dirs = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]

    def dfs(x,y, seqNo, visited,dirs: tuple[int, int] ,bounds: tuple[int, int], graph):
        visited.add((x,y)) 
        if seqNo == 4:
            return True
        
        nx, ny = x+dirs[0], y+dirs[1]
        if 0 <= nx < bounds[0] and 0 <= ny < bounds[1]:
            if graph[(nx,ny)] == sequence[seqNo]:
                return dfs(nx,ny,seqNo+1, visited, dirs, bounds, graph)
    
    graph, bounds = parser(test)
    visited = set()
    ctr = 0
    x_bound, y_bound =  bounds
    for i in range(x_bound):
        for j in range(y_bound):
            if graph[(i,j)] == 'X':
                for z, (dx,dy) in enumerate(dirs):
                    nx, ny = i+dx, j+dy
                    if 0 <= nx < x_bound and 0 <= ny < y_bound:
                        if graph[(nx,ny)] == 'M' :
                            if dfs(nx,ny,2, visited, dirs[z], bounds, graph):
                                ctr += 1
    return ctr

def part_2(test: bool = False):
    xdirs = [(-1,-1), (1,-1), (-1,1), (1,1)]
    graph, bounds = parser(test)
    ctr = 0
    x_bound, y_bound =  bounds
    for i in range(x_bound):
        for j in range(y_bound):
            if graph[(i,j)] == 'A':
                res = []
                for dx,dy in xdirs:
                    if 0 <= i+dx < x_bound and 0 <= j+dy < y_bound:
                        res.append(graph[(i+dx, j+dy)])
                if len(res) == 4 and res in [['M', 'S', 'M', 'S'],['S', 'M', 'S', 'M'], ['M', 'M', 'S', 'S'], ['S', 'S', 'M', 'M']]:
                    ctr += 1
    return ctr

if __name__ == "__main__":
    print(part_1())
    print(part_2())