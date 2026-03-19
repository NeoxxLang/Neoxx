import os
import shutil
import threading
import time
import sys

# Paths
source_nxx = "nxx"
source_venv = "nxxvenv"
source_compiler_py = os.path.join("compiler", "nxxc.py")
source_compiler_cpp = os.path.join("compiler", "nxxc.cpp")

destination = "GeneratedProject"

# Spinner animation
running = True
def spinner():
    symbols = ['/', '|', '\\', '|']
    i = 0
    while running:
        sys.stdout.write("\r" + symbols[i % len(symbols)])
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1

# Start spinner thread
t = threading.Thread(target=spinner)
t.start()

def copy_folder(src, dst):
    if os.path.exists(src):
        shutil.copytree(src, dst, dirs_exist_ok=True)

def copy_file(src, dst):
    if os.path.exists(src):
        shutil.copy2(src, dst)

# Create destination
os.makedirs(destination, exist_ok=True)

# Copy stuff
copy_folder(source_nxx, os.path.join(destination, "nxx"))
copy_folder(source_venv, os.path.join(destination, "nxxvenv"))
copy_file(source_compiler_py, os.path.join(destination, "nxxc.py"))
copy_file(source_compiler_cpp, os.path.join(destination, "nxxc.cpp"))

# Stop spinner
running = False
t.join()

# Final message
print("\rDone!")