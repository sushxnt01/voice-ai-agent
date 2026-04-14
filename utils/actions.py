import os

OUTPUT_DIR = "output"

# make sure output folder exists
os.makedirs(OUTPUT_DIR, exist_ok=True)


def create_file():
    file_path = os.path.join(OUTPUT_DIR, "sample.txt")
    with open(file_path, "w") as f:
        f.write("This file was created by AI.")
    return f"File created at {file_path}"


def write_code():
    file_path = os.path.join(OUTPUT_DIR, "code.py")
    with open(file_path, "w") as f:
        f.write("print('Hello from AI code')")
    return f"Code written in {file_path}"


def summarize(text):
    return "Summary: " + text[:50]