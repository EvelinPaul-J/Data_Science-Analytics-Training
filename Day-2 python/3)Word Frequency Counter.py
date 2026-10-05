def freq(text):
    freq_li=text.lower().split()
    result={}
    for word in freq_li:
         result[word] = result.get(word, 0) + 1
    return result
text="Python is easy and Python is powerful"
print(freq(text))