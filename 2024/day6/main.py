data = open("input.txt").read()
grid = {y+1j*x:v for y,r in enumerate(data.splitlines())for x,v in enumerate(r)}
start = [x for x in grid if grid[x]=="^"][0]

def walk(grid):
    p,d,S = start,-1,set()
    while p in grid and(p,d)not in S:
        S.add((p,d))
        if grid.get(p+d)=="#":
            d *= -1j
        else:
            p += d
    return {s[0]for s in S},(p,d) in S

part1=len(P := walk(grid)[0])
part2=sum(walk(grid|{p: "#"})[1]for p in P)