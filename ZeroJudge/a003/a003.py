user_input = input("請輸入出生月分與日期")
m, d  = map(int, user_input.split())
S=(m*2+d)%3
if S == 0:
    print("普通")
elif S == 1:
    print("吉")
elif S == 2:
    print("大吉")
