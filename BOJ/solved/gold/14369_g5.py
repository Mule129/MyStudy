"""
one ->->->->o
two -> w
three ->-> h
four ->->-> r
five ->->->v
six -> x
seven ->-> s
eight -> g
nine ->->->->->n
ten ->->-> t

4
OZONETOWER
WEIGHFOXTOURIST
OURNEONFOE
ETHER

고유 단어가 있는 단어 제거. 제거한 단어와 제거되지 않은 단어중 겹치는 단어 있으면 하나씩 순차적으로 제거해 나감
중복된 숫자 값이 있을 수 있음을 주의할 것
"""
# 14369_g5
number_arr = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
number_arr_cnt = [0 for _ in range(10)]
en_arr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
arr = [0 for _ in range(len(number_arr))]

dump_arr = []

def change_number(value: str = "OZONETOWER") -> str:
    dump = 0
    # min 값을 계속 찾아나서기. min 값이 1일 경우 고유한 값으로 판단
    # 첫번째 반복문 : 0~9 사이 고유 단어 찾기(min을 통하여)
    # 두번째 반복문 : 고유단어 바탕으로 문자 내 단어 분석
    while True:
        for i in range(len(number_arr)):
            for j in range(len(i)):
                if number_arr[i][j] in number_arr[i+1]:
                    break
                number_arr_cnt[i] += 1

    return "123"

for i in range(1, int(input())+1):
    print(f"Case #{i}: ", change_number(input()))
