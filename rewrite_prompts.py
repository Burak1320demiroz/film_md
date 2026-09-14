import re

skeleton = "A B A C B D E C A B C A C B A B D C E D A".split()

cameras = {
    "A": "50mm, f/2.8, ISO 800, camera fixed at approximately 1 meter, low angle close-up. Physically accurate perspective.",
    "B": "35mm, f/4.0, ISO 800, camera fixed at approximately 4 meters, eye-level medium shot. Physically accurate perspective.",
    "C": "35mm, f/2.8, ISO 800, camera fixed at approximately 2 meters, low angle medium close-up. Physically accurate perspective.",
    "D": "24mm, f/5.6, ISO 1600, camera fixed at approximately 6 meters, high angle wide shot. Physically accurate perspective.",
    "E": "14mm, f/8.0, ISO 400, static space camera at approximately 1000 meters, extreme wide shot. Physically accurate perspective."
}

base_scenes = {
    "A": "00",
    "B": "01",
    "C": "03",
    "D": "05",
    "E": "06"
}

def process_file(filepath, start_scene_idx):
    with open(filepath, 'r') as f:
        content = f.read()

    sections = content.split('---')
    new_sections = [sections[0]]
    
    scene_idx = start_scene_idx
    
    for sec in sections[1:]:
        if not ("📸 GÖRSEL PROMPT" in sec or "🎥 VİDEO PROMPT" in sec):
            new_sections.append(sec)
            continue
            
        skel = skeleton[scene_idx]
        cam_text = cameras[skel]
        
        if scene_idx > int(base_scenes[skel]):
            cam_text += f" — the same position, height and lens as Scene {base_scenes[skel]}."
            
        # Replace camera
        sec = re.sub(r"(?<=CAMERA:\n)(.*?)(?=\n\n)", cam_text, sec, flags=re.DOTALL)
        
        # Add 'station heading 12 o'clock' to ENVIRONMENT if station/ring/hub is mentioned
        if "station" in sec.lower() or "hub" in sec.lower() or "ring" in sec.lower():
            sec = re.sub(r"(?<=ENVIRONMENT:\n)(.*?)(?=\n\n)", r"\1 Station heading 12 o'clock.", sec, flags=re.DOTALL)
            
        # Add flat back to SUBJECT
        sec = re.sub(r"(?<=SUBJECT:\n)(.*?)(?=\n\n)", r"\1 Back silhouette is flat, no back-mounted equipment.", sec, flags=re.DOTALL)
        
        # Replace Lars with the astronaut
        sec = re.sub(r"\bLars('s)?\b", lambda m: "the astronaut's" if m.group(1) else "the astronaut", sec)
        
        # Replace negative text block
        sec = re.sub(r"no readable text, no text overlay, no title card, no HUD", "No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign", sec)
        
        new_sections.append(sec)
        scene_idx += 1
        
    with open(filepath, 'w') as f:
        f.write("---".join(new_sections))

process_file("yatay_4_dk_filmler/THE_LOCKED_PULSE/THE_LOCKED_PULSE_BOLUM_1.md", 0)
process_file("yatay_4_dk_filmler/THE_LOCKED_PULSE/THE_LOCKED_PULSE_BOLUM_2.md", 11)

