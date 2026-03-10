# 使用方式 python update_md_props.py -d /你的/文件夹/路径 -c "随笔"

import os
import argparse

def process_md_file(file_path, category_value):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"读取文件失败 {file_path}: {e}")
        return

    # 判断文件是否有内容，以及是否有合法的 YAML Front Matter
    if not lines or lines[0].strip() != '---':
        # 文件开头没有 Front Matter，直接在头部创建一个新的
        new_lines = [
            "---\n",
            f"categories: {category_value}\n",
            "---\n"
        ] + lines
    else:
        in_front_matter = True
        has_categories = False
        front_matter_end_idx = -1
        new_lines = []
        
        for i, line in enumerate(lines):
            # 保留第一行的 ---
            if i == 0:
                new_lines.append(line)
                continue
            
            if in_front_matter:
                # 遇到第二个 ---，说明 Front Matter 结束
                if line.strip() == '---':
                    in_front_matter = False
                    front_matter_end_idx = len(new_lines)
                    new_lines.append(line)
                    continue
                
                # 规则 1：如果有 share 属性，删除该属性（即跳过不写入）
                if line.startswith('share:'):
                    continue
                
                # 检查是否已经存在 categories 属性
                if line.startswith('categories:'):
                    has_categories = True
                    
                new_lines.append(line)
            else:
                # Front Matter 之外的正文内容直接保留
                new_lines.append(line)
        
        # 规则 2：如果没有 categories 属性，在 Front Matter 结束前添加
        if not has_categories and front_matter_end_idx != -1:
            new_lines.insert(front_matter_end_idx, f"categories: {category_value}\n")

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"成功处理: {file_path}")
    except Exception as e:
        print(f"写入文件失败 {file_path}: {e}")

def main():
    # 配置命令行参数解析
    parser = argparse.ArgumentParser(description="批量修改 Markdown 文件的 Front Matter 属性")
    parser.add_argument("-d", "--dir", type=str, default=".", help="指定 Markdown 文件所在目录 (默认: 当前运行目录)")
    parser.add_argument("-c", "--category", type=str, default="教程", help="指定 categories 属性的值 (默认: 教程)")
    
    args = parser.parse_args()
    
    target_dir = args.dir
    category_val = args.category
    
    if not os.path.exists(target_dir):
        print(f"错误: 目录 '{target_dir}' 不存在。")
        return
        
    count = 0
    # 遍历目录及其所有子目录
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.lower().endswith('.md'):
                file_path = os.path.join(root, file)
                process_md_file(file_path, category_val)
                count += 1
                
    print(f"\n处理完成！共检查了 {count} 个 Markdown 文件。")

if __name__ == "__main__":
    main()