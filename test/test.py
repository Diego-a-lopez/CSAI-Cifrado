
import os
import subprocess

# List of file names to process
file_names = ["JdP_001_input", "JdP_002_input", "JdP_003_input", "videoEjemplo"]  # Update with actual file names

# Path to the analysis script
analysis_script = "./analisis.py"  # Update with the actual path

# Path to the decryption script
decryption_script = "./descifrar.py"  # Update with the actual path

# Iterate through each file
for file_name in file_names:
    print(f"Processing file: {file_name}")
    
    # Call the analysis script to get the key
    try:
        key_output = subprocess.check_output(["python", analysis_script, file_name]).decode().strip()
        print("Possible key found:", key_output)
        decryption_output = subprocess.check_output(["python", decryption_script, file_name, key_output])
        # Decode output with UTF-8, ignore errors
        decryption_output = decryption_output.decode('utf-8', 'ignore').strip()
        print("Decrypted text:")
        print(decryption_output) 
    except subprocess.CalledProcessError as e:
        print("Error:", e)
    except UnicodeDecodeError as e:
        print("Error decoding output:", e)
