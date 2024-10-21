# Function to find Levenshtein distance between string `X` and `Y`.
def dist(X, Y):
    # `m` and `n` is the total number of characters in `X` and `Y`, respectively
    (m, n) = (len(X), len(Y))

    # For all pairs of `i` and `j`, `T[i, j]` will hold the Levenshtein distance
    # between the first `i` characters of `X` and the first `j` characters of `Y`.
    # Note that `T` holds `(m+1)×(n+1)` values.
    T = [[0 for x in range(n + 1)] for y in range(m + 1)]

    # we can transform source prefixes into an empty string by
    # dropping all characters
    for i in range(1, m + 1):
        T[i][0] = i  # (case 1)

    # we can reach target prefixes from empty source prefix
    # by inserting every character
    for j in range(1, n + 1):
        T[0][j] = j  # (case 1)

    # fill the lookup table in a bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:  # (case 2)
                cost = 0  # (case 2)
            else:
                cost = 1  # (case 3c)

            T[i][j] = min(T[i - 1][j] + 1,  # deletion (case 3b)
                          T[i][j - 1] + 1,  # insertion (case 3a)
                          T[i - 1][j - 1] + cost)  # replace (case 2 + 3c)

    return T[m][n]

if __name__ == '__main__':
    X = 'ABA'
    Y = 'ABC'

    print('The Levenshtein distance is', dist(X, Y))
#Remember if you are deleting from A to B u make insert val in prev and delete will depete for deleting from A it is [i-1,j], '' and B, then insert + 1[for deleting]
#Remember if you are inserting from A to B B u will delete from B and insert
#https://www.techiedelight.com/levenshtein-distance-edit-distance-problem/

# dp[i-1][j]: This value represents the cost of converting the first i-1 characters of str1 to the first j characters of str2,
# i.e., after performing a deletion operation on str1 (removing the i-th character OF STR1 TO MATCH STR2).
# dp[i][j-1]: This value represents the cost of converting the first i characters of str1 to the first j-1 characters of str2,
# i.e., after performing an insertion operation on str1 (adding the j-th character of str2 TO STR1).