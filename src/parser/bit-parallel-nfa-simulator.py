import re

# NFAシミュレータの定義
T = "cccccababababccccc" # 検索対象文字列
P = "abab|ababab|abababab"  # [pattern (キーワード) -> 正規表現 -> 構文木] -> Thompson-NFA
subpattern = re.split("[・|*]", P) # サブパターンを演算子で分割する
s = len(subpattern)  # サプパターンの個数
n = len(T)  # 検索対象文字列の長さ
S = frozenset(("a", "b", "c"))  # 入力文字の集合
M = [{s_alpha: 0 for s_alpha in S} for sub in subpattern] # マスクビット初期化　{ 各入力文字 : 0で初期化=0b000000.. }


def bitparallelThompsonNfa():
    # ビットパラレル化によるNFAシミュレーション (Shift-And法) 
    # 参考: "正規表現技術入門" - https://gihyo.jp/book/2015/978-4-7741-7270-5

    # マスクビット作成
    for i in range(s):
        temp = 1  # bitを立てた状態で初期化
        for sub_a in subpattern[i]:
            M[i][sub_a] |= temp
            temp <<= 1

    # マッチング
    accept = [1 << len(sub)-1 for sub in subpattern] # 0b100000のように左端のビットを立てる(受理状態).

    for i in range(s): # range(s)=サブパターンの個数
        # << & (Shif-And) を使ったNFAのシミュレーション
        R = 0
        
        for t_alpha in T: # T=対象検索文字列
            R = (((R << 1) | 1) & M[i][t_alpha])
            print(f'bin(R)= {bin(R)}, accept={bin(accept[i])}, result={R & accept[i]}')

            if (R & accept[i]) != 0:
                print(f'*** マッチしました {subpattern[i]} ***')

bitparallelThompsonNfa()
