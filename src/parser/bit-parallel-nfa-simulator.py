# import re

# NFAシミュレータ(照合処理機)作成に必要な定義
# T = "cccccabababccccc" # 検索対象文字列
T = "bbbbaaaabbbbbb" # 検索対象文字列
# P = "abab|ababab|abababab"  # [pattern (キーワード) -> 正規表現 -> 構文木] -> Thompson-NFA
P = "a・(aaa|aa|a)"
# subpattern = re.split("[・|*]", P)
n = len(T)  # 検索対象文字列の長さ
m = len(P)  # キーワードの長さ nfaの状態数のこと
# S = frozenset(("a", "b", "c"))  # 入力文字の集合
S = frozenset(("a", "b"))  # 入力文字の集合
# マスクビット初期化　{ 各入力文字 : patternの長さ分の0で初期化=0b000000 }
M = {s: 0 for s in S}

# シミュレートしたいε-NFAのε-closure + 5つ組定義
E = {
# 各状態sのε-closure
# 状態: (ε遷移で移動可能な次状態)
# 参考: https://www.cs.is.saga-u.ac.jp/lecture/automaton/03F/Lect05.pdf
 0: (0,1,2,3),
 1: (1),
 2: (2),
 3: (3),
 4: (4,10),
 5: (5),
 6: (6),
 7: (7,10),
 8: (8),
 9: (9,10),
 10: (10),
}

delta = {
    # (現在のx番目のposition, 遷移先のy番目の文字列) = y
    (0, "a"): (1),
    (1, "a"): (2,3,5),
    (2, "a"): (3),
    (3, "a"): (4),
    (4, "a"): (5),
    (5, "a"): (6),
    (6, "a"): (7),
}

Qn = P
S = S
In = 0 # 初期状態
Fn = (2,4,7) # 受理状態
Bn = [] 

# Glashnov NFAの作図から。簡単なので大丈夫。
# (ε遷移を含まない)Δを定義
# deltaを書き直す
# 以下のdeltaのloopから空タプル()が返却されなくなる
# Bnが定義できる
# buildEpsilon()が定義できる
# bitparallelThompsonNfa()も定義できる
# 実装完了？
for d in delta: # d = key(0,1,2...)
    (si,σ) = d
    sj = delta[d]
    (σ,_) = delta[i]
    Bn[i][σ] |= 0*(len(Qn)-1-j) + 10*j

# print(f'Bn={Bn}')
# Bn=[{'b': 0, 'a': 0}, {'b': 0, 'a': 0},...]

# ε遷移のマスクテーブル作成に必要な定義
En = {} #[0]*m
for i in range(m):
    for j,s in enumerate(E):
        En[i] |= 0*(len(Qn)-1-j) + 10*j
L = m
# B = Mの拡張版  # {s: 0*L for s in S}  # 基本はMと同じ

# ε遷移付きマスクビット作成
def buildEpsilon():  # シミュレートしたい Glashnov NFA =(Qn, S, In, Fn, Bn, En)
    # Builds ε-mask-table
    # 参考: "情報知識ネットワーク特論「情報検索とパターン照合」" - https://ocw.hokudai.ac.jp/wp-content/uploads/2016/01/InformationKnowledgeNetwork-2005-Note-05.pdf

    # マスクビット作成
    # temp = 1  # bitを立てた状態で初期化
    # for p in P:
    #     M[p] |= temp
    #     temp <<= 1
    #     #print(f'M[{p}]= {bin(M[p])}')

    B = {}  # B = M
    for σ in P:
        B[σ] = 0*L
        for i in range(L):
            B[σ] = B[σ] | Bn[i][σ] # B[σ] =| Bn[i][σ]と同義

    Ed = En   # Ed = R
    for i in range(L):
        for j in range(2**i):
            Ed[2**i + j] = En[i] | Ed[j]
    # print(f'Ed={Ed}')
    # print(f'B={B}')
    return (B, Ed)


def bitparallelThompsonNfa():
    # ビットパラレル化によるNFAシミュレーション (Shift-And法) 
    # 参考: "正規表現技術入門" - https://gihyo.jp/book/2015/978-4-7741-7270-5

    (M, R) = (B, Ed) = buildEpsilon()

    # マスクビット作成
    # temp = 1  # bitを立てた状態で初期化
    # for p in P:
    #     M[p] |= temp
    #     temp <<= 1
    #     #print(f'M[{p}]= {bin(M[p])}')

    # マッチング
    # R = 0
    D = R[In] # 0  # NFAの現在の状態配列（初期状態で初期化）
    accept = 1 << (m-1)  # bin(accept)=0b100000 のように受理状態だけ1にする
    print(f'bin(accept)= {bin(accept)}')
    for s in range(n):
        # << & (Shif-And) を使ったNFAのシミュレーション
        # R = ((R << 1) | 1) & M[T[s]]
        D = R[((D << 1) | 1) & M[T[s]]]
        print(f'D= {bin(D)}, M[T[s]]={bin(M[T[s]])} in {s}nd loop')
        # if (R & accept) != 0:
        if (D & accept) != 0:
            print(f'we\'re found pattern at {s}')


# Driver Code
bitparallelThompsonNfa()
