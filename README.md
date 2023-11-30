# OSX-Reorganiser
Reorder files in OSX by metadata field 'Content Created' and rename files to match this order

Context: I have several hundred images that I would like to be arranged by date of creation i.e. the date the image was taken on an iPhone. 

Problem: On Mac OS organising in the finder by date of creation is not possible. A generic field "Created" is not the same, for example.

Desired Solution: Programme should rename images 1...N in order of date of creation. This will allow finder to order correctly (i.e. by name).

This Programme: Reads image filenames and extracts the metadata. Reorders by date of creation. Renames image files accordingly. 

Works for images (.jpeg, HEIC) and movies (.mp4, .MOV). Works for one directory only. Works for spaces in filenames / directory path. Time taken approx 10 seconds per hundred images. 

INSTRUCTIONS: Edit the MAIN.py file to include your directory. Run with python3 from any directory.
