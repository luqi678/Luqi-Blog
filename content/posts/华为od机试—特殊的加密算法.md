---
title: P00200. 华为od机试—特殊的加密算法
date: 2026-01-15 18:24:25
excerpt: 在二维数组密码本中查找明文数字串，将路径坐标转换为密文，并返回字典序最小的密文。
tags:
  - 笔试
  - 机考
  - 华为
  - DFS
  - 回溯
  - 矩阵搜索
ODtags:
  - 2024E卷
rating: ⭐⭐⭐
status: complete
destination: 03-Projects/11-笔试/01-华为
obsidianUIMode: source
categories: 华为机考
---

## 一、 题目描述

有一种特殊的加密算法，明文为一段数字串，经过密码本查找转换，生成另一段密文数字串。

**规则如下：**

1.  **明文**：为一段数字串由 0~9 组成。
2.  **密码本**：为数字 0~9 组成的二维数组。
3.  **匹配规则**：需要按明文串的数字顺序在密码本里找到同样的数字串，密码本里的数字串是由相邻的单元格数字组成，上下和左右是相邻的。
    * **注意**：对角线不相邻，同一个单元格的数字不能重复使用。
4.  **加密规则**：每一位明文对应密文即为密码本中找到的单元格所在的行和列序号（序号从0开始）组成的两个数宇。
    * 如明文第 $i$ 位 `Data[i]` 对应密码本单元格为 `Book[x][y]`，则明文第 $i$ 位对应的密文为 `X Y`，`X` 和 `Y` 之间用空格隔开。

**特殊要求：**

* 如果有多条密文，返回字符序最小的密文。
* 如果密码本无法匹配，返回 "error"。

请你设计这个加密程序。

## 二、输入描述

1.  第一行输入 1 个正整数 $N$，代表明文的长度（$1 \le N \le 200$）。
2.  第二行输入 $N$ 个明文组成的序列 `Data[i]`（$0 \le Data[i] \le 9$）。
3.  第三行输入 1 个正整数 $M$，代表密文的长度（此处原题意应为密码本的大小/行数，根据用例推断 $M$ 为矩阵边长）。
4.  接下来 $M$ 行，每行 $M$ 个数，代表密文矩阵（密码本）。

## 三、输出描述

输出字典序最小密文，如果无法匹配，输出 "error"。

## 四、用例

### 用例1
**输入**
```text
2
0 3
3
0 0 2
1 3 4
6 6 4
```
**输出**
```text
0 1 1 1
```

### 用例2
**输入**
```text
2
0 5
3
0 0 2
1 3 4
6 6 4
```
**输出**
```text
error
```
**说明**
> 找不到 0 5 的序列，返回error。

### 用例3
**输入**
```text
6
6 3 8 4 7 6
11
4 0 2 5 2 2 7 8 2 7 4
8 2 5 1 1 4 2 5 5 3 1
5 6 6 6 4 8 3 7 0 3 8
8 8 7 6 8 1 0 8 7 0 3
7 0 4 1 1 3 3 6 7 4 6
6 6 3 7 2 4 0 6 1 2 7
5 0 4 4 8 1 2 5 1 2 8
0 6 0 3 8 8 5 2 8 6 5
5 2 5 8 2 0 7 8 3 6 7
3 0 1 7 2 6 7 4 6 0 7
3 8 2 2 3 4 0 2 1 2 0
```
**说明**
此为复杂匹配测试用例。

### 用例4
**输入**
```text
3
1 2 3
4
1 0 0 0
2 0 0 0
3 4 5 6
7 8 9 0
```

### 用例5
**输入**
```text
3
4 5 6
4
1 2 3 4
5 6 7 8
0 0 0 0
9 0 0 0
```

### 用例6
**输入**
```text
2
0 1
3
0 1 2
0 3 4
1 5 6
```

### 用例7
**输入**
```text
4
6 7 8 9
5
0 0 0 0 0
0 6 7 8 9
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
```

### 用例8
**输入**
```text
4
1 1 1 1
5
1 1 0 0 0
0 0 0 0 0
0 0 1 1 0
0 0 0 0 1
0 0 0 0 0
```

### 用例9
**输入**
```text
4
4 0 0 0
6
0 4 1 0 2 0
3 0 0 4 3 0
1 4 0 3 4 4
0 0 1 1 4 3
1 2 1 0 0 1
0 0 2 3 4 0
```

### 用例10
**输入**
```text
2
8 9
3
0 1 2
3 4 5
6 7 0
```

## 五、备注

* 明文长度 $N$ 最大为 200。
* 矩阵为 $M \times M$。
* 字典序最小意味着比较生成的坐标字符串（例如 "0 1 1 1" < "0 2 0 3"）。

## 六、题目解析

