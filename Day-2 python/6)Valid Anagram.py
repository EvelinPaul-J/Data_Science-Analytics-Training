def is_anagram(s, t):
    return sorted(s) == sorted(t)
s = "listen"
t = "silent"
print(is_anagram(s, t))