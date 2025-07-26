import os

#folder_path = os.environ.get("folder_path")
folder_path = "/app/output"


def test():
  with open(os.path.join(folder_path, "out_connectors.txt"), "w") as f:
    print(f"DEBUG: Writing to {folder_path}")
    f.write("hola!dddddddddddddddd!!")
    
test()