### 1. 题目分析
本题是一个典型的矩阵路径搜索问题，要求在二维网格中寻找一条路径，使得路径上的数字顺序与给定的明文一致。
关键约束条件包括：
* **相邻性**：只能上下左右移动。
* **不重复**：同一个单元格在一次路径中只能使用一次。
* **字典序最小**：如果有多个匹配，返回坐标组合成的字符串字典序最小的那个。

### 2. 解题思路
核心解题思路是通过深度优先搜索（DFS）在一个给定的密码本（二维数组）中找到一条路径。


具体步骤如下：

1.  **初始化**：
    * 读取明文长度 `n` 和明文内容 `data`。
    * 读取密码本大小 `m` 和密码本内容 `book`。
    * 定义方向数组 `directions`（右、下、左、上）。
    * 初始化 `minPath` 用于存储结果，`found` 标记是否找到。

2.  **遍历起点**：
    * 遍历密码本的每一个单元格 `(i, j)`。
    * 如果 `book[i][j]` 等于明文的第一个数字 `data[0]`，则以此为起点启动 DFS。

3.  **深度优先搜索 (DFS)**：
    * **参数**：当前匹配的明文索引 `index`，当前坐标 `(x, y)`，访问标记 `visited`，当前路径字符串 `path`。
    * **终止条件**：如果 `index` 等于明文长度，说明找到了一条完整路径。此时比较 `path` 和 `minPath`，保留字典序较小的那个，并设置 `found = true`。
    * **剪枝与合法性检查**：检查 `(x, y)` 是否越界，是否已访问，或数字是否匹配。如果不满足，直接返回。
    * **递归搜索**：
        * 标记 `(x, y)` 为已访问。
        * 将当前坐标加入路径字符串。
        * 向四个方向（右、下、左、上）尝试移动，递归调用 DFS 寻找 `data[index + 1]`。
        * **回溯**：递归返回后，将 `(x, y)` 的访问标记复位，以便其他路径可以使用该点。

4.  **输出结果**：
    * 如果 `found` 为真，输出 `minPath`。
    * 否则输出 "error"。

### 3. 代码实现

#### C++ 实现
```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

// 全局变量定义
static int n, m; // 分别用于存储明文的长度和密码本的尺寸
vector<vector<int>> book; // 用于存储密码本，是一个二维向量
vector<vector<int>> directions = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}}; // 表示四个搜索方向：右、下、左、上
string minPath = ""; // 用于存储找到的字典序最小的密文路径
bool found = false; // 标记是否找到了至少一种加密方式

// 深度优先搜索函数声明
void dfs(const vector<int>& data, int index, int x, int y, vector<vector<bool>>& visited, string path);

int main() {
    cin >> n; // 读取明文的长度
    vector<int> data(n); // 创建向量存储明文数字
    for (int i = 0; i < n; ++i) {
        cin >> data[i]; // 读取每个明文数字
    }

    cin >> m; // 读取密码本的尺寸
    book.resize(m, vector<int>(m)); // 初始化密码本向量
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> book[i][j]; // 填充密码本内容
        }
    }

    vector<vector<bool>> visited(m, vector<bool>(m, false)); // 标记密码本中的数字是否已经被访问过
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < m; ++j) {
            if (book[i][j] == data[0]) { // 从找到的第一个数字开始搜索
                dfs(data, 0, i, j, visited, ""); // 使用深度优先搜索找到所有可能的加密路径
            }
        }
    }

    cout << (found ? minPath : "error") << endl; // 如果找到至少一种加密方式，输出最小字典序的密文；否则，输出"error"
    return 0;
}

void dfs(const vector<int>& data, int index, int x, int y, vector<vector<bool>>& visited, string path) {
    if (index == n) { // 如果已经处理完所有明文数字
        if (!found || path < minPath) { // 如果找到的是第一种加密方式，或者字典序比之前的小
            minPath = path; // 更新最小字典序密文路径
        }
        found = true; // 标记找到了加密方式
        return;
    }

    if (x < 0 || y < 0 || x >= m || y >= m || visited[x][y] || book[x][y] != data[index]) {
        // 如果坐标越界，或该位置已访问，或该位置数字与明文不匹配，则返回
        return;
    }

    visited[x][y] = true; // 标记当前位置已访问
    
    // 注意：这里需要先判断是否是最后一个字符，或者逻辑稍微调整。
    // 原代码逻辑：在进入下一层前拼接。为了处理最后一位，需要在这一层处理坐标拼接
    // 下面逻辑稍微修正了拼接时机，确保路径完整
    string currentPos = to_string(x) + " " + to_string(y);
    // 如果不是第一个数字，前面加空格（根据题目输出格式，通常数字间有空格）
    // 题目示例："0 1 1 1" -> (0,1) (1,1)。
    // 这里的path传入时是之前的路径。
    string newPath = (path.empty() ? "" : path + " ") + currentPos;

    // 检查是否是最后一个数字
    if (index == n - 1) {
         if (!found || newPath < minPath) {
            minPath = newPath;
        }
        found = true;
        visited[x][y] = false; // 回溯
        return;
    }

    // 遍历四个方向
    for (const auto& dir : directions) {
        int newX = x + dir[0];
        int newY = y + dir[1];
        dfs(data, index + 1, newX, newY, visited, newPath); // 在新方向上搜索下一个明文数字
    }

    visited[x][y] = false; // 回溯，撤销当前位置的访问标记
}
```
**

