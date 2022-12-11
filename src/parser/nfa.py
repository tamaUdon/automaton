# NFAの実装
# 5つ組を定義
ε = None  # ε: 空文字
states = [0, 1, 2, 3, 4]  # Q: [int]
# characters = [ε, '0', '1']  # Σ: [ε | 'string']
start = [states[0], states[1]]  # q0: [int]
accept = [states[3], states[4]]  # F: [int]
transition = {  # δ: map dictionary (現在のstate, 現在のinput) -> 次のstate
    (states[0], '0'): states[1],
    (states[0], '1'): states[2],
    (states[1], '0'): states[1],
    (states[1], '1'): states[1],
    (states[1], ε): states[3],
    (states[2], '0'): states[2],
    (states[2], '1'): states[2],
    (states[2], ε): states[4],
}

input_str = ""


def operation():
    print("判定したい文字列を入力してください: ", end="")
    str = input()
    state = start
    st_b = -1
    for st_b in state:  # 開始状態が複数ある
        for s in str:
            if s == "'":
                s = ε  # 空文字判定
            print('state:', st_b, 's:', s)
            st_b = transition[(st_b, s)]
            print('->', st_b)
    return st_b in accept


def main():
    print(operation())


if __name__ == "__main__":
    main()
