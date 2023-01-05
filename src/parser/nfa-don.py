from typing import List
import ast

# NFAの実装
# 5つ組を定義
ε = None  # ε: 空文字
states = frozenset([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])  # Q: [int]
characters = frozenset([ε, '0'])  # Σ: [ ε | 'string']
start = 0  # q0: int
accept = frozenset([1, 2, 3])  # F: [int]
input_str = ""

# 正規表現
don_regex = "ドンドン(?:(?:ドン)?ドン)?"

# 抽象構文木 (構文解析=parsing)
don_ast = ast.parse(don_regex)
4. この辺り、pythonのソースコードが簡潔でわかりやすいので解説を載せる。実質ビルトイン関数のcompile()をしているだけ。
https: // github.com/python/cpython/blob/a34f0bdcf6a3c91f4b80a788205416e82e95f70f/Lib/ast.py  # L33
5. compile() -> re.parse()に飛ぶ。正規表現マッチングの実装はこれ。少し解説する。
https: // github.com/python/cpython/blob/a34f0bdcf6a3c91f4b80a788205416e82e95f70f/Lib/re/_parser.py  # L507

# NFA構築 (Thompson法)
1. 正規表現の本 4章 DFA型エンジンのThompson法を参考にして実装する

# DFA変換 (決定性化)
2. この辺も探したら普通に出てきそう

# テキスト走査
3. Qiitaに走査結果を書く


def transition(state, char):  # δ: map dictionary (現在のstate, 現在のinput) -> 次のstate
    print(f'trans by state={state}({type(state)}), str={str}({type(char)}')
    if state == 0 and char == None:
        return frozenset([1, 2, 3])
    if state == 1 and char == '0':
        return frozenset([1])
    if state == 2 and char == '0':
        return frozenset([4])
    if state == 3 and char == '0':
        return frozenset([5])
    if state == 4 and char == '0':
        return frozenset([2])
    if state == 5 and char == '0':
        return frozenset([6])
    if state == 6 and char == '0':
        return frozenset([3])
    return frozenset([])


def operation(state, char):
    l_state = set(list(state))
    ll_state = []
    for i, st in enumerate(char):  # 入力文字loop
        print(f'{len(str)-1} == {i}')

        if len(ll_state) > 0:
            l_state = set(ll_state)
            ll_state = []

        # if s == "'":  # 空文字（今回は不要）
        #     s = ε
        for l_s in l_state:  # possible state loop
            print(f'l_state={l_state}')
            print('state:', l_s, 's:', st)
            # for s in str[i]:  # rest str loop
            slist = list(transition(l_s, st))
            ll_state.extend(slist)
            print(f' -> ll_state={ll_state}, slist={slist}')

            lll_state = []
            llll_state = []
            for s in str[i:]:
                for sl in slist:
                    lll_state = transition(sl, s)

            print(f'現在のlll_stateは...{ll_state}')
            if ll_state <= accept:
                print(f'lll_stateを返却します...{ll_state}')
                return ll_state

        # if l_state <= accept:
        #     return l_state
    return set()


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
    nodedatas = []  # NodeData
    ltree = None
    rtree = None
    tree = Tree(nodedatas, ltree, rtree)
    trace_post_order(tree)


if __name__ == "__main__":
    main()
