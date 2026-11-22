import os

ENTRY = "Every evening, someone leaves a cup of tea by the blue door at the end of the lane, still warm, with a note that says only: tomorrow. No one has ever seen who. By morning, the cup is empty."

os.makedirs("/output", exist_ok=True)
# Write the entry exactly, with no trailing newline, so the file
# contains only the 189 characters of ENTRY.
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
