# Shader LLM Wiki｜知識總索引

> **對象**：已學過一些電腦圖學的大學生。**版本範圍**：主要使用桌面 OpenGL / GLSL 330 core 講解；WebGL 1 的語法差異另行標註。

本 Wiki 是具備資料來源、主題條目、交叉連結與 ingest 紀錄的本地 Markdown 知識庫。**不是 HTML 簡報**。所有來源摘要都是自行整理，未大量複製原始教材。

## 建議閱讀順序

| 順序 | 主題 | 來源 | 核心問題 |
|---|---|---|---|
| 1 | [渲染管線](topics/graphics-pipeline.md) | [S01](https://learnopengl.com/Getting-started/Hello-Triangle) | 渲染管線與三角形 |
| 2 | [GLSL 語法與資料傳遞](topics/glsl-basics.md) | [S02](https://learnopengl.com/Getting-started/Shaders) | GLSL 與 stage I/O |
| 3 | [Vertex 與 Fragment Shader](topics/shader-stages.md) | [S03](https://webglfundamentals.org/webgl/lessons/webgl-shaders-and-glsl.html) | 頂點與片段著色器 |
| 4 | [矩陣變換與頂點位置](topics/transformations.md) | [S04](https://learnopengl.com/Getting-started/Transformations) | 矩陣與空間變換 |
| 5 | [Uniform 與時間控制](topics/uniforms.md) | [S05](https://thebookofshaders.com/03/) | Uniform 與動態效果 |
| 6 | [顏色向量與 mix 混色](topics/colors-and-mix.md) | [S06](https://thebookofshaders.com/06/) | 顏色向量與插值 |

## 核心術語速查

| 術語 | 意義 | 條目 |
|---|---|---|
| Graphics Pipeline | 頂點到片段與 framebuffer 的處理流程 | [渲染管線](topics/graphics-pipeline.md) |
| Vertex Shader | 計算頂點位置與輸出資料的可程式化階段 | [著色器階段](topics/shader-stages.md) |
| Rasterization | 把圖元覆蓋區域轉換成片段 | [渲染管線](topics/graphics-pipeline.md) |
| Fragment Shader | 計算每個片段輸出的可程式化階段 | [著色器階段](topics/shader-stages.md) |
| GLSL `in/out` | 輸入與輸出介面 | [GLSL 基礎](topics/glsl-basics.md) |
| Uniform | Draw call 期間共享的 shader 參數 | [Uniform](topics/uniforms.md) |
| `mix(a,b,t)` | 線性插值 | [顏色混合](topics/colors-and-mix.md) |

## 資料來源及編修紀錄

- [來源機器可讀登錄表](../sources.json)
- [Ingest 紀錄](../logs/ingest-log.md)
- [檢查結果](../logs/lint-report.md)
- [AI 開發規範](../AGENTS.md)
- [需求訪談紀錄](../requirements.md)

## 內容使用限制

此 Wiki 用於教學；GLSL 原始碼僅為概念範例，未宣稱完成實際 OpenGL 執行測試。遇到 OpenGL、WebGL 不同版本的描述時，優先標記適用環境，不擅自合併成單一語法。
