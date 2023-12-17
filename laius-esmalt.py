from collections import deque

def bfs(graph, algus):
    külastatud = set()
    järjekord = deque([algus])  #järjekord sõlmedele
    külastatud.add(algus)
    
    while järjekord:
        praegune_sõlm = järjekord.popleft()
        print("Külastatud sõlm:", praegune_sõlm) #näitab külastatud sõlmi
        
        for naaber in graph[praegune_sõlm]:
            if naaber not in külastatud:
                külastatud.add(naaber)          #märgi naabersõlm külastatuks ja lisa järjekorda
                järjekord.append(naaber)

#sõnastik lihtsalt suvaline näide
graaf = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C','F'],
    'G': ['C','A', 'D'],
    'H': ['E']
}

#alustab esimest sõlmest
algussõlm = 'A'
bfs(graaf, algussõlm)
