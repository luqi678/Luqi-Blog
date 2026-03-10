---
title: 华为od机试—图论基础：BFS与DFS算法详解
date: 2026-01-03 17:35:43
excerpt: 深度优先搜索(DFS)与广度优先搜索(BFS)的核心原理、应用场景及Java代码模板总结。
tags:
  - 算法
  - 图论
  - BFS
  - DFS
  - 搜索
rating: ⭐⭐⭐⭐
status: complete
destination: 03-Projects/11-笔试/01-华为
obsidianUIMode: source
categories: 华为机考
---

## 1. 基本概念

图的搜索算法是遍历图中节点的基础方法。



- **DFS (Depth-First Search，深度优先搜索)**：
    - **定义**：一种用于遍历或搜索树或图的算法。沿着树的深度遍历树的节点，尽可能深地搜索树的分支。
    - **核心要素**：**栈 (Stack)**（通常通过**递归**隐式实现），**回溯**。

- **BFS (Breadth-First Search，广度优先搜索)**：
    - **定义**：从根节点开始，沿着树的宽度遍历树的节点。如果所有节点均被访问，则算法中止。
    - **核心要素**：**队列 (Queue)**，**层级**。

## 2. 解决什么问题

常见的应用场景区分：

| 算法 | 核心应用场景 | 典型例题 |
| :--- | :--- | :--- |
| **DFS** | 1. **连通性问题**：判断两点是否相通。<br>2. **路径存在性**：是否存在一条路径。<br>3. **回溯算法**：排列组合、全排列、N皇后。<br>4. **拓扑排序**、**检测环**。 | 岛屿数量、全排列、二叉树的最大深度 |
| **BFS** | 1. **最短路径问题**（无权图）：从起点到终点的最少步数。<br>2. **层序遍历**：二叉树的层序打印。<br>3. **多源BFS**：从多个起点同时扩散（如腐烂的橘子）。 | 迷宫最短路、二叉树层序遍历、网络延迟时间 |

## 3. 基本思想和策略

- **DFS (一条路走到黑)**：
    - **核心思想**：不撞南墙不回头。从一个节点出发，访问其一个邻接点，再以该邻接点为起点继续访问，直到没有未访问的邻接点，然后**回溯**到上一个节点，继续访问其他分支。
    
- **BFS (层层推进)**：
    - **核心思想**：像水波纹一样扩散。从起点出发，先访问离起点最近的所有节点（第一层），然后再访问离起点次近的所有节点（第二层），依此类推。

## 4. 求解步骤

### DFS 步骤
1.  **访问**当前节点并标记为已访问。
2.  对当前节点的每一个**未访问**的邻接节点，递归执行步骤 1。
3.  如果当前节点没有未访问的邻接点，则**回溯**。

### BFS 步骤
1.  将起点放入**队列**，并标记为已访问。
2.  若队列不为空，取出队首节点。
3.  将该节点的所有**未访问**邻接节点加入队列，并标记为已访问。
4.  重复步骤 2-3，直到队列为空。

## 5. 常见类型与算法实现（Java 标准模板）

### 类型一：DFS (递归实现 - 最常用)

适用于树的遍历、图的连通性检测、全排列等。

**代码模板**：

```java
import java.util.*;

class Solution {
    // 标记数组，防止重复访问
    boolean[] visited; 
    // 图的邻接表表示
    List<List<Integer>> graph; 

    public void dfsTraversal(int n, List<List<Integer>> edges) {
        // 1. 建图 (如果题目没给邻接表)
        graph = new ArrayList<>();
        for(int i = 0; i < n; i++) graph.add(new ArrayList<>());
        for(List<Integer> edge : edges) {
            graph.get(edge.get(0)).add(edge.get(1));
            // 如果是无向图，需添加反向边
            graph.get(edge.get(1)).add(edge.get(0)); 
        }

        visited = new boolean[n];
        
        // 处理非连通图的情况，遍历所有节点
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i);
            }
        }
    }

    // DFS 核心递归函数
    private void dfs(int u) {
        // 1. 标记当前节点已访问
        visited[u] = true;
        System.out.print(u + " "); // 处理节点逻辑

        // 2. 遍历邻接节点
        for (int v : graph.get(u)) {
            if (!visited[v]) {
                // 3. 递归调用
                dfs(v);
            }
        }
    }
}
```

### 类型二：BFS (队列实现 - 最短路必用)

适用于求无权图最短路径、层序遍历。

**代码模板**：

```java
import java.util.*;

class Solution {
    public void bfs(int startNode, int n, List<List<Integer>> graph) {
        // 1. 初始化队列和访问数组
        Queue<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[n];
        
        // 2. 起点入队并标记
        queue.offer(startNode);
        visited[startNode] = true;
        
        int step = 0; // 记录步数/层级

        // 3. 队列不为空时循环
        while (!queue.isEmpty()) {
            int size = queue.size(); // 当前层的节点数
            
            // 遍历当前层的所有节点
            for (int i = 0; i < size; i++) {
                int curr = queue.poll();
                System.out.println("Visiting: " + curr + " at step " + step);
                
                // 处理邻接节点
                for (int neighbor : graph.get(curr)) {
                    if (!visited[neighbor]) {
                        queue.offer(neighbor);
                        visited[neighbor] = true; // 关键：入队时立即标记，防止重复入队
                    }
                }
            }
            step++; // 遍历完一层，步数+1
        }
    }
}
```

### 类型三：网格图搜索 (机考常考 - 岛屿/迷宫)

**特点**：图是二维矩阵，使用方向数组 `dirs` 控制移动。

**代码模板 (以 BFS 为例)**：

```java
class Solution {
    // 方向数组：上、下、左、右
    int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public int bfsGrid(char[][] grid) {
        int m = grid.length, n = grid[0].length;
        Queue<int[]> queue = new LinkedList<>();
        boolean[][] visited = new boolean[m][n];
        
        // 假设从 (0,0) 出发
        queue.offer(new int[]{0, 0});
        visited[0][0] = true;
        int distance = 0;
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] curr = queue.poll();
                int x = curr[0], y = curr[1];
                
                // 尝试向四个方向移动
                for (int[] dir : dirs) {
                    int nx = x + dir[0];
                    int ny = y + dir[1];
                    
                    // 越界检查 和 访问检查
                    if (nx >= 0 && nx < m && ny >= 0 && ny < n 
                        && !visited[nx][ny] && grid[nx][ny] != '#') { // '#' 假设为障碍
                        
                        queue.offer(new int[]{nx, ny});
                        visited[nx][ny] = true;
                    }
                }
            }
            distance++;
        }
        return -1; // 无法到达
    }
}
```

---

## 6. 总结与对比表 (一图胜千言)

| 维度 | DFS (深度优先) | BFS (广度优先) |
| :--- | :--- | :--- |
| **数据结构** | **栈 (Stack)** / 递归 | **队列 (Queue)** |
| **空间复杂度** | $O(h)$ (h为树高)，通常较小 | $O(w)$ (w为最大宽度)，通常较大 |
| **路径特性** | 不一定是最短路径 | **无权图中必定是最短路径** |
| **访问顺序** | 纵向挖掘，深度优先 | 横向铺开，层层推进 |
| **典型应用** | 连通性、全排列、回溯 | 最短路、层序遍历、泛洪填充 |

### 记忆口诀

> **BFS 找最短，队列一层层推；**
> **DFS 搜到底，递归回溯显神威。**

## 引用

**版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。**