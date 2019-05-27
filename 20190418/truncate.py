from collections import defaultdict
text = """
A press release is the quickest and easiest way to get free publicity. If well written,
a press release can result in multiple published articles about your firm and its products. 
And that can mean new prospects contacting you asking you to sell to them.
"""


text2 = text.lower().split()


word_count = defaultdict(lambda: 0) # default value 를 0으로 하는 딕셔너리 만들어줌
for word in text2:
    word_count[word] += 1

sorted_word_count = sorted(word_count.items())
for k, v in sorted_word_count:
    print(k, ":", v)