#### Java 实现
```java
import java.util.*;

public class Main {
    static int n, m; // 分别用于存储明文的长度和密码本的尺寸
    static int[][] book; // 用于存储密码本，是一个二维数组
    static int[][] directions = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}}; // 表示四个搜索方向：右、下、左、上
    static String minPath = ""; // 用于存储找到的字典序最小的密文路径
    static boolean found = false; // 标记是否找到了至少一种加密方式

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        if (scanner.hasNextInt()) {
            n = scanner.nextInt(); // 读取明文的长度
        } else {
            return;
        }
        
        int[] data = new int[n]; // 创建数组存储明文数字
        for (int i = 0; i < n; i++) {
            data[i] = scanner.nextInt(); // 读取每个明文数字
        }

        m = scanner.nextInt(); // 读取密码本的尺寸
        book = new int[m][m]; // 初始化密码本数组
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < m; j++) {
                book[i][j] = scanner.nextInt(); // 填充密码本内容
            }
        }

        boolean[][] visited = new boolean[m][m]; // 标记密码本中的数字是否已经被访问过
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < m; j++) {
                if (book[i][j] == data[0]) { // 从找到的第一个数字开始搜索
                    dfs(data, 0, i, j, visited, ""); // 使用深度优先搜索找到所有可能的加密路径
                }
            }
        }

        System.out.println(found ? minPath.trim() : "error"); // 如果找到至少一种加密方式，输出最小字典序的密文；否则，输出"error"
    }

    public static void dfs(int[] data, int index, int x, int y, boolean[][] visited, String path) {
        // 边界和匹配检查
        if (x < 0 || y < 0 || x >= m || y >= m || visited[x][y] || book[x][y] != data[index]) {
            return;
        }

        visited[x][y] = true; // 标记当前位置已访问
        String currentPos = x + " " + y;
        String newPath = path.equals("") ? currentPos : path + " " + currentPos;

        if (index == n - 1) { // 如果已经处理完所有明文数字
            if (!found || newPath.compareTo(minPath) < 0) { // 如果找到的是第一种加密方式，或者字典序比之前的小
                minPath = newPath; // 更新最小字典序密文路径
            }
            found = true; // 标记找到了加密方式
            visited[x][y] = false; // 回溯
            return;
        }

        for (int[] dir : directions) { // 遍历四个方向
            int newX = x + dir[0];
            int newY = y + dir[1];
            dfs(data, index + 1, newX, newY, visited, newPath); // 在新方向上搜索下一个明文数字
        }

        visited[x][y] = false; // 回溯，撤销当前位置的访问标记
    }
}
```
**

#### Python 实现
```python
import sys

# 增加递归深度以防万一
sys.setrecursionlimit(2000)

def solve():
    try:
        line1 = sys.stdin.readline()
        if not line1: return
        n = int(line1.strip())
        
        line2 = sys.stdin.readline()
        if not line2: return
        data = list(map(int, line2.split()))
        
        line3 = sys.stdin.readline()
        if not line3: return
        m = int(line3.strip())
        
        book = []
        for _ in range(m):
            book.append(list(map(int, sys.stdin.readline().split())))
    except ValueError:
        return

    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # 四个搜索方向：右、下、左、上
    min_path = None  # 存储找到的字典序最小的密文路径
    found = False  # 标记是否找到至少一种加密方式

    def dfs(index, x, y, visited, path):
        nonlocal min_path, found
        
        # 边界与匹配检查
        if x < 0 or y < 0 or x >= m or y >= m or visited[x][y] or book[x][y] != data[index]:
            return

        visited[x][y] = True
        current_pos = f"{x} {y}"
        new_path = path + " " + current_pos if path else current_pos

        if index == len(data) - 1:
            if not found or new_path < min_path:
                min_path = new_path
            found = True
            visited[x][y] = False
            return

        for dx, dy in directions:
            newX, newY = x + dx, y + dy
            dfs(index + 1, newX, newY, visited, new_path)

        visited[x][y] = False  # 回溯

    visited = [[False for _ in range(m)] for _ in range(m)]
    for i in range(m):
        for j in range(m):
            if book[i][j] == data[0]:
                dfs(0, i, j, visited, "")

    print(min_path if found else "error")

if __name__ == "__main__":
    solve()
```
**

