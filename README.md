---
title: 📝READE
date: 2025-07-01 14:43:33
tags: 
status: 
destination:
---
# READE

## 运行
### 本地调试
```
hugo server -D
```

### 格式修改
```
# post 目录下执行python脚本
python update_md_props.py -d /你的/文件夹/路径 -c "随笔"
-d 可不输入，默认当前目录下
-c 收入目录，可不输入，默认"教程"，建议填入
```

## 发布流程
```
# 1. 删除旧的 public 文件夹（可选，确保干净） 
rm -rf public 
# 2. 构建静态文件 
hugo 
# 如果使用了特定主题或草稿，可以加参数如 
hugo -t FixIt 
# 3. 进入 public 目录 
cd public 
# 4. Git 操作 
git init git add . 
git commit -m "Publishing to github pages" 
# 5. 推送到你的发布仓库（请替换为你自己的地址） 
git push -f git@github.com:用户名/仓库名.git master
```

## 引用
