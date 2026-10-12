import sys,re,glob
# usage: show.py PREFIX n [n...]  -> prints scene with NEGATIVE lines abbreviated when identical to ref (first scene's)
pref=sys.argv[1]
ns=sys.argv[2:]
def neg_lines(txt):
    return re.findall(r'^NEGATIVE:.*$',txt,re.M)
import os
base=os.path.dirname(os.path.abspath(__file__))+'/w/'
ref=None
for n in ns:
    t=open(f'{base}{pref}_S{n}.txt').read()
    negs=neg_lines(t)
    out=t
    for i,ng in enumerate(negs):
        out=out.replace(ng,f'NEGATIVE[{i}]: <{len(ng)} char> '+ng[:0] if False else f'NEGATIVE[{i}] ({len(ng)} ch): '+ng)
    print(out)
