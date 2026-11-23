# Vertex 與 Fragment Shader

- **Wiki ID**：W03
- **知識狀態**：已整理，待人工複核
- **適用讀者**：有初步電腦圖學基礎的大學生
- **主要來源**：[S03｜WebGL Fundamentals — WebGL Shaders and GLSL](https://webglfundamentals.org/webgl/lessons/webgl-shaders-and-glsl.html)
- **來源摘要**：[raw/s03-source-note.md](../../raw/s03-source-note.md)
- **來源章節**：WebGL Shaders and GLSL：Vertex Shader、Fragment Shader、Attributes、Uniforms

> 本文是 AI 依公開教材撰寫的繁體中文學習筆記，而非來源逐字翻譯；例子為教學示意。

## 核心概念

Vertex Shader 與 Fragment Shader 分工不同。**Vertex Shader** 對輸入頂點執行計算，核心輸出是裁剪空間位置 `gl_Position`；**Fragment Shader** 對光柵化產生的片段計算輸出，最常見的是顏色。

## 對照

| 面向 | Vertex Shader | Fragment Shader |
|---|---|---|
| 處理單位 | 頂點 | 片段 |
| 常見輸入 | 頂點位置、顏色、法線、UV | 從前面階段插值過來的資料 |
| 常見輸出 | `gl_Position`、傳遞變數 | 顏色或其他 fragment outputs |
| 典型任務 | 座標變換 | 材質／顏色計算 |

## 資料怎麼從頂點傳到片段？

在 GLSL 330 core，可在 Vertex Shader 使用 `out vec3 vColor;`，Fragment Shader 宣告 `in vec3 vColor;`。對應的變數由管線連接；在預設平滑插值模式下，三角形內部的片段收到插值後的值。

## 注意 API 版本

本來源教材使用 **WebGL 1.0** 的 `attribute` 與 `varying`。桌面 OpenGL GLSL 330 core 常使用 `in` 與 `out`。這是兩種環境的對應觀念，不是能直接混合貼上的原始碼。

## 常見誤解

- Vertex Shader 不需要替整個三角形逐像素上色。
- Fragment Shader 執行次數不等於可見螢幕像素數（深度、覆蓋與多重取樣等情況會影響）。

## 自我檢查

1. `gl_Position` 應該在哪個 Shader 指定？
2. 為何 `varying` 範例不能直接當成 GLSL 330 core 程式？

## 來源與可追溯性

- 主要依據：S03，WebGL Fundamentals — WebGL Shaders and GLSL，https://webglfundamentals.org/webgl/lessons/webgl-shaders-and-glsl.html（查閱 2026-11-23）。
- 摘要對照：`raw/s03-source-note.md`。
- 版本提醒：WebGL1 的 attribute/varying 與 GLSL 330 core 的 in/out 不可直接混用；fragment 不等同於最終螢幕 pixel。

## 接著閱讀

- [GLSL 語法與資料傳遞](glsl-basics.md)
- [矩陣變換與頂點位置](transformations.md)

[返回 Wiki 索引](../index.md)
