import os

# 标签文件夹路径
label_dir = "valid/labels"  # 替换为你的标签文件夹路径

# 遍历所有标签文件
for label_file in os.listdir(label_dir):
    if label_file.endswith(".txt"):
        file_path = os.path.join(label_dir, label_file)

        # 读取标签文件内容
        with open(file_path, "r") as f:
            lines = f.readlines()

        # 修改每一行的类别索引为1
        new_lines = []
        for line in lines:
            parts = line.split()
            if len(parts) == 5:  # 确保每行有5个值（class_id, x_center, y_center, w, h）
                parts[0] = "1"  # 将类别索引改为1
                new_lines.append(" ".join(parts) + "\n")  # 重新拼接行
            else:
                print(f"文件 {label_file} 中的行格式错误: {line}")

        # 将修改后的内容写回文件
        with open(file_path, "w") as f:
            f.writelines(new_lines)

print("类别索引已全部修改为1！")