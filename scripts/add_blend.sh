#!/bin/bash

in_filename=$1
out_filename="${in_filename%%.*}.stl"
blender --background $in_filename --python export_stl.py -- $out_filename
git add $in_filename $out_filename
