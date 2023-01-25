T = "cccccabababccccc"  # 検索対象文字列
P = "ababab"  # pattern (キーワード) -> 正規表現 ->nfa化
# P = "abab|ababab|abababab" # pattern (キーワード)
n = len(T)  # 検索対象文字列の長さ
m = len(P)  # キーワードの長さ nfaの状態数のこと
S = frozenset(("a", "b", "c"))  # 入力文字の集合
# マスクビット初期化　{ 各入力文字のord[] : patternの長さ分の0で初期化[0,0,0,0,0,0] }
M = {s: [0]*m for s in S}


def bitparallelThompsonNfa():

    # マスクビット作成
    temp = [1]*m
    print(f'temp= {temp}')
    for i in range(m):
        M[P[i]] = temp  # patternの長さ分の0で初期化[0,0,0,0,0,0]の部分に正しい配列を入れる
        temp <<= [1]*6  # 左ビットシフト <------ TODO:list内包表記でbit-shiftを実装する

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
