from typing import List
# import ast


# def transition(state, char):  # δ: map dictionary (現在のstate, 現在のinput) -> 次のstate

# print(f'trans by state={state}({type(state)}), str={str}({type(char)}')
# if state == 0 and char == None:
#     return frozenset([1, 2, 3])
# if state == 1 and char == '0':
#     return frozenset([1])
# if state == 2 and char == '0':
#     return frozenset([4])
# if state == 3 and char == '0':
#     return frozenset([5])
# if state == 4 and char == '0':
#     return frozenset([2])
# if state == 5 and char == '0':
#     return frozenset([6])
# if state == 6 and char == '0':
#     return frozenset([3])
# return frozenset([])


# 選択に対応するGNFA(ε-NFA)
# 5つ組を定義
ε = None  # ε: 空文字
Q = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}  # Q: 取りうる状態の集合
Sigma = {'ドン'}  # Σ: アルファベット
I = {0}  # q0: 初期状態
F = {1, 2, 3}  # F: 受理状態の集
delta = {  # (現在の状態, 入力アルファベット) : 取りうる状態の辞書
    (0, ε): {1, 2, 3},
    (1, 'ドン'): {4},
    (2, 'ドン'): {5},
    (3, 'ドン'): {6},
    (4, 'ドン'): {10},
    (5, 'ドン'): {7},
    (6, 'ドン'): {8},
    (7, 'ドン'): {10},
    (8, 'ドン'): {9},
    (9, 'ドン'): {10},
}

input_str = ""

# ✅正規表現
# don_regex = "ドンドン(?:(?:ドン)?ドン)?"
# don_regex = "(ドンドンドンドン) | (ドンドンドン) | (ドンドン)"


# ✅抽象構文木 (構文解析=parsing) ... この段落はいらないかも。正規表現から直接Thompson法で作図したため。また、正規表現->AST->NFA変換関数も必要になるため。
# don_ast = ast.parse(don_regex)
# 4. この辺り、pythonのソースコードが簡潔でわかりやすいので解説を載せる。実質ビルトイン関数のcompile()をしているだけ。
# https: // github.com/python/cpython/blob/a34f0bdcf6a3c91f4b80a788205416e82e95f70f/Lib/ast.py  # L33
# 5. compile() -> re.parse()に飛ぶ。正規表現マッチングの実装はこれ。少し解説する。
# https: // github.com/python/cpython/blob/a34f0bdcf6a3c91f4b80a788205416e82e95f70f/Lib/re/_parser.py  # L507

# NFA構築
# ✅ Thompson法の定義に従い、選択に対応するε-NFAを定義 -> 図を書いた。
# ✅ 1.1 図から5つ組（p130の記載を移す）に起こす
# ✅ 1.2 expand関数を作成し、ε遷移除去をする（p127）
# ✅ 2.0 部分集合構成法でDFAに変換する (決定性化)（p129）
#  2.1 wu-manbarでe-nfaを直接シミュレート

# def expand(states, delta):
#     # ε-NFAからε遷移を除去する
#     # statesは状態の集合、deltaは遷移関数（文字と状態集合の辞書）
#     modified = True
#     while modified:
#         modified = False
#         for q in states:
#             if not states >= delta[(q, ε)]:
#                 states |= delta[(q, ε)]
#             modified = True
#     return states

BuildEps(N=(Qn, ∑, In, Fn, Bn, En)):
    for σ∈∑do
    B[σ] ←0L
    for i∈0…L–1 doB[σ] ←B[σ] | Bn[i, σ]
    end of for
    Ed[0] ←En[0]
    for i∈0…L–1 do
    for j∈0…2i–1 do
    Ed[2i + j] ←En[i] | Ed[j]
    end of for
    end of for
    return (B, Ed)


def bp_thompson(N=(Qn, ∑, In, Fn, Bn, En), T=t1t2…tn):
    Preprocessing:
        (B, Ed) ←BuildEps(N)
    Searching:
        D ←Ed[In]
        /* 初期状態*/
        for pos∈1…n do
        ifD & Fn≠0L then report an occurrence ending at pos–1
        D ←Ed[(D << 1) & B[tpos]]
        end of for


def subset_construction(Q, Sigma, delta, I, F):
    # 部分集合構成法によるDFA変換
    Q_d = set()
    delta_d = dict()
    F_d = set()
    queue = {frozenset(I)}
    dfa_states = {frozenset(I): 0}

    while len(queue) != 0:
        dstate = queue.pop()
        Q_d.add(dfa_states[dstate])
        if dstate & F:
            F_d.add(dfa_states[dstate])
        for sigma in Sigma:
            dnext = frozenset(dnext)
            if len(dnext) == 0:
                continue
            if not dnext in dfa_states:
                queue.add(dnext)
                newstate = len(dfa_states)
                dfa_states[dnext] = newstate
            delta_d[(dfa_states[dstate], sigma)] = dfa_states[dnext]
    return Q_d, Sigma, delta_d, 0, F_d


# def operation(state, char):
#     l_state = set(list(state))
#     ll_state = []
#     for i, st in enumerate(char):  # 入力文字loop
#         print(f'{len(str)-1} == {i}')

#         if len(ll_state) > 0:
#             l_state = set(ll_state)
#             ll_state = []

#         # if s == "'":  # 空文字（今回は不要）
#         #     s = ε
#         for l_s in l_state:  # possible state loop
#             print(f'l_state={l_state}')
#             print('state:', l_s, 's:', st)
#             # for s in str[i]:  # rest str loop
#             slist = list(transition(l_s, st))
#             ll_state.extend(slist)
#             print(f' -> ll_state={ll_state}, slist={slist}')

#             lll_state = []
#             llll_state = []
#             for s in str[i:]:
#                 for sl in slist:
#                     lll_state = transition(sl, s)

#             print(f'現在のlll_stateは...{ll_state}')
#             if ll_state <= accept:
#                 print(f'lll_stateを返却します...{ll_state}')
#                 return ll_state

#         # if l_state <= accept:
#         #     return l_state
#     return set()


# def main():
#     print("判定したい文字列を入力してください: ", end="")
#     str = input()
#     state = start

#     f_state = operation(state, str)  # == 1のところマッピング型（dictを追加で定義する）
#     if not f_state:
#         print(f"受理しませんでした: {f_state}")
#     elif list(f_state)[0] == 1:
#         print(f"これはドンブラザーズです: {f_state}")
#     elif list(f_state)[0] == 2:
#         print(f"これはドン・キホーテです: {f_state}")
#     elif list(f_state)[0] == 3:
#         print(f"これはドン・グリスです: {f_state}")
#     else:
#         print(f"Uncaught Error: {f_state}")

def main():

    non_ε_nfa = expand(Q, delta)
    print(non_ε_nfa)

    # subset_construction(Q, Sigma, delta, I, F)

    # nodedatas = []  # NodeData
    # ltree = None
    # rtree = None
    # tree = Tree(nodedatas, ltree, rtree)
    # trace_post_order(tree)


if __name__ == "__main__":
    main()