#### JavaScript 实现
```javascript
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let inputLines = [];

rl.on('line', function(line) {
  if(line.trim() !== '') {
      inputLines.push(line.trim());
  }
}).on('close', function() {
  if (inputLines.length === 0) return;

  let lineIdx = 0;
  const n = parseInt(inputLines[lineIdx++]);
  const data = inputLines[lineIdx++].split(/\s+/).map(Number);
  const m = parseInt(inputLines[lineIdx++]);
  
  let book = [];
  for(let i=0; i<m; i++){
      book.push(inputLines[lineIdx++].split(/\s+/).map(Number));
  }

  const directions = [[0, 1], [1, 0], [-1, 0], [0, -1]];
  let minPath = "";
  let found = false;
  const visited = Array.from({length: m}, () => Array(m).fill(false));

  function dfs(index, x, y, path) {
      if (x < 0 || y < 0 || x >= m || y >= m || visited[x][y] || book[x][y] !== data[index]) {
          return;
      }

      visited[x][y] = true;
      const currentPos = `${x} ${y}`;
      const newPath = path === "" ? currentPos : path + " " + currentPos;

      if (index === n - 1) {
          if (!found || newPath < minPath) {
              minPath = newPath;
          }
          found = true;
          visited[x][y] = false;
          return;
      }

      for (const [dx, dy] of directions) {
          dfs(index + 1, x + dx, y + dy, newPath);
      }

      visited[x][y] = false;
  }

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < m; j++) {
      if (book[i][j] === data[0]) {
        dfs(0, i, j, "");
      }
    }
  }

  console.log(found ? minPath : "error");
});
```
**

#### C语言 实现
```c
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

#define MAX_SIZE 100 // 密码本的最大尺寸
#define PATH_LEN 2000 // 路径字符串的最大长度，根据N=200调整

int n, m;
int book[MAX_SIZE][MAX_SIZE];
int directions[4][2] = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
char minPath[PATH_LEN] = "";
bool found = false;

void dfs(int data[], int index, int x, int y, bool visited[MAX_SIZE][MAX_SIZE], char path[PATH_LEN]) {
    if (x < 0 || y < 0 || x >= m || y >= m || visited[x][y] || book[x][y] != data[index]) {
        return;
    }

    visited[x][y] = true;
    
    char newPath[PATH_LEN];
    strcpy(newPath, path);
    char temp[20];
    if (strlen(path) > 0) {
        sprintf(temp, " %d %d", x, y);
    } else {
        sprintf(temp, "%d %d", x, y);
    }
    strcat(newPath, temp);

    if (index == n - 1) {
        if (!found || strcmp(newPath, minPath) < 0) {
            strcpy(minPath, newPath);
        }
        found = true;
        visited[x][y] = false; // 回溯
        return;
    }

    for (int i = 0; i < 4; i++) {
        int newX = x + directions[i][0];
        int newY = y + directions[i][1];
        dfs(data, index + 1, newX, newY, visited, newPath);
    }

    visited[x][y] = false; // 回溯
}

int main() {
    if (scanf("%d", &n) != 1) return 0;
    int data[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &data[i]);
    }

    if (scanf("%d", &m) != 1) return 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d", &book[i][j]);
        }
    }

    bool visited[MAX_SIZE][MAX_SIZE] = {false};
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            if (book[i][j] == data[0]) {
                dfs(data, 0, i, j, visited, "");
            }
        }
    }

    if (found) {
        printf("%s\n", minPath);
    } else {
        printf("error\n");
    }

    return 0;
}
```
**

### 4. 复杂度分析
* **时间复杂度**：最坏情况下，对于每个起始点都需要进行 DFS。DFS 的深度为 $N$，每个节点最多有 4 个分支（上下左右）。理论最坏时间复杂度为 $O(M^2 \times 3^N)$（实际上由于 `visited` 数组和数字匹配限制，分支数远小于 4）。但在本题数据规模下（$N \le 200, M$ 未知但通常较小），加上剪枝，可以通过。
* **空间复杂度**：$O(M^2)$ 用于存储密码本和 `visited` 数组，递归调用栈的深度为 $O(N)$。

## 引用

[1] (200分) - 特殊的加密算法（Java & Python& JS & C++ & C ）.html
[4] C++ Code Snippet from Source
[5] Java Code Snippet from Source
[6] JavaScript Code Snippet from Source
[7] Python Code Snippet from Source
[8] C Code Snippet from Source

**版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。**
```