def all_variants(text):
    i, x = 0, 0
    while i != len(text):
        yield text[i]
        i += 1
    while x != len(text) - 1:
        yield text[x:x + 2]
        x += 1
    yield text


a = all_variants("abc")
for i in a:
    print(i)
