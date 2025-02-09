from collections import defaultdict, deque

def alien_order(words):
    # Step 1: Create a graph and count in-degrees
    graph = defaultdict(set)
    in_degree = {char: 0 for word in words for char in word}  # Initialize in-degrees for all characters

    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        min_length = min(len(word1), len(word2))
        
        # Check for invalid case: word2 is a prefix of word1 but appears later
        if len(word1) > len(word2) and word1[:min_length] == word2[:min_length]:
            return ""  # Invalid order
        
        # Find the first differing character and add an edge
        for j in range(min_length):
            if word1[j] != word2[j]:
                if word2[j] not in graph[word1[j]]:
                    graph[word1[j]].add(word2[j])
                    in_degree[word2[j]] += 1
                break

    # Step 2: Perform topological sort using Kahn's Algorithm
    queue = deque([char for char in in_degree if in_degree[char] == 0])
    result = []

    while queue:
        char = queue.popleft()
        result.append(char)
        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) == len(in_degree):
        return "".join(result)
    return ""  # Cycle detected or incomplete graph


if __name__ == "__main__":
    # Test cases
    test_cases = [
        (["wrt", "wrf", "er", "ett", "rftt"], "wertf"),  # Regular case
        (["z", "x", "z"], ""),  # Cycle case
        (["abc", "ab"], ""),  # Prefix conflict
        (["a", "b", "c"], "abc"),  # Disconnected graph
        (["a"], "a"),  # Single word
    ]

    for words, expected in test_cases:
        result = alien_order(words)
        print(f"Words: {words} -> Result: {result} (Expected: {expected})")
        assert result == expected, f"Test failed for words: {words}"