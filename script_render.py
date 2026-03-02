import bpy
import os
import time
import tkinter
import tkinter.filedialog as tkFileDialog


def exp_doss():
    dossier = tkFileDialog.askdirectory(title="Choisir le répertoire cible")
    if dossier:
        return dossier
    else: 
        print("Aucun chemin renvoyé")
        sys.exit(1)

#Dossier d'output
output_dir = exp_doss()
os.makedirs(output_dir, exist_ok=True)

#fichier Log
log_file = os.path.join(output_dir, "log.txt")

scene = bpy.context.scene
#scene.render.engine = 'BLENDER_EEVEE_NEXT'  # ou 'CYCLES'
scene.render.image_settings.file_format = 'PNG' #format de sortie

ranges = []

Plages = input("Enter the frames like this: FrameX>frameY-frameY+1>frameZ for example\n").split("-")
try:
    for el in Plages:
        frm = el.split(">")
        assert(len(frm)==2,"A frame range can only go from one frame to another (Frame0>Frame5 for example)")
        ranges.append((int(frm[0]),int(frm[1])))
except:
    print("\nERROR : a numeric value is required for frames\n")

frames_to_render = set()
for start, end in ranges:
    frames_to_render.update(range(start, end+1))

frames_sorted = sorted(frames_to_render)
total_frames = len(frames_sorted)

for i, frame in enumerate(frames_sorted, 1):
    scene.frame_set(frame)
    scene.render.filepath = os.path.join(output_dir, f"frame_{frame:04d}")
    
    start_time = time.time()
    bpy.ops.render.render(write_still=True)
    end_time = time.time()
    
    frame_time = end_time - start_time
    eta = frame_time * (total_frames - i)
    
    msg = (f"[{i}/{total_frames}] Frame {frame} | "
           f"Time: {frame_time:.2f}s | ETA: {eta/60:.2f}min | "
           f"File: {scene.render.filepath} | "
           f"Engine: {scene.render.engine} | "
           f"Resolution: {scene.render.resolution_x}x{scene.render.resolution_y}")
    
    print(msg)
    
    with open(log_file, "a") as f:
        f.write(msg + "\n")

#& blender_path -b fichier.blend -P script_render.py if blender not in the environment PATH

#blender -b fichier.blend -P script_render.py if blender in environment PATH