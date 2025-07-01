import os

password = "admin123"  # Hardcoded
print("Running vulnerable app...")

def dangerous_action():
    eval("print('Evaluated code')")

dangerous_action()
os.system("ls")
