import os
import time

INPUT_DIR = "input_feed"

FILES_TO_CREATE = [
    "CLAIM_Batch2024.csv",  # Should process
    "ENROLL_Jan2025.834",   # Should process
    "ELIG_Daily_Upd.txt",   # Should process
    "UNKNOWN_FILE.pdf",     # Should error
    "CLAIM_Late.csv"        # Should process
]

def create_files():
    if not os.path.exists(INPUT_DIR):
        print(f"Waiting for agent to creating {INPUT_DIR}...")
        try:
            os.makedirs(INPUT_DIR)
        except:
            pass
            
    print("🚀 Stimulating File Feed...")
    for filename in FILES_TO_CREATE:
        item_path = os.path.join(INPUT_DIR, filename)
        with open(item_path, "w") as f:
            f.write("DUMMY CONTENT")
        print(f"dropped: {filename}")
        time.sleep(2) # Stagger them to see processing

if __name__ == "__main__":
    create_files()
