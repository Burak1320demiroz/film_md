import re

skeleton = "A B A C B D E C A B C A C B A B D C E D A".split()

cameras = {
    "A": "50mm, f/2.8, ISO 800, camera fixed at approximately 1 meter, low angle close-up. Physically accurate perspective.",
    "B": "35mm, f/4.0, ISO 800, camera fixed at approximately 4 meters, eye-level medium shot. Physically accurate perspective.",
    "C": "35mm, f/2.8, ISO 800, camera fixed at approximately 2 meters, low angle medium close-up. Physically accurate perspective.",
    "D": "24mm, f/5.6, ISO 1600, camera fixed at approximately 6 meters, high angle wide shot. Physically accurate perspective.",
    "E": "14mm, f/8.0, ISO 400, static space camera at approximately 1000 meters, extreme wide shot. Physically accurate perspective."
}

motions = {
    "A": "Low-angle close-up at 1 meter, fixed lockoff position.",
    "B": "Eye-level medium shot at 4 meters, fixed camera.",
    "C": "Low-angle medium close-up at 2 meters, fixed camera.",
    "D": "High-angle wide shot at 6 meters, static camera position.",
    "E": "High-angle extreme wide shot at 1000 meters, static camera position."
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
        mot_text = motions[skel]
        
        if scene_idx > int(base_scenes[skel]):
            suffix = f" — the same position, height and lens as Scene {base_scenes[skel]}."
            cam_text += suffix
            mot_text += suffix
            
        # Replace camera
        sec = re.sub(r"(?<=CAMERA:\n)(.*?)(?=\n\n)", cam_text, sec, flags=re.DOTALL)
        
        # Replace MOTION
        sec = re.sub(r"(?<=MOTION: )(.*?)(?=\nLIGHTING:)", mot_text, sec, flags=re.DOTALL)
        
        # Add human count to NEGATIVE CORE
        if "Exactly 6" in sec:
            human_count = "Exactly 6 human characters in the frame."
        else:
            human_count = "Exactly one human character in the frame."
            
        sec = re.sub(r"(?<=NEGATIVE CORE: )(.*?)(?=\n)", lambda m: m.group(1).replace(human_count, "").strip(", ") + ", " + human_count, sec)

        new_sections.append(sec)
        scene_idx += 1
        
    with open(filepath, 'w') as f:
        f.write("---".join(new_sections))

process_file("yatay_4_dk_filmler/THE_LOCKED_PULSE/THE_LOCKED_PULSE_BOLUM_1.md", 0)
process_file("yatay_4_dk_filmler/THE_LOCKED_PULSE/THE_LOCKED_PULSE_BOLUM_2.md", 11)

