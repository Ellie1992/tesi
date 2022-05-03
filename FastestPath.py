a = 0
b = 1
c = 2
d = 3
e = 4
f = 5
g = 6
h = 7
i = 8
j = 9
V = [a,b,c,d,e,f,g,h,i,j]
def edg(a):
    if a == 0:
        return 'a'
    elif a == 1:
        return 'b'
    elif a == 2:
        return 'c'
    elif a == 3:
        return 'd'
    elif a == 4:
        return 'e'
    elif a == 5:
        return 'f'
    elif a == 6:
        return 'g'
    elif a == 7:
        return 'h'
    elif a == 8:
        return 'i'
    elif a == 9:
        return 'j'
#edges = [(0, 1, 1, 1), (4, 7, 2, 1), (0, 1, 2, 1), (1, 5, 3, 1), (1, 4, 3, 1), (0, 3, 3, 1), (0, 2, 4, 1), (3, 6, 5, 1), (4, 8, 6, 1), (2, 5, 6, 1), (5, 8, 7, 1), (5, 6, 7, 1), (6, 9, 8, 1), (6, 9, 9, 1), (0, 6, 10, 1)]
#edges = [(a, b, 1, 1), (e, h, 2, 2), (a, b, 5, 1), (b, f, 6, 1), (b, e, 3, 1), (a, d, 3, 3), (a, c, 4, 2), (d, g, 5, 1), (e, i, 6, 1), (c, f, 6, 1), (f, i, 7, 1), (f, g, 7, 2), (g, j, 8, 1), (g, j, 9, 1), (a, g, 10, 1), (i, j, 8, 1)]
#edges = [(0, 1, 1, 1), (4, 7, 2, 2), (0, 1, 6, 1), (1, 5, 7, 1), (1, 4, 3, 1), (0, 3, 3, 3), (0, 2, 4, 2), (3, 6, 5, 1), (4, 8, 6, 1), (2, 5, 6, 1), (5, 8, 8, 1), (5, 6, 8, 1), (6, 9, 8, 1), (6, 9, 10, 1), (0, 6, 0, 1), (6, 9, 1, 4)]
#edges = [(0, 1, 1, 1), (4, 7, 2, 2), (0, 1, 5, 1), (1, 5, 6, 1), (1, 4, 3, 1), (0, 3, 3, 3), (0, 2, 4, 2), (3, 6, 5, 1), (4, 8, 6, 1), (2, 5, 6, 1), (5, 8, 7, 1), (5, 6, 7, 2), (6, 9, 8, 1), (6, 9, 9, 1), (0, 6, 11, 1), (6, 9, 12, 5)]
#edges = [(0, 1, 1, 1), (4, 7, 2, 2), (0, 1, 5, 1), (1, 5, 6, 1), (1, 4, 3, 1), (0, 3, 3, 3), (0, 2, 4, 2), (3, 6, 5, 1), (4, 8, 6, 1), (2, 5, 6, 1), (5, 8, 7, 1), (5, 6, 7, 2), (6, 9, 8, 1), (6, 9, 9, 1), (0, 6, 6, 3)]
#edges = [(a, b, 2, 1), (e, h, 2, 2), (a, b, 1, 1), (b, f, 6, 1), (b, e, 3, 1), (a, d, 3, 3), (a, c, 1, 2), (d, g, 5, 1), (e, i, 6, 1), (c, f, 6, 1), (f, i, 7, 1), (f, g, 7, 2), (g, j, 8, 1), (g, j, 9, 1), (a, g, 10, 1), (i, j, 8, 1)]
#edges = [(a, b, 1, 1), (e, h, 2, 2), (a, b, 5, 1), (b, f, 6, 1), (b, e, 3, 1), (a, d, 3, 3), (a, c, 4, 2), (d, g, 5, 1), (e, i, 6, 1), (c, f, 6, 1), (f, i, 7, 1), (f, g, 7, 2), (g, j, 8, 1), (g, j, 9, 1), (a, g, 4, 1)]
#edges = [(a, b, 1, 1),(a,c,2,1),(b,d,2,1),(c,d,3,2)]
#edges = [(a, b, 1, 1),(b,d,2,1),(a,c,2,1),(c,d,3,2)]
#edges = [(a, b, 1, 1),(b,d,2,1),(a,c,2,2),(c,d,4,1)]
#edges = [(a, b, 5, 1),(a,c,9,1),(b,d,6,1),(c,e,10,1),(d,f,7,2),(e,f,11,1)]
#edges = [(a, b, 5, 1),(a,c,7,1),(b,d,6,1),(c,d,8,1),(d,f,7,2),(d,f,9,1)]
edges = [(a, b, 4, 1),(a,c,5,1),(c,d,6,1),(b,d,6,1),(d,f,7,2),(d,f,9,1)]
edges.sort(key = lambda x:x[2])
for e in edges:
    print(edg(e[0])+", "+edg(e[1])+", "+str(e[2])+", "+str(e[3]))
