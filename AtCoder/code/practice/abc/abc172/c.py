N,M,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
 
WA = [0]
WB = [0]
n = min(N,M) # 共通の冊数
for i in range(n*2):
    if i%2 == 0:
        WA.append(WA[i]+A[i//2])
        WB.append(WB[i]+B[i//2])
    else:
        WA.append(WA[i]+B[i//2])
        WB.append(WB[i]+A[i//2])
 
    # 途中で制限時間を超えたので終了
    if K < WA[-1] or K < WA[-1]:
        print (i)
        exit ()
 
# 低い方を読み終わった
if N < M: # 大きいほう
    X = B
else:
    X = A
for i in range(n,max(N,M)):
    WA.append(WA[-1]+X[i])
    if K < WA[-1]:
        print (len(WA)-1)
        exit ()
 
# 全部読み終わった
print (len(WA)-1)
