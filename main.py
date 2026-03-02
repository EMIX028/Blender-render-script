import os
import time
import sys
import tkinter
import tkinter.filedialog as tkFileDialog
import select_el as search
import render_settings



os.system(f"blender -b {search.select_file()} -P script_render.py {search.exp_doss()}")