value = input()

data = "c= c- d- lj nj s=".split(" ")
data_2 = "z="
data_3 = "dz="
cnt_1 = 0

if data_2 in value:
    cnt_1 += value.count(data_2)

cnt_2 = 0
if data_3 in value:
    cnt_2 += value.count(data_3)
cnt_1 = cnt_1 - cnt_2
cnt = 0
for i in data:
    if i in value:
        cnt += value.count(i)

cnt_3 = len(value)
last = cnt_3 - (cnt + cnt_1 + 2*cnt_2)
"""print((cnt + cnt_1 + 2*cnt_2), cnt_3)
print(f"cnt : {cnt} , cnt_1 : {cnt_1}, cnt_2 : {cnt_2}, cnt_3 : {cnt_3}")

"""
print(last)


"""c - 참고
c;x;xx;a;b;
int main() {
    while((c = getchar())>20) {
        a++;
        if(c=='-'||c=='='){b--; x=='z' && xx=='d' ? b--:0;}
        if(c=='j')x=='l'||x=='n'?b--:0;
        xx=x;x=c;
    }
    printf("%d\n",a+b);
}
"""