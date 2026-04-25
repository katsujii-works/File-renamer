import os

folder_path = "folder"  # フォルダ名

files = os.listdir(folder_path)

for i, file in enumerate(files):
    old_path = os.path.join(folder_path, file)
    
    new_name = f"file_{i+1}.jpg"
    new_path = os.path.join(folder_path, new_name)
    
    os.rename(old_path, new_path)

print("完了！")
