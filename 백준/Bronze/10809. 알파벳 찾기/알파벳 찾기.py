ans = {}
for a in range(97,123):
    ans[chr(a)] = -1
word = input()
word = list(word)
for i in range(len(word)):
    if(ans[word[i]] == -1):
        ans[word[i]] = i
for i in ans:
    print(ans[i], end=" ")