T = "cccccabababccccc"  # 検索対象文字列
P = "ababab"  # pattern (キーワード) -> 正規表現 ->nfa化
# P = "abab|ababab|abababab" # pattern (キーワード)
n = len(T)  # 検索対象文字列の長さ
m = len(P)  # キーワードの長さ nfaの状態数のこと
S = frozenset(("a", "b", "c"))  # 入力文字の集合
# マスクビット初期化　{ 各入力文字 : patternの長さ分の0で初期化=0b000000 }
M = {s: 0 for s in S}


def bitparallelThompsonNfa():

    # マスクビット配列作成
    temp = 1  # bitを立てた状態で初期化
    for p in P:
        M[p] |= temp
        temp <<= 1
        #print(f'M[{p}]= {bin(M[p])}')

    # マッチング
    R = 0  # NFAの現在の状態配列
    accept = 1 << (m-1)  # bin(accept)=0b100000 のように受理状態だけ1にする
    print(f'bin(accept)= {bin(accept)}')
    for s in range(n):
        # << & (Shif-And) を使ったNFAのシミュレーション
        R = ((R << 1) | 1) & M[T[s]]
        print(f'R= {bin(R)}, M[T[s]]={bin(M[T[s]])} in {s}nd loop')
        if (R & accept) != 0:
            print(f'we\'re found pattern at {s}')


# Driver Code
bitparallelThompsonNfa()
