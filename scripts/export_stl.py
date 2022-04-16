import bpy
import sys
import os

filename: str = sys.argv[-1]
filename_no_ext = os.path.splitext(filename)[0]
filename_no_ext_no_path = os.path.split(filename)[1]
if filename_no_ext_no_path != "":
	bpy.ops.export_mesh.stl(filepath=f"{filename}")
