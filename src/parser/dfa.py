# DFAの実装
# 5つ組を定義
# states = [0, 1, 2]  # Q: int
# characters = ['0', '1']  # Σ: int
start = 0  # q0: int
accept = [0]  # F: int
transition = {  # δ: map dictionary (現在のstate, 現在のinput) -> 次のstate
    (0, '0'): 0, (0, '1'): 1,
    (1, '0'): 2, (1, '1'): 0,
    (2, '0'): 1, (2, '1'): 2,
}
# 空文字, ε = None

input_str = ""


def operation():
    print("判定したい文字列を入力してください: ", end="")
    str = input()
    state = start
    for s in str:
        state = transition[(state, s)]
    return state in accept


def main():

    print(operation())


if __name__ == "__main__":
    main()
