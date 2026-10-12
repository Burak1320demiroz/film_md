import sys,re,os,glob,json
pref=sys.argv[1]
base=os.path.dirname(os.path.abspath(__file__))+'/w/'
files=sorted(glob.glob(f'{base}{pref}_S*.txt'),key=lambda f:int(re.search(r'_S(\d+)\.txt',f).group(1)))
R={
 'AUDIO_satiri': r'^AUDIO:',
 'ses_yasasi(transmitted|conducted|vacuum silence|no exterior|no sound)': r'^AUDIO:.*(transmitted|conducted|vacuum silence|no exterior|no outside|no sound|through the (hull|boot|sole|suit|structure))',
 'temas_el_yuzey': r'[Hh]and-to-surface',
 'temas_nesne_nesne': r'object-to-object|object-to-surface|between objects',
 'giysi_birebir': r'(clothing|suit)[^.]{0,40}identical|identical[^.]{0,40}(clothing|suit)',
 'g_sayisi': r'\b0[.,]\d+\s*g\b|m/s',
 'ortam_adi(vacuum|thin atmosphere)': r'vacuum|thin atmosphere|atmosphere of',
 'saat_yonu': r"o'clock",
 'efor_oran(rate/decay/slows)': r'(slows?|slower|decay|decelerat|shorter|per second|cm in the first|reps? |tremor|shake|shak)',
 'gok/ufuk(sky|horizon|stars)': r'\b(sky|horizon|stars?)\b',
 'ekran/gosterge': r'\b(screen|display|monitor|gauge|readout|HUD|dial)s?\b',
 'tok_nesne_sayisi(rakam)': r'\b\d+\s+(rivets?|bolts?|cylinders?|plates?|struts?|lugs?)',
}
neg_core={}
print('film',pref,'scenes',len(files))
for k,p in R.items():
    hv=[];hi=[]
    for f in files:
        n=int(re.search(r'_S(\d+)\.txt',f).group(1))
        t=open(f).read()
        parts=t.split('### 🎥')
        img=parts[0]; vid=parts[1] if len(parts)>1 else ''
        if re.search(p,vid,re.M|re.I): hv.append(n)
        if re.search(p,img,re.M|re.I): hi.append(n)
    print(f'{k}: video {len(hv)}/{len(files)} | image {len(hi)}/{len(files)}')
    if len(hv)<len(files) and len(files)-len(hv)<=14: print('   video eksik:',[int(re.search(r"_S(\d+)\.txt",f).group(1)) for f in files if int(re.search(r"_S(\d+)\.txt",f).group(1)) not in hv])
