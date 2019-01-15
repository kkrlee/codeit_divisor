i = 1
count = 0

while i <= 120:
    if 120 % i == 0:
        print(i)
        count += 1
    i += 1

print("%d의 약수는 총 %d개입니다" % (120, count))
