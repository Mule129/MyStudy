import sys

n = sys.stdin.readline()

value = set()
count = 0
for i in range(int(n)):
    data = sys.stdin.readline()
    if data == "ENTER\n":
        count += len(value)
        value = set()
    
    else: 
        value.add(data)
        
count += len(value)
sys.stdout.write(str(count))

#중복 문자 사용에선 set, 속도 측면에서는 dict 사용이 더 빠르다
# dict 사용시 키에 매칭되는 값에 빈 값(1 등)을 넣어준다..:thinking:
#물론 sys 내장모듈은 input/print 와 비교했을때 넘사벽..
# dict는 자료 크기가 늘어날수록 시간이 많이 걸리지만 dict는 해시 테이블을 이용하여 key값에 따라 value의 저장위치가 결정되어 배열 전체를 탐색하지 않고도 값을 빠르게 찾을 수 있다
#키워드 : 딕셔너리 내부구조, python 3.6이후 내부구조 차이, set()선언, big o 동작표기법