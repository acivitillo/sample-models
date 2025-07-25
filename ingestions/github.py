# In your job script
import os

# Use the OUTPUT_DIR environment variable if available
output_dir = os.environ.get("OUTPUT_DIR", "/app/output")
os.makedirs(output_dir, exist_ok=True)

# Create the file in the shared directory
file_path = os.path.join(output_dir, "example.txt")
with open(file_path, "w") as file:
    file.write("Hello from the job!")
