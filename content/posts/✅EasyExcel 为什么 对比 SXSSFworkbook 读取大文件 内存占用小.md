---
title: 📝EasyExcel 为什么 对比 SXSSFworkbook 读取大文件 内存占用小
date: 2025-06-18
categories:
  - 面试
tags:
  - EasyExcel
  - 文件管理
  - POI
status: complete
destination: 
draft: false
---

# EasyExcel 为什么比 SXSSFWorkbook 读取大文件内存占用小？

## 一、核心结论

**EasyExcel 在读取大 Excel 文件时内存占用更小，主要是因为它采用了 SAX 事件驱动的流式读取方式，而 SXSSFWorkbook 本质仍依赖 DOM 模式读取。**

---

## 二、技术实现对比

### 1. EasyExcel 使用 SAX（事件驱动）模式读取

- 使用 `SAX`（Simple API for XML）解析 `.xlsx` 文件的 XML 内容。
    
- 不加载整个文件到内存中，**逐行读取、即读即处理**。
    
- 内存占用非常小，适合处理百万级数据。
    

```java
EasyExcel.read(inputStream, MyModel.class, new MyListener()).sheet().doRead();
```

---

### 2. SXSSFWorkbook 是写优化工具，读取仍基于 XSSFWorkbook

- `SXSSFWorkbook` 是 Apache POI 的 **写优化版本**，用于写入大数据量时避免 OOM。
    
- **读取时依旧基于 `XSSFWorkbook`（DOM 模式）**，一次性加载整个工作簿进内存。
    
- 即使搭配 `StreamingReader`，效果也远不如 EasyExcel 的 SAX。
    

---

## 三、读取模式对比

|特性|EasyExcel (SAX)|SXSSFWorkbook (DOM)|
|---|---|---|
|解析方式|SAX|DOM|
|内存占用|低|高|
|支持大文件|是（百万级）|有限（几十万易 OOM）|
|是否流式读取|是|否|
|写入优化|一般|是（用于写入）|

---

## 四、案例说明

### 假设场景：

一个 `.xlsx` 文件，包含 **100 万行、20 列** 数据。

#### EasyExcel 读取：

- 只保留当前读取行的内存对象；
    
- 假设单行数据约 2KB；
    
- 内存峰值保持在 2MB ~ 10MB。
    

#### SXSSFWorkbook 读取：

- 加载全部数据到内存；
    
- 可能占用几百 MB ~ 几 GB；
    
- 高风险触发 OOM。
    

---

## 五、写入时 EasyExcel 也更节省内存

- 虽底层依赖 `SXSSFWorkbook`，但 EasyExcel 封装了写入过程；
    
- 自动进行缓存、刷新、释放等控制；
    
- 支持配置写入缓存大小等参数。
    

---

## 六、总结

|原因|说明|
|---|---|
|✅ SAX 流式解析|EasyExcel 使用 SAX，不加载整个工作簿到内存|
|⛔ SXSSF 是写优化|SXSSFWorkbook 是为写而优化，读取仍依赖 XSSF|
|✅ 行级事件处理|EasyExcel 逐行处理并即时释放对象|
|✅ 不依赖中间结构|不构造 workbook/sheet/row 等对象树，节省大量对象分配和 GC 压力|

---

## 七、建议

如需进一步节省内存并处理大文件，推荐使用：

- `EasyExcel` 的事件监听读取模式
    
- 自定义模型类避免大对象嵌套
    
- 分 Sheet 读取，避免一次读取整个文件
    

---


## 引用

**版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。**
