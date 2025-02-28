def process_data_sets(k, data_sets):
    results = []
    for i in range(k):
        n, m, *traits = data_sets[i]
        your_traits = traits[0]
        ancestor_traits = traits[1:]
        
        mutant_count = sum(1 for j in range(m) if all(your_traits[j] != ancestor[j] for ancestor in ancestor_traits))
        
        results.append(f"Data Set {i+1}:\n{mutant_count}/{m}\n")
    
    return "\n".join(results)

k = int(input().strip())
data_sets = []
for _ in range(k):
    n, m = map(int, input().split())
    traits = [input().strip() for _ in range(n + 1)]
    data_sets.append((n, m, *traits))

print(process_data_sets(k, data_sets))