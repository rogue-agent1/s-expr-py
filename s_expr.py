def parse(text):
    tokens = text.replace('(',' ( ').replace(')',' ) ').split()
    def read(i):
        if tokens[i]=='(':
            lst=[]; i+=1
            while tokens[i]!=')': v,i=read(i); lst.append(v)
            return lst, i+1
        tok=tokens[i]
        try: return int(tok),i+1
        except ValueError:
            try: return float(tok),i+1
            except ValueError: return tok,i+1
    r,_=read(0); return r
def serialize(obj):
    if isinstance(obj,list): return '('+' '.join(serialize(x) for x in obj)+')'
    return str(obj)
if __name__ == "__main__":
    e="(+ 1 (* 2 3) (- 10 4))"
    p=parse(e)
    assert p==['+',1,['*',2,3],['-',10,4]]
    assert serialize(p)==e
    print(f"Parsed: {p}")
    print("All tests passed!")
