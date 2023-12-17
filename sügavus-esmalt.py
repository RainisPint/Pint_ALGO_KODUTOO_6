def dfs(graaf, praegune_sõlm, külastatud):
    # Töötle praegust sõlme ja märgi see külastatuks
    print("Külastatud sõlm:", praegune_sõlm)
    külastatud.add(praegune_sõlm)
    
    for naaber in graaf[praegune_sõlm]:   #töötleb naabersõlmed läbi
        if naaber not in külastatud:
            dfs(graaf, naaber, külastatud)

#graafi näidis
graaf = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

külastatud = set()

algussõlm = 'A'
dfs(graaf, algussõlm, külastatud)
