i = 1
count = 0
n = 120

while i <= n:
    if n % i == 0:
        print(i)
        count += 1
    i += 1

print("%d의 약수는 총 %d개입니다" % (n, count))
