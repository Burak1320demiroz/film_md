# -*- coding: utf-8 -*-
"""THE_STOLEN_SKY — ortak prompt parçaları (PLAN Bible ile birebir aynı metin)."""

TOTAL = 96

# ── CAMERA BIBLE — 20 harf, aynı harf = aynı metin (03_SAHNE_SIRALAMASI §4 sözlüğü + ölçülebilir imza) ──
CAM = {
 "A": "wide shot, 24mm spherical lens, low angle, camera low at knee height on a fixed locked-off tripod, 6.0 m from the nearest subject, absolutely zero camera movement",
 "B": "medium shot, 40mm spherical lens, camera at eye height on a fixed tripod, 3.0 m from the figure, absolutely zero camera movement",
 "C": "over-the-shoulder medium close-up, 35mm spherical lens, camera just behind and above the near figure's shoulder at head height, 1.8 m from the far subject, fixed, absolutely zero camera movement",
 "D": "medium close-up, 50mm spherical lens, high angle, camera slightly above eye height at 1.7 m looking down at the hands and the object, 1.4 m from them, fixed, absolutely zero camera movement",
 "E": "wide shot, 24mm spherical lens, high angle, camera slightly above head height at 2.2 m on a fixed locked-off tripod, 7.0 m from the nearest subject, absolutely zero camera movement",
 "F": "medium long shot, 28mm spherical lens, camera at eye height on a fixed tripod, 4.0 m from the figures, absolutely zero camera movement",
 "G": "medium long shot from the rear of the cabin, 24mm spherical lens, camera at seated eye height fixed to the rear cabin wall, 2.2 m from the pilot seat, it moves only as the craft moves",
 "H": "medium long tracking shot from behind and slightly to one side of the craft, 28mm spherical lens, camera at hull height 8.0 m behind the craft, the camera keeps pace with it",
 "J": "medium shot, 40mm spherical lens, low angle, camera slightly below the figure's chest height at 1.2 m, 2.6 m from the figure, a slow steady push-in over the whole take",
 "K": "extreme close-up macro insert, 75mm spherical lens, camera flat and square to the surface at hand height, 0.5 m from it, fixed, absolutely zero camera movement",
 "L": "medium close-up, 50mm spherical lens, low angle, camera slightly below eye height at 1.1 m looking up at the hand and the control, 1.4 m from them, fixed, absolutely zero camera movement",
 "M": "medium shot tracking upward from below and behind the craft, 28mm spherical lens, camera 9.0 m behind the craft's tail, the camera rises with it",
 "N": "medium shot, 28mm spherical lens, low angle, camera low at ground height on a fixed tripod, 12 m from the craft, absolutely zero camera movement",
 "O": "medium long shot following behind the walking figures, 28mm spherical lens, camera at shoulder height 3.5 m behind the last figure, the camera moves forward at their walking pace",
 "P": "wide shot from the side, 28mm spherical lens, camera at hull height on a fixed tripod, 30 m from the craft, absolutely zero camera movement",
 "Q": "wide shot looking back down from outside the lattice, 24mm spherical lens, high angle, camera 40 m from the craft, fixed, absolutely zero camera movement",
 "R": "medium shot through the fine metal mesh of the lift cage, 35mm spherical lens, camera at chest height inside the cage, 2.0 m from the figure outside, the camera rises with the cage",
 "T": "wide shot, 24mm spherical lens, camera at eye height on a fixed tripod, 8.0 m from the hangar mouth, a single slow pan from inside the hangar mouth out to the sky, no other movement",
 "W": "medium shot, 35mm spherical lens, profile, camera at chest height, 2.5 m from the subject, a short sideways track that settles and holds",
 "X": "medium shot tracking upward from the front lower quarter of the craft, 35mm spherical lens, low angle, camera 10 m ahead of and below the craft, the camera rises with it",
}
CAM_TR = {  # başlık bloğu için
 "A": "24mm · WS · low angle · lockoff", "B": "40mm · MS · eye level · fixed", "C": "35mm · MCU · OTS · fixed",
 "D": "50mm · MCU · high angle (slight) · fixed", "E": "24mm · WS · high angle (slight) · lockoff", "F": "28mm · MLS · eye level · fixed",
 "G": "24mm · MLS · cabin rear · craft-fixed", "H": "28mm · MLS · rear-quarter tracking", "J": "40mm · MS · low angle (slight) · push-in",
 "K": "75mm · ECU · flat · fixed", "L": "50mm · MCU · low angle (slight) · fixed", "M": "28mm · MS · from below-behind · rising",
 "N": "28mm · MS · low angle · fixed", "O": "28mm · MLS · from behind · walking pace", "P": "28mm · WS · side · fixed",
 "Q": "24mm · WS · looking back down · fixed", "R": "35mm · MS · through mesh · rising", "T": "24mm · WS · eye level · single pan",
 "W": "35mm · MS · profile · short side track", "X": "35mm · MS · front-low · rising",
}

