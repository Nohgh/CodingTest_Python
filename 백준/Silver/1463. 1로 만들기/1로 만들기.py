import sys
input=sys.stdin.readline
n=int(input())

#dp테이블 초기화
d=[0]*1000001

for i in range(2,n+1):
    #현재의 수에서 1을 빼는 경우, 처음부터 1을 빼는 이유 2,3으로 나누지 못하는 값은 미리 빼둬야함, 뒤에서 더 적은 값이 있다면 
    #그 값이 최소가 되기 때문에(비교함) 처음에 그 전값에서 1더한 값으로 시작한다.
    d[i]=d[i-1]+1

    #현재의 수가 2로 나누어 떨어지는 경우
    if i%2==0:
        d[i]=min(d[i],d[i//2]+1) #d[i//2]하고 +1은 2로 나누고
    if i%3==0:
        d[i]=min(d[i],d[i//3]+1)
print(d[n])

