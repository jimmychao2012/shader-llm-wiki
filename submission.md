# 繳交內容草稿｜Shader LLM Wiki × 教學 HTML 簡報

> 填入 GitHub 帳號與公開網址，確認 GitHub Pages 連結後再繳交。姓名、學校、學號、系級依實際資料填寫。

## 1. LLM Wiki 主題與簡介

我的主題是「Shader：從頂點到畫面顏色」。對象是已經學過一些電腦圖學的大學生。利用六份技術來源整理成六篇繁體中文 Wiki，主題涵蓋渲染管線、GLSL 資料傳遞、Vertex/Fragment Shader、矩陣變換、Uniform 與顏色混合。

## 2. LLM Wiki 連結或成果

Wiki 入口：`https://github.com/jimmychao2012/shader-llm-wiki/blob/main/wiki/index.md`

專案的 `raw/`、`sources.json`、`logs/ingest-log.md` 保留了六份 ingest 資料的摘要、來源與紀錄。`requirements.md` 紀錄先討論後生成的需求決策。

## 3. 教學 HTML 簡報連結

公開網址：`https://jimmychao2012.github.io/shader-llm-wiki/slides/`

共 11 頁，支援按鈕／方向鍵翻頁，包含顏色插值互動示範。每張投影片都有對應 Wiki 條目的連結。

## 4. Graph／Loop 的設計

主要 Graph：讀取 Wiki → 來源覆蓋率檢查 → 建立每頁證據對照 → 教學大綱 → 逐頁撰稿與忠實度檢查 → HTML 渲染 → 頁面與互動檢查 → 交件。完整圖在 `workflow/graph.md`。

小 Loop：逐頁稿沒有 Wiki 依據就只修該頁；排版或 JavaScript 測試失敗就只修 HTML。每一小圈最多三輪，資料不足則停止，不自行捏造。

## 5. 一次實際執行結果與紀錄

建立 11 張投影片，引用 Wiki W01～W06；完成 11 筆逐頁來源對照。`scripts/lint_wiki.py` 與 `scripts/lint_slides.py` 皆檢查通過（0 errors）。也以 Chromium 進行桌面 1366px 和手機 390px 視窗測試，操作下一頁、方向鍵和 mix 比例滑桿，沒有偵測到 JavaScript 例外或水平溢出。檢查截圖與細節在 `reports/validation.md` 及 `reports/`。

## 6. 反思

最容易出錯的是「內容與來源對照」這個節點：舊版簡報草稿直接列原始來源 ID，但沒有清楚指向完成的 Wiki 條目。我把「逐頁證據對照」和「覆蓋率檢查」提前到撰稿之前；這樣出現錯誤時只需修正對應頁面，不會把整份簡報推倒重做。詳細見 `reports/reflection.md`。

## 補充說明

互動顏色展示以 JavaScript 模擬 RGB mix，不等於真正執行 GLSL。HTML 的本機 Chromium 測試已完成，但需要部署 GitHub Pages 後再人工檢查公開網址。
