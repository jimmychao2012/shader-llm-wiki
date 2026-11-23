# 顏色向量與 mix 混色

- **Wiki ID**：W06
- **知識狀態**：已整理，待人工複核
- **適用讀者**：有初步電腦圖學基礎的大學生
- **主要來源**：[S06｜The Book of Shaders — Colors](https://thebookofshaders.com/06/)
- **來源摘要**：[raw/s06-source-note.md](../../raw/s06-source-note.md)
- **來源章節**：Chapter 06：Colors、Mixing color、Playing with gradients

> 本文是 AI 依公開教材撰寫的繁體中文學習筆記，而非來源逐字翻譯；例子為教學示意。

## 核心概念

GLSL 常以 `vec3(r,g,b)` 表示 RGB 三通道數值。`vec3` 的 `.x/.y/.z` 與 `.r/.g/.b` 是同一組分量的不同命名。

`mix(a,b,t)` 是線性插值，對浮點數與向量常可理解成 `a * (1 - t) + b * t`。當 `t` 從 0 變到 1，就可以在兩組顏色之間形成漸層。

```glsl
vec3 blue = vec3(0.1, 0.3, 0.9);
vec3 orange = vec3(1.0, 0.5, 0.1);
float t = 0.25;
vec3 color = mix(blue, orange, t);
```

以上是**自行編寫的概念程式片段**，不是來源網站的原始範例。輸入 `t=0.25` 時，輸出為 75% 的 `blue` 加上 25% 的 `orange`（逐通道插值）。

## 使用提醒

- 這裡討論的是數值插值。實際顯示結果可能受到 gamma、色彩空間與輸出管線影響。
- 如果 `t` 超出 [0,1]，浮點版本的 `mix` 仍可做外插，不應以為一定會自動限制在 [0,1]。

## 常見誤解

- 向量分量名稱不同不代表資料類型不同。
- 線性 RGB 數值插值與人類感知均勻的色彩過渡不是同一個概念。

## 自我檢查

1. `mix(red, blue, 0.0)` 會得到哪一端？
2. 想用時間讓顏色往返變化，應該如何構造介於 0 到 1 的比例？

## 來源與可追溯性

- 主要依據：S06，The Book of Shaders — Colors，https://thebookofshaders.com/06/（查閱 2026-11-23）。
- 摘要對照：`raw/s06-source-note.md`。
- 版本提醒：RGB 值與顯示色彩空間是不同議題；混色教學以簡化數值模型為主。

## 接著閱讀

- [Uniform 與時間控制](uniforms.md)

[返回 Wiki 索引](../index.md)
