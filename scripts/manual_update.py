import os
import re
import sys

user_comment = os.environ.get("USER_COMMENT", "")
repo_root = os.getcwd()

print("=== DEBUG: 完整收到的评论 ===")
print(user_comment)
print("=== END DEBUG ===\n")

# 超级宽容正则：允许 Content: 后有任意数量换行/空格，甚至整段代码单独一行
pattern = r'/update_page\s+Page:\s*([^\s]+)\s+Content:\s*([\s\S]*)'  # 关键！用 [\s\S]* 吃掉所有字符包括换行
match = re.search(pattern, user_comment, re.IGNORECASE)

if not match:
    print("❌ ERROR: 无法解析命令格式")
    print("请使用格式：/update_page Page: 文件名 Content: 代码内容（可多行）")
    sys.exit(1)

file_path = match.group(1).strip()
new_content = match.group(2).strip()  # 去掉首尾空白

print(f"✅ 解析成功！")
print(f"文件: {file_path}")
print(f"内容长度: {len(new_content)} 字符")

try:
    full_path = os.path.join(repo_root, file_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ SUCCESS: 已更新 {full_path}")
except Exception as e:
    print(f"❌ 写入失败: {e}")
    sys.exit(1)