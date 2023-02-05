import re

T = "cccccabababccccc"  # 検索対象文字列
P = "abab|ababab|abababab"  # pattern (キーワード) -> 正規表現 -> Thompson-NFA

# Define the length of the pattern and text
m = len(P)
n = len(T)

# サブパターンを演算子で分割する
subpattern = re.split("[・|*]", P)
s = len(subpattern)  # サプパターンの個数
t = m // s  # 各サブパターンの長さ

# Initialize the shift value for each subpattern
shift = [0]*s  # s = subpatternの個数 = 3

# Initialize the hash values for each subpattern
hshvals = [0]*s

# Define the hash_pattern() function to generate
# a hash for each subpattern


def hashPattern(subpattern):
    hsh = 0
    for sub in subpattern:
        hsh = hsh * 256 + ord(sub)
    return hsh


# Define the Wu Manber algorithm


def wuManber():

    hshvals = [hashPattern(subpattern[i]) for i in range(s)]
    print(hshvals)

    # 各subpatternの長さ=2,3,4 * (subpatternの個数(3) - i - 1)=2, 1, 0 -> 4,3,0
    shift = [t * (s - i - 1) for i in range(s)]

    # Initialize the match value
    match = False

    # Iterate through the T
    for i in range(n - m + 1):
        # Check if the subpatterns match
        for j in range(s):
            if hashPattern(T, i + j * t, i + (j + 1) * t) != hshvals[j]:
                break
        else:
            # If the subpatterns match, check if
            # the full pattern matches
            if T[i:i + m] == P:
                print("Match found at index", i)
                match = True

        # Shift the pattern by the appropriate
        # amount
        for j in range(s):
            if i + shift[j] < n - m + 1:
                break
        else:
            i += shift[j]

    # If no match was found, print a message
    if not match:
        print("No match found")


# # Driver Code
# T = "aaa"
# pattern = "aa|aaa|aaaa"
# # Function call
wuManber()
