import os
import re
import sys

# 1. 获取评论内容
user_comment = os.environ.get("USER_COMMENT", "")
repo_root = os.getcwd() 

# 2. 解析指令
# 格式：/update_page Page: 文件名 Content: 新代码
# 注意：我们假设 Content: 后的内容很长，使用 re.DOTALL 捕获所有换行
match = re.search(r'/update_page\s+Page:\s*(\S+)\s+Content:\s*(.*)', user_comment, re.DOTALL | re.IGNORECASE)

if not match:
    # 如果指令格式不对，退出并失败
    print("Error: Command format incorrect.")
    sys.exit(1)

file_path = match.group(1).strip()
new_content = match.group(2).strip()

# 3. 写入文件 (全量覆盖模式)
try:
    full_path = os.path.join(repo_root, file_path) # 组合绝对路径
    
    # 创建父文件夹（如果不存在）
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ SUCCESS: Updated {full_path}")

except Exception as e:
    print(f"❌ FAILURE: Write Error: {e}")
    sys.exit(1)
