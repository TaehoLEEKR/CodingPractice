'''시간초과'''
# N = int(input())
# cardList = list(map(int,input().split()))
# M = int(input())
# countList = list(map(int,input().split()))
# res = [cardList.count(i) for i in countList]
# print(' '.join(map(str,res)))

from collections import defaultdict

N = int(input())
cardList = list(map(int, input().split()))

cardCount = defaultdict(int)
for card in cardList:
    cardCount[card] += 1

M = int(input())
countList = list(map(int, input().split()))

res = [cardCount[num] for num in countList]

print(' '.join(map(str, res)))