def isaret(kind, ref):
    if kind == "donus":
        return f"— the same position, height and lens as Scene {ref+1}."
    if kind == "kume":
        return f"continues the previous clip from its exact last frame — the same position, height and lens as Scene {ref+1}."
    return ""

# ── PHYSICS / AUDIO — hacme göre (KONSEPT §2; her promptta aynı sayı) ──
PHYS = {
 "YUZEY": "Gravity is 0.9 g under one atmosphere of breathable-density air; dust falls fast and settles within two seconds, shadow edges soft but deep, haze rises and thins, nothing hangs in the air.",
 "IC":    "Gravity is 0.9 g under one atmosphere of breathable-density air; dust falls fast and settles within two seconds, shadow edges soft but deep, haze rises and thins, nothing hangs in the air.",
 "KABIN": "Gravity is 0.9 g inside a cabin pressurised at one atmosphere; loose objects fall fast and settle within two seconds, nothing hangs in the air.",
 "KABIN0G": "Microgravity inside a cabin pressurised at one atmosphere; the one loose object drifts in a straight line while turning slowly on its own axis, the three figures strapped in.",
 "C0":    "Gravity is 0.9 g inside a hull pressurised at one atmosphere; nothing floats, dust falls fast and settles within two seconds.",
 "VAKUM": "Hard vacuum in orbit above the planet; no air and no sound outside the hulls, shadows absolute black with razor edges, any released fragment keeps a straight line and its own rotation axis.",
}
PHYS_SHORT = {
 "KABIN": "inside the sealed cabin at one atmosphere the same 0.9 g holds, nothing floats.",
 "VAKUM": "above the lattice the air is gone, no sound outside, shadows absolute black, any fragment keeps a straight line.",
 "C0":    "inside the amber hull the same 0.9 g holds at one atmosphere.",
 "IC":    "inside, the same 0.9 g holds at one atmosphere.",
 "YUZEY": "outside, the same 0.9 g holds under one atmosphere.",
}
AUD = {
 "YUZEY": "Sound carries normally — engine roar, metal impacts, wind; breathing inside the helmet.",
 "IC":    "A closed-space echo, a steady low fan, distant muffled impacts through the walls, breathing inside the helmet.",
 "KABIN": "A steady cabin hum and breathing inside the helmets, exterior sound muffled.",
 "KABIN0G": "A steady cabin hum and breathing inside the helmets, exterior sound muffled.",
 "C0":    "Low curved tones inside the hull, a slow deep hum, no human breathing.",
 "VAKUM": "No exterior sound at all; only the radio hiss and breathing carried inside the hull.",
}

def physics(vol):
    if isinstance(vol, tuple):
        a, b = vol
        if PHYS[a] == PHYS[b]:
            return f"PHYSICS: {PHYS[a]}"
        return f"PHYSICS: {PHYS[a]} From the moment the volume changes, {PHYS_SHORT[b]}"
    return f"PHYSICS: {PHYS[vol]}"

def audio(vol, extra):
    if isinstance(vol, tuple):
        a, b = vol
        base = f"{AUD[a]} After the transition, {AUD[b][0].lower()+AUD[b][1:]}"
    else:
        base = AUD[vol]
    e = (extra.strip().rstrip(".") + ". ") if extra else ""
    return f"AUDIO: {base} {e}No dialogue. No music."

