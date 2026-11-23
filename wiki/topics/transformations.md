# 矩陣變換與頂點位置

- **Wiki ID**：W04
- **知識狀態**：已整理，待人工複核
- **適用讀者**：有初步電腦圖學基礎的大學生
- **主要來源**：[S04｜LearnOpenGL — Transformations](https://learnopengl.com/Getting-started/Transformations)
- **來源摘要**：[raw/s04-source-note.md](../../raw/s04-source-note.md)
- **來源章節**：Getting-started/Transformations：Matrices、Matrix multiplication、In practice

> 本文是 AI 依公開教材撰寫的繁體中文學習筆記，而非來源逐字翻譯；例子為教學示意。

## 核心概念

模型幾何常需要平移（translation）、旋轉（rotation）與縮放（scale）。用矩陣組合可以重複應用到多個頂點，不需手動逐一重寫位置陣列。

## 齊次座標與矩陣

位置可表示為 `vec4(x, y, z, 1.0)`，再與 `mat4` 相乘。`w=1` 讓平移能透過 4×4 矩陣表示。方向向量若使用 `w=0`，則不受平移部分影響。

```glsl
#version 330 core
layout (location = 0) in vec3 aPos;
uniform mat4 transform;
void main() {
    gl_Position = transform * vec4(aPos, 1.0);
}
```

這是單一示意；在完整 3D 渲染常分別處理 Model、View、Projection（MVP）矩陣。

## 為何順序重要？

矩陣乘法通常**不具交換律**。例如先縮放再平移，與先平移再縮放，物體的最終位置可能不同。採用列向量表示時，`P * V * M * position` 由右往左套用。

## 常見誤解

- 不是任何座標都能直接當成 clip space 輸出。
- 縮放與旋轉的順序未必可以交換。

## 自我檢查

1. 使用 `vec4(position,1.0)` 的第四個值有什麼作用？
2. 為何要小心矩陣相乘順序？

## 來源與可追溯性

- 主要依據：S04，LearnOpenGL — Transformations，https://learnopengl.com/Getting-started/Transformations（查閱 2026-11-23）。
- 摘要對照：`raw/s04-source-note.md`。
- 版本提醒：變換矩陣順序不交換；當使用齊次座標時 translation 需要 4D 表示。

## 接著閱讀

- [Vertex 與 Fragment Shader](shader-stages.md)
- [Uniform 與時間控制](uniforms.md)

[返回 Wiki 索引](../index.md)
