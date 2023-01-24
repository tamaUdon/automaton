T = "cccccabababccccc"  # 検索対象文字列
P = "ababab"  # pattern (キーワード) -> 正規表現 ->nfa化
# P = "abab|ababab|abababab" # pattern (キーワード)
n = len(T)  # 検索対象文字列の長さ
m = len(P)  # キーワードの長さ nfaの状態数のこと
S = frozenset(("a", "b", "c"))  # 入力文字の集合
M = [s for s in S] * len(P)  # マスクビット初期化　各入力文字の種類[] * pattern(キーワード)長


def bitparallelThompsonNfa():

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
bitparallelThompsonNfa()