# ── NEGATIVE BIBLE — §5.1 çekirdek (bu filmin kapsam satırıyla) ──
N_TAKE  = "Single unbroken take, no cuts, no dissolves, no camera resets, no angle change."
N_BLOOM = "0% bloom, no glow, no soft focus, every surface keeps visible texture."
N_TEXT  = "No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suits, the tools, the craft, the panels, the walls or the ground in the frame — no subtitles, no captions, no watermark."
N_GRAIN = "Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture, no face morphing, no face and no eyes behind any helmet pane."
N_GEAR  = "Equipment and clothing identical throughout, no drift, no gear appearing or disappearing."
N_HAND  = "Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers."
N_PART  = "Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping."
N_PANE  = "No face, no eyes and no mouth behind any helmet pane, every pane stays fully opaque."
N_VEYRA = "Each tall figure keeps exactly two arms, two legs and one head, no extra limbs, no human face on it."
N_SHORT_TEXT = "No readable text, letters, digits or symbols on any surface, no subtitles, no captions, no watermark."

def n_count(h, v=0):
    vv = {0:"", 1:" and exactly one tall figure with two arms, two legs and one head", 2:" and exactly two tall figures each with two arms, two legs and one head", 3:" and exactly three tall figures each with two arms, two legs and one head"}[v]
    if h == 0 and v: return "Exactly " + {1:"one tall figure",2:"two tall figures",3:"three tall figures"}[v] + " with two arms, two legs and one head, human count zero, no duplicates."
    if h == 1:  return "Exactly one human character in a suit" + vv + ", no duplicates, no extra person."
    if h == 2:  return "Exactly 2 human characters in suits" + vv + ", no duplicates, no extra person."
    if h == 3:  return "Exactly 3 human characters in suits" + vv + ", no duplicates, no extra person."
    if h == 4:  return "Exactly 4 human characters in suits" + vv + ", no duplicates, no extra person."
    return ""

def negative(video, humans, veyra, extra, insansiz_short):
    """insansiz_short=True: <900 karakter, yokluk kalıbı yok (KART 10)."""
    s = []
    if video: s.append(N_TAKE)
    if humans == 0:
        if veyra: s.append(n_count(0, veyra))
        else: s.append("Human count zero in this frame, the empty deck and sky are the subject.")
        s += [N_BLOOM, N_SHORT_TEXT, N_GRAIN, N_GEAR, N_PART]
        ex = list(extra)
        out = " ".join(s + ex)
        while len(out) >= 900 and ex:
            print(f"   ⚠️ insansız NEGATIVE {len(out)} ≥ 900 — ek düşürüldü: {ex[-1][:50]}")
            ex = ex[:-1]; out = " ".join(s + ex)
        assert len(out) < 900, ("insansız NEGATIVE uzun", len(out))
        return out
    if humans or veyra: s.append(n_count(humans, veyra))
    s += [N_BLOOM, N_TEXT, N_GRAIN, N_GEAR, N_HAND, N_PART]
    budget = 10 - len(s)   # betik kapanış çitini de sayıyor → fiilî tavan 10 (8 çekirdek + ≤2)
    ex = list(extra)
    if len(ex) > budget:
        print(f"   ⚠️ NEGATIVE ek {len(ex)} > bütçe {budget} — fazlası düşürüldü: {ex[budget:]}")
        ex = ex[:budget]
    s += ex
    return " ".join(s)

