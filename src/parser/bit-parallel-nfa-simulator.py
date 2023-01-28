T = "cccccabababccccc"  # 検索対象文字列
P = "ababab"  # pattern (キーワード) -> 正規表現 ->nfa化
# P = "abab|ababab|abababab" # pattern (キーワード)
n = len(T)  # 検索対象文字列の長さ
m = len(P)  # キーワードの長さ nfaの状態数のこと
S = frozenset(("a", "b", "c"))  # 入力文字の集合
# マスクビット初期化　{ 各入力文字 : patternの長さ分の0で初期化[0,0,0,0,0,0] }
M = {s: [0]*m for s in S}

# TODO: []じゃなくて0001のような数値型に変換, さらに二進数に（？）するらしい. M[]もintで初期化できそう.
# 2. ε遷移を実装（おそらく別でシミュレートする.単に演算子|で分割して複数回マッチング書襟を回せば良さそう. = wu-manbar?）
# 3. 引数をThompson-NFA(オートマトン)に変更? <- ε遷移に対応している時点で引数を受け取って↑の初期化をできるはず


def bitparallelThompsonNfa():

    # マスクビット配列作成
    temp = [1]*m  # bitを立てた状態で初期化
    for i, j in enumerate(reversed(range(m))):  # reversedと最初からのindexが必要
        # M=[0,0,0,0,0,0]にPの文字列をreverseした配列を代入する(post-orderで探索するためreverse)
        M[P[j]][i] |= temp[i]  # OR演算 TODO:処理の中身確認

    print(f'M= {M}')

    # マッチング
    R = [0]*m  # NFAの現在の状態配列
    accept = 1 << (m - 1)  # TODO: 受理状態だけビットを立てておく
    print(f'accept= {accept}')
    for s in range(n):
        # << & (Shif-And) を使ったNFAのシミュレーション
        # 検索対象文字列をループで取得して、マスクビット(今は[]で実装している)を引っ張り出している
        # R = [((R << 1) | 1) & c for c in M[T[s]]]
        R = [((R[i] << 1) | 1) & M[T[s]][i]
             for i in range(m)]  # TODO: 多分ここのマスクビット計算がミスっている
        print(f'R= {R} in {s}nd loop')
        if [R[i] & accept[i] for i in range(m)] != [0]*m:
            print(s)


# Driver Code
bitparallelThompsonNfa()
