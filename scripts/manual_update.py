import os
import re
import sys

user_comment = os.environ.get("USER_COMMENT", "")
repo_root = os.getcwd()

match = re.search(r'/update_page\s+Page:\s*(\S+)\s+Content:\s*(.*)', user_comment, re.DOTALL | re.IGNORECASE)

if not match:
    print("Error: Command format incorrect.")
    sys.exit(1)

file_path = match.group(1).strip()
new_content = match.group(2).strip()

try:
    full_path = os.path.join(repo_root, file_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"✅ Updated {full_path}")
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)
