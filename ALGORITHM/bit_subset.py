
# 집합의 원소의 개수가 변하지 않는 경우에만 사용가능
bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i # 0번 원소의 유, 무
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
        for l in range(2):
            bit[3] = l
            print(bit)
