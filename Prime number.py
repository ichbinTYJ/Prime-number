# -*- coding: utf-8 -*-

def genPrimes():
    p=[]
    if p==[]:
        next=2
        p.append(next)
        yield next
    if p!=[]:
        while True:
            for s in p:
                if next%s!=0:
                    y=True
                else:
                    y=False
                    break
            if y==True:         
                p.append(next)
                yield next
                next=next+1
            else:
                next=next+1
                
