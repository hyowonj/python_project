d = int(input())
f = 1
for c in range (2, d//2 + 1):
    if d % c == 0:
        f = f + 1
    else:
        f = f
if f != 1:
    print("소수가 아니다")
else:
    print("소수이다")
# for h in range(10):
#     if h == 5:
#         continue
#     print(h)
    
      
