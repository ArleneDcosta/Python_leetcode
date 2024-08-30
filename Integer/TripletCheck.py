def getaddtripletcount(freq,diff):
    print(freq)
    res = 0
    ele = sorted(freq.keys())

    for i in range(0,len(ele)-2):
        res += freq[ele[i]] * freq[ele[i] + diff] * freq[ele[i] + 2 * diff]

    return res

def solution(queries, diff):
    from collections import defaultdict

    # Initialize dictionaries
    freq = defaultdict(int)  # Tracks the frequency of each number
    pairs = defaultdict(int)  # Tracks valid pairs (x, y) with x - y = diff
    triples_count = 0  # Tracks the number of valid triples

    result = []

    for query in queries:
        op = query[0]
        x = int(query[1:])

        if op == '+':
            freq[x] += 1
            triples_count = getaddtripletcount(freq,diff)

        elif op == '-':
            # Decrease frequency of x
            del freq[x]
            triples_count = getaddtripletcount(freq, diff)
        result.append(triples_count)

    return result

def solutionoptimized(queries, diff):
    from collections import defaultdict

    # Initialize dictionaries
    freq = defaultdict(int)  # Tracks the frequency of each number
    pairs = defaultdict(int)  # Tracks valid pairs (x, y) where x - y = diff
    triples_count = 0  # Tracks the number of valid triples

    # Result array to store the count after each query
    result = []

    for query in queries:
        op = query[0]  # '+' or '-'
        x = int(query[1:])  # The number involved

        if op == '+':
            triples_count += freq[x-diff] * 1 * freq[x + diff]
            triples_count += freq[x-(2 * diff)] * 1 * freq[x-diff]
            triples_count += freq[x+(2 * diff)] * 1 * freq[x+diff]

            freq[x] += 1

        elif op == '-':
            triples_count -= freq[x - diff] * freq[x] * freq[x + diff]
            triples_count -= freq[x - (2 * diff)] * freq[x] * freq[x - diff]
            triples_count -= freq[x + (2 * diff)] * freq[x] * freq[x + diff]

            del freq[x]

        # Store the current count of triples
        result.append(triples_count)

    return result

def solutionnotworking(queries, diff):
    from collections import defaultdict

    # Initialize dictionaries
    freq = defaultdict(int)  # Tracks the frequency of each number
    pairs = defaultdict(int)  # Tracks valid pairs (x, y) where x - y = diff
    triples_count = 0  # Tracks the number of valid triples

    # Result array to store the count after each query
    result = []

    for query in queries:
        op = query[0]  # '+' or '-'
        x = int(query[1:])  # The number involved

        if op == '+':
            # Add valid triples involving x as the middle element
            triples_count += pairs[x - diff]

            # # Update pairs to include new pairs ending with x + diff
            # pairs[x + diff] += freq[x]

            # Update pairs to include new pairs starting with x - diff
            pairs[x] += freq[x - diff]

            # Increase frequency of x
            freq[x] += 1

        elif op == '-':
            # Remove valid triples involving x as the middle element
            triples_count -= pairs[x - diff]

            # Update pairs to exclude pairs ending with x + diff
            pairs[x + diff] -= freq[x]

            # Decrease frequency of x
            freq[x] -= 1

            # Update pairs to exclude pairs starting with x - diff
            pairs[x] -= freq[x - diff]

            # Remove x from freq if no more occurrences
            if freq[x] == 0:
                del freq[x]

        # Store the current count of triples
        result.append(triples_count)

    return result



if __name__ == '__main__':
    print(solution(queries=["+4", "+5", "+6", "+4", "+3", "-4"], diff=1))
    print(solutionoptimized(queries=["+4", "+5", "+6", "+4", "+3", "-4"], diff=1))
