import math
a, b, c = map(float, input().split())
if (a + b > c) and (a + c > b) and (b + c > a) and (a > 0 and b > 0 and c > 0):
    p = (a + b + c) / 2
    dientich = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"{dientich:.1f}")
else:
    print("Khong phai 3 canh cua tam giac")