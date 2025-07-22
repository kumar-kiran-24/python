class k:
    def __init__(s,fn,db):
        s.fn=fn
        s.db=db
    def print(s):
        print(s.fn,"\n",s.db)

class b(k):
    def __init__(s, fn, db):
        super().__init__(fn, db)
        print("hello")
a=k("kian","29-11-2004")
a.print()
a.print()