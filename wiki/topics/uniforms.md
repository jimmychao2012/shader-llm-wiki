# Uniform 與時間控制

- **Wiki ID**：W05
- **知識狀態**：已整理，待人工複核
- **適用讀者**：有初步電腦圖學基礎的大學生
- **主要來源**：[S05｜The Book of Shaders — Uniforms](https://thebookofshaders.com/03/)
- **來源摘要**：[raw/s05-source-note.md](../../raw/s05-source-note.md)
- **來源章節**：Chapter 03：Uniforms、u_time、u_resolution、u_mouse

> 本文是 AI 依公開教材撰寫的繁體中文學習筆記，而非來源逐字翻譯；例子為教學示意。

## 核心概念

`uniform` 是讓應用程式把參數傳給 shader 的介面：同一次 draw call 內的 shader invocation 可讀取該 uniform 變數的相同值。適合傳遞時間、解析度、顏色或變換矩陣等。

The Book of Shaders 的 `u_time`、`u_resolution`、`u_mouse` **不是 GLSL 自動存在的內建變數**；它們是教材範例採用的命名規則，實際上需要由宿主程式設定。

## 動畫概念

```glsl
uniform float u_time;
float pulse = 0.5 + 0.5 * sin(u_time);
```

此式可以把 `sin` 的 [-1, 1] 變化映射成 [0, 1]；例如用來控制顏色混合比率。這段範例不包含宿主程式的 uniform 設定，也不代表已經實際在 GPU 執行。

## 和頂點屬性有何差別？

- 頂點屬性可在一個 draw call 中隨著不同頂點而不同。
- uniform 在同一個 draw call 中對讀取它的 shader invocation 維持一致。

## 常見誤解

- `u_time` 名稱不具有標準化魔法功能。
- 需要動態效果不代表要修改或重編 Shader 原始碼；可更新 uniform 值。

## 自我檢查

1. 哪一類資料適合 uniform？
2. `u_mouse` 是否由 GLSL 自動更新？

## 來源與可追溯性

- 主要依據：S05，The Book of Shaders — Uniforms，https://thebookofshaders.com/03/（查閱 2026-11-23）。
- 摘要對照：`raw/s05-source-note.md`。
- 版本提醒：u_time/u_mouse/u_resolution 是教材的命名慣例，不是 GLSL 強制內建變數。

## 接著閱讀

- [矩陣變換與頂點位置](transformations.md)
- [顏色向量與 mix 混色](colors-and-mix.md)

[返回 Wiki 索引](../index.md)
