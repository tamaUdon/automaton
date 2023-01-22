
T = "cccccabababccccc"  # 検索対象文字列
P = "abababab"  # pattern (キーワード)
# P = "abab|ababab|abababab" # pattern (キーワード)
n = 6  # 検索対象文字列の長さ
m = 20  # キーワードの長さ
S = frozenset(("a", "b", "c"))  # 入力文字の集合
M = [0] * len(S)  # マスクビット


def bitpsrsllelThompsonNfa():

    # マスクビット作成
    temp = 1
    for i in range(1, m):
        M[P[i]] = temp
        temp <<= 1  # 左ビットシフト

    # マッチング
    R = 0
    accept = 1 << (m - 1)
    for s in range(1, n):
        # << & (Shifi-And) を使ったNFAのシミュレーション
        R = ((R << 1) | 1) & M[T[s]]
        if (R & accept) != 0:
            print(s)


# Driver Code
bitpsrsllelThompsonNfa()


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
