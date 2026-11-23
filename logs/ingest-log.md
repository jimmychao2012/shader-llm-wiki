# Ingest 實際紀錄

- 日期：2026-11-23
- 執行方式：線上讀取六份公開教材頁面 → 自行中文摘要 → 製作條目、索引與來源登錄 → 執行本地 lint。
- 特別註明：本次 **ingest** 是將網頁內容人工／AI 摘要轉入本地 Markdown Wiki；不是下載完整文章建立向量資料庫，也沒有設定自動網路爬取。

## 先討論、後生成

第 1 題讀者由使用者選定（已接觸電腦圖學的大學生），其餘第 2～8 題由使用者授權 AI 決定。詳細內容見 `requirements.md`。

## 第一批：S01、S02（2 篇）

1. 查閱 LearnOpenGL 的 Hello Triangle 及 Shaders。
2. 記錄 graphics pipeline、Shader stage、GLSL 的核心術語。
3. 形成 `raw/s01...`、`raw/s02...` 與對應 Wiki 條目。
4. 初步決定採用桌面 OpenGL GLSL 330 core 作為主要語法基準，避免教材版本混用。

## 第二批：S03～S06（4 篇）

1. 查閱 WebGL Fundamentals: WebGL Shaders and GLSL、LearnOpenGL: Transformations、The Book of Shaders: Uniforms、Colors。
2. 為每篇建立來源摘要，連結到對應 Wiki。
3. **版本差異發現**：S03 的 WebGL 1.0 會使用 `attribute/varying`，S02 主要示範桌面 GLSL `in/out`。在 W02/W03 條目明確說明版本差異，避免錯誤拼接程式碼。
4. **術語問題**：片段（fragment）不是保證寫入畫面的 pixel；在 W01/W03 補充深度與後續測試。
5. **uniform 名稱問題**：S05 的 `u_time` 等為教材慣例，不是 GLSL 保證存在的內建名稱；在 W05 明確標記。

## 已完成與限制

- 完成 6 份原始資料摘要、6 篇 Wiki 條目、索引與互連。
- 原始網頁已在本次執行中查閱；由於授權與合理引用考量，`raw/` 留的是整理筆記，不是網頁全文。
- 網頁內容和條目已由 AI 綜合整理，但**尚未經獨立審查者或專家逐條人工核實**。
- 靜態檢查結果另見 `lint-report.md`。
