# S03｜WebGL Fundamentals — WebGL Shaders and GLSL

- **來源 ID**：S03
- **原始標題**：WebGL Fundamentals — WebGL Shaders and GLSL
- **原始網址**：https://webglfundamentals.org/webgl/lessons/webgl-shaders-and-glsl.html
- **取用／核對日期**：2026-11-23
- **資料種類**：公開技術教材；本庫僅儲存自行整理的摘要，不重製全文
- **參考章節**：WebGL Shaders and GLSL：Vertex Shader、Fragment Shader、Attributes、Uniforms
- **對應 Wiki**：[wiki/topics/shader-stages.md](../wiki/topics/shader-stages.md)

## 本次擷取的知識要點

Vertex Shader 產生 clip-space 位置；Fragment Shader 對光柵化的片段計算輸出。

## 適用範圍與使用注意

WebGL1 的 attribute/varying 與 GLSL 330 core 的 in/out 不可直接混用；fragment 不等同於最終螢幕 pixel。

## Ingest 決策

- 收錄理由：與「Shader 從頂點到畫面顏色」的入門教學路徑直接相關。
- 處理方式：自行歸納繁體中文說明，保留術語與出處，不存放網頁全文。
- 審查狀態：來源頁面內容已查閱；摘要由 AI 整理；程式檢查不等於專家審定。
