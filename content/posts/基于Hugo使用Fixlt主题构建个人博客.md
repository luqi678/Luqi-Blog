---
title: 📝基于Hugo使用Fixlt主题构建个人博客
date: 2025-06-17
categories:
  - 教程
tags:
  - Hugo
  - Fixlt
status: 
destination: 
draft: false
---
# 基于Hugo使用Fixlt主题构建个人博客

## 安装Hugo
### 1️⃣ 安装 Hugo

-   访问官网下载：https://gohugo.io/getting-started/installing/
    
-   推荐使用 [Chocolatey](https://chocolatey.org/)：
```
choco install hugo-extended -confirm
```
-   检查是否安装成功：
    
```
hugo version
```

> ❗ 注意：一定要安装带 `extended` 的版本，才能支持一些主题依赖 SCSS 的功能。


## 安装Fixlt主题
[FixIt - Hugo 主题 官网](https://pre.fixit.lruihao.cn/zh-cn/)

### Git 子模块[](https://pre.fixit.lruihao.cn/zh-cn/documentation/installation/#git-submodule)

[点击快速创建博客！ https://github.com/hugo-fixit/hugo-fixit-starter1/generate](https://github.com/hugo-fixit/hugo-fixit-starter1/generate "一个基于 Git 子模块创建 Hugo FixIt 站点的快速启动模板。")

在当前目录中初始化一个空的 Git 存储库。

    git init

将 [FixIt](https://github.com/hugo-fixit/FixIt) 添加到你的项目中，作为一个 [Git 子模块](https://git-scm.com/book/en/v2/Git-Tools-Submodules) 存储在 `themes` 目录中的。

    git submodule add https://github.com/hugo-fixit/FixIt.git themes/FixIt

要使用 `dev` 分支上的版本，可以使用以下命令：

    git submodule add -b dev https://github.com/hugo-fixit/FixIt.git themes/FixIt
    
    # 或者，将子模块分支从 `main` 切换到 `dev`：
    git submodule set-branch -b dev themes/FixIt

使用以下命令升级主题：

    git submodule update --remote --merge themes/FixIt

 稳定版 release 
 https://github.com/hugo-fixit/FixIt/releases


## 启动命令
```cmd
hogo server
```

## 引用
[基于EasyExcel+线程池+定时轮询服务解决POI文件导出大量数据时的内存溢出及超时问题](03-Projects/05-语雀/download/积累/项目亮点&难点/基于EasyExcel+线程池+定时轮询服务解决POI文件导出大量数据时的内存溢出及超时问题.md)