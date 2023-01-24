# Define the hash_pattern() function to generate
# a hash for each subpattern

def hashPattern(subpattern):
    h = 0
    for sub in subpattern:
        h = h * 256 + ord(sub)
    return h


# Define the Wu Manber algorithm


def wuManber(text, pattern):

    # Define the length of the pattern and
    # text
    m = len(pattern)
    n = len(text)

    # Define the number of subpatterns to use
    s = 2

    # Define the length of each subpattern
    t = m // s

    # サブパターンを演算子で分割する
    subpattern = pattern.split("[・]|[|]|[*]")

    # Initialize the hash values for each
    # subpattern
    h = [0] * s
    for i in range(s):
        h[i] = hashPattern(pattern, i * t, (i + 1) * t)

    # Initialize the shift value for each
    # subpattern
    shift = [0] * s  # s = subpatternの個数 = 2
    for i in range(s):  # 各subpatternの長さ=2,3,4 * (subpatternの個数(3) - i - 1)=2, 1, 0 -> 4,3,0
        shift[i] = t * (s - i - 1)

    # Initialize the match value
    match = False

    # Iterate through the text
    for i in range(n - m + 1):
        # Check if the subpatterns match
        for j in range(s):
            if hashPattern(text, i + j * t, i + (j + 1) * t) != hlist[j]:
                break
        else:
            # If the subpatterns match, check if
            # the full pattern matches
            if text[i:i + m] == pattern:
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
# text = "aaa"
# pattern = "aa|aaa|aaaa"

# # Function call
# wuManber(text, pattern)