def max_a(l,t):
    max = (-float('inf'),-float('inf'))
    for el in l:
        if el[1] >= max[1] and el[1] <= t:
            max = el
    if max == (-float('inf'),-float('inf')):
        return []
    return max
def startingTimeAlreadyExist(l, st, at):
    for i in range(0,len(l)) :
        if l[i][0]==st:
            l[i] = (l[i][0], at) #(l[i][0],min(l[i][1], at))
    return l
def stae(l, st):
    for el in l:
        if el[0]==st:
            return True
    return False
def cancellaElementiDominati(l,s,a):
    for el in l:
        if (s > el[0] and a <= el[1])  or (s == el[0] and a < el[1]):
            l.remove(el)
    return l
def nonDominato(l,s,a):
    for el in l:
        if (el[0] > s and el[1] <= a)  or (el[0] == s and el[1] < a):
            return False
    return True

def FP(s,es,V):
    l ={}
    f =[]
    esr = []
    i = 0
    for v in V:
        l[v]=[]
        if v == s:
            f.append((0,float('inf')))
        else:
            f.append((float('inf'),float('inf')))
    for e in es:
        if e[0] == s:
            if (e[2],e[2]) not in l[e[0]]:
                l[e[0]].append((e[2],e[2]))
        if l[e[0]]:
            max = max_a(l[e[0]], e[2])
            '''
            print(edg(e[0])+" "+edg(e[1]))
            print(l[e[0]])
            print("t: "+str(e[2]))
            print("t+l: "+str(e[2]+e[3]))
            print("max: "+str(max))
            print(l[e[1]])
            '''
            if max:
                if stae(l[e[1]], max[0]):
                    startingTimeAlreadyExist(l[e[1]], max[0], e[2]+e[3])
                else:
                    if nonDominato(l[e[1]], max[0], e[2]+e[3]):
                        l[e[1]].append((max[0], e[2]+e[3]))
                        esr.append(e)
                        i+=1
                if (e[2]+e[3]-max[0]) < f[e[1]][0]:
                    f[e[1]] = (e[2]+e[3]-max[0],e,i-1)
                cancellaElementiDominati(l[e[1]],max[0], e[2]+e[3])
                
    return f,esr

ff,esr = FP(a,edges,V)



for v in ff:
    if v[0] == float('inf') or v[1]==float('inf'):
        print(v)
    else:
        print(str(v[0])+", ("+edg(v[1][0])+", "+edg(v[1][1])+", "+str(v[1][2])+", "+str(v[1][3])+"), "+ str(v[2]))
'''
for e in edges:
    print(edg(e[0])+", "+edg(e[1])+", "+str(e[2])+", "+str(e[3]))
'''
for e in esr:
    print(edg(e[0])+", "+edg(e[1])+", "+str(e[2])+", "+str(e[3]))
def fastestPathOracolo(esr,ff,s,t):
    if ff[t][1] == float('inf'):
        return ["No esiste path"]
    start = ff[t][2]
    path =[t]
    at = float('inf')
    while s not in path:
        if esr[start][1] == t and esr[start][2]+esr[start][3] <= at: 
            path.append(esr[start][0])
            t = esr[start][0]
            at = esr[start][2]
        start = start - 1
    return path

path = fastestPathOracolo(esr,ff,a,f)

for p in path[::-1]:
    print(edg(p))
