# 渲染管線

- **Wiki ID**：W01
- **知識狀態**：已整理，待人工複核
- **適用讀者**：有初步電腦圖學基礎的大學生
- **主要來源**：[S01｜LearnOpenGL — Hello Triangle](https://learnopengl.com/Getting-started/Hello-Triangle)
- **來源摘要**：[raw/s01-source-note.md](../../raw/s01-source-note.md)
- **來源章節**：Getting-started/Hello-Triangle：graphics pipeline 與 shader stages

> 本文是 AI 依公開教材撰寫的繁體中文學習筆記，而非來源逐字翻譯；例子為教學示意。

## 核心概念

OpenGL 圖形管線（graphics pipeline）把頂點資料轉換為可在畫面上顯示的片段結果。要辨認**資料流**與**可程式化階段**：並不是每一步都會執行自己寫的 Shader。

一個便於初學者理解的順序是：**頂點資料 → Vertex Shader → 圖元組裝 → 光柵化（Rasterization）→ Fragment Shader → 逐片段測試／混合 → Framebuffer**。這是教學上的簡化，不代表所有 OpenGL 設定都完全相同。

## 必須理解的三件事

1. 頂點包含位置以及可能的顏色、法線、UV 等屬性。
2. 光柵化把三角形覆蓋的區域轉成片段（fragments），並插值頂點輸出。
3. 片段輸出仍可能受深度、模板與混合等操作影響，不保證直接變成最終螢幕像素。

## 概念小例子

三角形有三個頂點，Vertex Shader 逐頂點計算位置；光柵化找出三角形覆蓋區域；Fragment Shader 再為片段計算顏色。這可以解釋為何「三個頂點」卻能形成許多有顏色的區域。

## 常見誤解

- **誤解：整個渲染流程都是 Shader。** 實際有固定功能階段。
- **誤解：Fragment 等於 Pixel。** 片段是管線中待處理的候選資料，可能被測試淘汰。

## 自我檢查

1. Rasterization 在 Vertex Shader 之前還是之後？
2. 為什麼 Fragment Shader 的輸出不一定等於最終畫素？

## 來源與可追溯性

- 主要依據：S01，LearnOpenGL — Hello Triangle，https://learnopengl.com/Getting-started/Hello-Triangle（查閱 2026-11-23）。
- 摘要對照：`raw/s01-source-note.md`。
- 版本提醒：圖元組裝、光柵化、著色器階段的順序；並非所有管線階段都是可程式化 Shader。

## 接著閱讀

- [GLSL 語法與資料傳遞](glsl-basics.md)

[返回 Wiki 索引](../index.md)