# ── CHARACTER BIBLE — kelimesi kelimesine; IN FRAME'e göre parça seçilir ──
PANE = "a squared helmet with one flat pane, fully opaque matte black, in a thick dark rim"
PANES = "every helmet squared with one flat pane, fully opaque matte black, in a thick dark rim"
CH = {
 "MARA": {
   "full":  "a commander in a dark cobalt hard-shell suit, a pale grey mark on the left shoulder plate, a short flat tool in the gloves, a small wrist control on the left forearm, " + PANE,
   "short": "a dark cobalt hard-shell suit with a pale grey mark on the left shoulder plate",
   "torso": "a dark cobalt hard-shell torso with a pale grey mark on the left shoulder plate, " + PANE,
   "hands": "dark cobalt gloves with a small wrist control on the left forearm",
   "back":  "the back of the dark cobalt suit is one continuous sculpted surface from collar to hip carrying nothing, a pale grey mark on the left shoulder plate",
   "scar":  "a long pale scrape across the left chest plate",
 },
 "REY": {
   "full":  "a pilot in a burnt-orange hard-shell suit with white bands on both upper arms and a narrow flat unit on the back, " + PANE,
   "short": "a burnt-orange hard-shell suit with white bands on both upper arms",
   "torso": "a burnt-orange hard-shell torso with white bands on both upper arms, " + PANE,
   "hands": "burnt-orange gloves, white bands at the upper arms",
   "back":  "the burnt-orange back is one continuous surface from collar to hip carrying only one narrow flat unit no thicker than a hand",
 },
 "ADA": {
   "full":  "an engineer in an off-white hard-shell suit with teal forearms, a flat rectangular module frame on the back, a hand-held field reader at the belt, " + PANE,
   "short": "an off-white hard-shell suit with teal forearms and a flat rectangular module frame on the back",
   "torso": "an off-white hard-shell torso with teal forearms, " + PANE,
   "hands": "off-white gloves with teal forearms",
   "back":  "the off-white back is one continuous surface from collar to hip carrying only one flat rectangular module frame the size of a chest plate",
 },
 "BOR": {
   "full":  "a heavy gunner in a graphite-grey hard-shell suit, broad mustard chest plates carrying a row of spare power cells, wide shoulders, a long dark tool held across the front, " + PANE,
   "short": "a graphite-grey hard-shell suit with broad mustard chest plates and a long dark tool",
   "torso": "a graphite-grey hard-shell torso, broad mustard chest plates carrying a row of spare power cells, " + PANE,
   "hands": "graphite-grey gloves on a long dark tool",
   "back":  "the back of the graphite-grey suit is one continuous sculpted surface from collar to hip carrying nothing",
   "limp":  "the right knee plate cracked and dark, his weight on the left leg",
   "empty": "the cell slots on the chest plates empty",
 },
}
VEYRA  = "a tall pale-ceramic figure a head taller than a human, narrow chest, a long head sweeping back, the lower leg bending backward, dark seams at every joint, a curved amber shield on the forearm with its convex face forward"
VEYRA_NOSHIELD = "a tall pale-ceramic figure a head taller than a human, narrow chest, a long head sweeping back, the lower leg bending backward, dark seams at every joint"
VEYRA_S = "a tall pale-ceramic figure a head taller than a human, the long head sweeping back, the lower leg bending backward"
SERRAK = "a tall pale-ceramic figure a head taller than a human, narrow chest, a long head sweeping back into a raised crest, a single wide ridge on one shoulder, the lower leg bending backward, dark seams at every joint"
OFFICER = "a tall pale-ceramic figure a full head taller than a human, a long head sweeping back, a single narrow mark on one shoulder, an amber service key the length of a hand clipped into a slot on the forearm"
K1  = "a boxy four-seat assault boat in scuffed grey, angular hull, a white-blue status lamp on the flank, two thrust rings at the rear quarters"
K1_BENT = "the right thrust ring bent out of line and jammed"
K1_CLAMP = "a squared steel clamp bolted across the right thrust ring holding it at one fixed angle"
K1_STUB = "the rear sensor stub torn off, a raw bright stump left on the tail"
E1  = "a wide evacuation ship with one broad horizontal white band along its grey hull"
E2  = "a second evacuation ship with two vertical white bands on its grey hull"
E2_DMG = "a dark scorch along its right stabiliser"
C0  = "the curved amber Veyra command ship, seamless hull"
FIGHTER = "a curved seamless Veyra fighter with an amber-lit edge"
DRONE = "a small marker drone the size of a helmet with three short clamp legs"
PORTAL_OPEN = "a bounded gate of amber light standing between two marker points, its edge a clean line"
LATTICE = "high in the sky a wide amber lattice of straight lines spaced no wider than two ship-lengths"
RING = "beyond the lattice, lower and smaller, the lensed bright ring of the black hole hangs at a fixed place, never pulsing"
WORLD = "black basalt ridges and angular worn human structures"
