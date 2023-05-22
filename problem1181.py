
lst = [input() for _ in range(int(input()))]
words = list(set(lst))
words.sort()
print("\n".join(map(str,sorted(words,key=lambda x:len(x)))))








