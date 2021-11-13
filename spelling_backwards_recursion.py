

# Easiest way

def spell(txt):
    index = -1
    for i in txt:
        print(txt[index])
        index += -1

# If you want with a recursive base.
def spell(txt):
    if txt == "":
        return txt
    else:
        print(txt[- 1])
        return spell(txt[0:len(txt) - 1])



txt = input()
spell(txt)
