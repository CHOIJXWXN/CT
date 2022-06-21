"""
가운데를 말해요
**다른 사람 코드임**
"""
from heapq import heappop, heappush
import sys
read = sys.stdin.readline

N = int(read())
mxh, mnh = list(), list()               # maxheap에는 중간값 포함 작은 수를, minheap에는 중간값 미포함 큰 수를 저장
for _ in range(N):
    n = int(read())
    if len(mnh) == len(mxh):            # 홀수째일 때 maxheap에 넣고
        heappush(mxh, -n)
    else:                               # 짝수째일 때 minheap에 넣음
        heappush(mnh, n)
    if mnh and mnh[0] < -mxh[0]:        # minheap에서 제일 작은 값이 maxheap에서 제일 큰 값보다 작을 때
        heappush(mnh, -heappop(mxh))    # maxheap에서 제일 큰 값을 minheap에 추가
        heappush(mxh, -heappop(mnh))    # minheap에서 제일 작은 값을 maxheap에 추가
    print(-mxh[0])                      # maxheap에서 가장 큰 값 출력
