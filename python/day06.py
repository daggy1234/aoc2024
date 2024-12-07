def parser(test):
    lines = open(f"./data/day06/{"test" if test else "inp"}.txt", "r").readlines()
    graph = {}
    start_ps = None
    xbc = 0
    ybc = 0
    for i, l in enumerate(lines):
        xbc = max(xbc, i)
        for j, c in enumerate(l.strip()):
            if c == '^':
                start_ps = (i, j)
            graph[(i, j)] = c
            ybc = max(ybc, j)
    return graph, start_ps, (xbc, ybc)

def part_1(test: bool = False):
    graph, start_ps, bounds = parser(test)
    dir = [(-1,0), (0,1), (1,0), (0,-1)]
    dir_mutations = ["^", ">", "v", "<"]
    ind = 0
    onctr = 0
    visited = set([start_ps])
    while True:
        apply_dir = dir[ind]
        new_ps = (start_ps[0] + apply_dir[0], start_ps[1] + apply_dir[1])
        if new_ps in visited:
            onctr += 1
        if new_ps[0] < 0 or new_ps[1] < 0 or new_ps[0] > bounds[0] or new_ps[1] > bounds[1]:
            break
        if graph[new_ps] == '#':
            ind += 1
            if ind >= len(dir):
                ind = 0
        else:
            graph[new_ps] = dir_mutations[ind]
            start_ps = new_ps
            visited.add(start_ps)
    return (len(visited)) 


def run_loop(graph, start_ps, bounds):
    dir = [(-1,0), (0,1), (1,0), (0,-1)]
    ind = 0
    visited = set([start_ps])
    dir_at_visited_p = {}
    dir_at_visited_p[start_ps] = dir[ind]
    while True:
        apply_dir = dir[ind]
        new_ps = (start_ps[0] + apply_dir[0], start_ps[1] + apply_dir[1])
        if new_ps in visited:
            if dir_at_visited_p[new_ps] == dir[ind]:
                return True, visited
        if new_ps[0] < 0 or new_ps[1] < 0 or new_ps[0] > bounds[0] or new_ps[1] > bounds[1]:
            break
        if graph[new_ps] == '#' or graph[new_ps] == 'O':
            ind += 1
            if ind >= len(dir):
                ind = 0
        else:
            start_ps = new_ps
            visited.add(start_ps)
            dir_at_visited_p[start_ps] = dir[ind]
    return False, visited

def part_2(test: bool = False):
    graph, start_ps, bounds = parser(test)
    oldsttat, visited = run_loop(graph, start_ps, bounds)
    loopctrs = 0
    for p in visited:
        if graph[p] == '#':
            continue
        graph[p] = '#'
        check,simvisit = run_loop(graph, start_ps, bounds)
        if check:
            loopctrs += 1
        graph[p] = '.'
        
    
    return len(visited), loopctrs

# print(part_1(False))
print(part_2(False))
