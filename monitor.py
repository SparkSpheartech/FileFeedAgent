import os
import time
import json
import shutil
import fnmatch
from datetime import datetime

CONFIG_PATH = "config.json"

class FileFeedAgent:
    def __init__(self):
        self.load_config()
        self.ensure_directories()
        
    def load_config(self):
        with open(CONFIG_PATH, "r") as f:
            self.config = json.load(f)
        print(f"[{datetime.now()}] Configuration loaded.")
        
    def ensure_directories(self):
        for key, path in self.config["directories"].items():
            if not os.path.exists(path):
                os.makedirs(path)
                print(f"Created directory: {path}")

    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {message}")
        with open("activity.log", "a") as f:
            f.write(f"[{timestamp}] {message}\n")

    def send_alert(self, email, subject, message):
        # Mock Email Function
        self.log(f"📧 ALERT SENT to {email} | Subject: {subject} | Body: {message}")

    def process_file(self, filename):
        input_path = os.path.join(self.config["directories"]["input"], filename)
        
        # Check against rules
        matched_rule = None
        for rule in self.config["rules"]:
            if fnmatch.fnmatch(filename, rule["pattern"]):
                matched_rule = rule
                break
        
        if matched_rule:
            self.log(f"✅ Rules Match: {filename} matches '{matched_rule['description']}'")
            
            # Action: Move to processed
            dest_path = os.path.join(self.config["directories"]["params"], filename)
            shutil.move(input_path, dest_path)
            self.log(f"🔄 File moved to {dest_path}")
            
            # Action: Alert
            self.send_alert(
                matched_rule["alert_email"],
                f"New File Received: {filename}",
                f"A new file matching '{matched_rule['description']}' has been processed."
            )
        else:
            self.log(f"⚠️ No Rule Match: {filename}")
            # Action: Move to error/unknown
            dest_path = os.path.join(self.config["directories"]["error"], filename)
            shutil.move(input_path, dest_path)
            self.log(f"🛑 File moved to Errors: {dest_path}")
            
            self.send_alert(
                self.config["global_alerts"]["admin_email"],
                f"Unknown File Detected: {filename}",
                "A file was received that does not match any known patterns."
            )

    def run(self):
        input_dir = self.config["directories"]["input"]
        poll_interval = self.config["polling_interval_seconds"]
        
        print(f"👀 File Feed Agent Monitoring: {input_dir}")
        print("Press Ctrl+C to stop.")
        
        try:
            while True:
                files = os.listdir(input_dir)
                if files:
                    for filename in files:
                        self.process_file(filename)
                
                time.sleep(poll_interval)
        except KeyboardInterrupt:
            print("\n🛑 Agent Stopping...")

if __name__ == "__main__":
    agent = FileFeedAgent()
    agent.run()
