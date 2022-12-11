# NFAの実装
# 5つ組を定義
ε = None  # ε: 空文字
states = frozenset([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])  # Q: [int]
characters = frozenset(['0'])  # Σ: [ε | 'string']
start = frozenset([list(states)[0]])  # q0: [int]
accept = frozenset([1, 2, 3])  # F: [int]

input_str = ""


def transition(state, str):  # δ: map dictionary (現在のstate, 現在のinput) -> 次のstate
    if state == 0 and str == '0':
        return frozenset([1, 2, 3])
    if state == 1 and str == '0':
        return frozenset([1])
    if state == 2 and str == '0':
        return frozenset([4])
    if state == 3 and str == '0':
        return frozenset([5])
    if state == 4 and str == '0':
        return frozenset([2])
    if state == 5 and str == '0':
        return frozenset([6])
    if state == 6 and str == '0':
        return frozenset([3])
    return frozenset([])


def operation(str, state):
    print('ready for loop...', state)
    l_state = state
    ll_state = set()
    for i, s in enumerate(str):
        print(f'{len(str)} == {i}')

        if len(ll_state) > 0:
            l_state = ll_state ここでset -> frozensetを変換しないとかも、苦明日作った方がはいやいかもね
            ll_state = set()
        # if s == "'":  # 空文字（今回は不要）
        #     s = ε
        for l_s in l_state:  # local状態をアップデート
            print('state:', l_s, 's:', s) あーーーここにfrozenset({1, 2, 3})そのまま履いているんだけどなんで？
            ll_state.add(transition(l_s, s))
            print('->', print(f'llset len={len(ll_state)}')
                  )
            if len(str)-1 == i:  # 入力文字列の最後ならloopせずに終了
                print('早期終了')
                if l_state in accept:
                    return l_state
    return frozenset([])


def main():
    print("判定したい文字列を入力してください: ", end="")
    str = input()
    state = start
    f_state = list(operation(str, state)).pop()  # frozensetから要素を取り出す
    if f_state in accept:
        if f_state == list(states)[1]:
            print(f"これはドンブラザーズです: {f_state, accept}")
        elif f_state == list(states)[2]:
            print(f"これはドン・キホーテです: {f_state, accept}")
        elif f_state == list(states)[3]:
            print(f"これはドン・グリスです: {f_state, accept}")
    else:
        print(f"受理しませんでした: {f_state, accept}")


if __name__ == "__main__":
    main()
