# GLSL 語法與資料傳遞

- **Wiki ID**：W02
- **知識狀態**：已整理，待人工複核
- **適用讀者**：有初步電腦圖學基礎的大學生
- **主要來源**：[S02｜LearnOpenGL — Shaders](https://learnopengl.com/Getting-started/Shaders)
- **來源摘要**：[raw/s02-source-note.md](../../raw/s02-source-note.md)
- **來源章節**：Getting-started/Shaders：GLSL、Types、Ins and outs、Uniforms

> 本文是 AI 依公開教材撰寫的繁體中文學習筆記，而非來源逐字翻譯；例子為教學示意。

## 核心概念

GLSL（OpenGL Shading Language）是類似 C 的著色器語言，支援向量（`vec2`、`vec3`、`vec4`）與矩陣（`mat4`），也有 `in`、`out`、`uniform` 等介面宣告。

本 Wiki 的示例以**桌面 OpenGL，GLSL 330 core**為主要脈絡，與 WebGL 1.0 的語法會有所差異。

## 一段簡化的 Vertex Shader（教學示意）

```glsl
#version 330 core
layout (location = 0) in vec3 aPos;
out vec3 vColor;

void main() {
    gl_Position = vec4(aPos, 1.0);
    vColor = vec3(0.2, 0.6, 1.0);
}
```

`aPos` 是每個頂點讀取的 attribute，`gl_Position` 是輸出的齊次裁剪空間位置，`vColor` 可傳遞到下一個 shader stage，經光柵化插值。這只是 Shader 程式片段，不是獨立可執行的完整 OpenGL 應用。

## 核心語法

| 寫法 | 用途 |
|---|---|
| `in` | 宣告輸入 |
| `out` | 宣告輸出 |
| `uniform` | 由程式設定、供 shader 使用的參數 |
| `vec3` | 三個浮點數成分的向量 |
| `mat4` | 4×4 矩陣 |

## 常見誤解

- `vec3` 不一定是座標，也可能是 RGB 或法線。
- 不同版本的 GLSL 不可任意貼上同一套 `attribute`、`varying`、`in`、`out` 寫法。

## 自我檢查

1. `uniform` 和每頂點 `in` 變數有什麼不同？
2. 為何要對齊 GLSL 版本？

## 來源與可追溯性

- 主要依據：S02，LearnOpenGL — Shaders，https://learnopengl.com/Getting-started/Shaders（查閱 2026-11-23）。
- 摘要對照：`raw/s02-source-note.md`。
- 版本提醒：不同 GLSL 版本的關鍵字可能不同；此 Wiki 主線為桌面 OpenGL 的 GLSL 330 core。

## 接著閱讀

- [渲染管線](graphics-pipeline.md)
- [Vertex 與 Fragment Shader](shader-stages.md)

[返回 Wiki 索引](../index.md)
