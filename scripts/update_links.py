import os
import re

def update_links_in_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    updated_content = re.sub(r'\[(.*?)\]\((.*?\.md)\)', lambda m: f"[{m.group(1)}]({m.group(2)[:-3]})", content)

    if updated_content != content:
        with open(file_path, 'w') as file:
            file.write(updated_content)
        return True
    return False

def walk_through_files():
    changed = False
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                if update_links_in_file(file_path):
                    changed = True
    return changed

if __name__ == "__main__":
    if walk_through_files():
        exit(0)  # Files were changed
    else:
        exit(1)  # No changes made