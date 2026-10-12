import sys,re,os,glob,collections
pref=sys.argv[1]
base=os.path.dirname(os.path.abspath(__file__))+'/w/'
files=sorted(glob.glob(f'{base}{pref}_S*.txt'),key=lambda f:int(re.search(r'_S(\d+)\.txt',f).group(1)))
HEAD={'IN','FRAME','CAMERA','PHYSICS','AUDIO','NEGATIVE','TIMELINE','START','FRAME:','SÜRE','VURUŞ','KURULUM','KLİP','SAHNE','IMAGE','VIDEO','PROMPT','GÖRSEL','VİDEO','HOOK','AMBER','TH','THE'}
cap=collections.defaultdict(list)
for f in files:
    n=int(re.search(r'_S(\d+)\.txt',f).group(1))
    t=open(f).read()
    # split image/video
    parts=re.split(r'### 🎥',t)
    img=parts[0]; vid=parts[1] if len(parts)>1 else ''
    for nm,seg in (('img',img),('vid',vid)):
        body=re.sub(r'^```.*$','',seg,flags=re.M)
        body='\n'.join(l for l in body.split('\n') if not l.startswith('# THE_') and not l.startswith('## ') and not l.startswith('SÜRE'))
        for m in re.finditer(r'\b[A-Z][A-Z0-9]{1,}\b',body):
            w=m.group(0)
            cap[w].append((n,nm))
for w,l in sorted(cap.items(),key=lambda x:-len(x[1])):
    ns=sorted(set(n for n,_ in l))
    print(w,len(l),'scenes',len(ns),ns[:12])
