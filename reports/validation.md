# Shader Wiki → HTML 教學簡報｜實際檢查紀錄

- 日期：2026-11-23
- 對象：`slides/index.html`、`wiki/topics/*.md`、`workflow/slide-sources.csv`
- 工具：Python + BeautifulSoup 靜態檢查、Playwright 驅動 Chromium 瀏覽器（以 set_content 載入 HTML，因執行環境阻擋本機 URL 導航）

## 第一次檢查：Wiki 對照風險

製作前檢查既有舊版簡報草稿，發現舊版以來源 `S01–S06` 標記，而非明確標註新完成 Wiki 的 `W01–W06`，且主題來源分配與當前 Wiki 登錄表不同。**處理**：依現有 Wiki 重建簡報、逐頁使用 `W` ID，加入指向 `wiki/topics/` 的連結並建立 CSV 對照表；舊版草稿沒有覆蓋正式 Wiki。

## 第二次檢查：程式與瀏覽器

- Wiki 來源：6 篇；涵蓋 W01–W06。
- HTML 頁數：11；每頁都有 Wiki ID 和能找到的相對路徑。
- 逐頁來源對照：11 筆。
- 瀏覽器測試結果：
  - desktop 1366px：上一頁/下一頁及鍵盤導覽到 ['1', '2', '3']；滑桿 t=1 為 RGB (220, 79, 185)；水平寬度 1366px；JS 例外 0 個。
  - mobile 390px：上一頁/下一頁及鍵盤導覽到 ['1', '2', '3']；滑桿 t=1 為 RGB (220, 79, 185)；水平寬度 390px；JS 例外 0 個。

補充：`python scripts/lint_wiki.py`、`python scripts/lint_slides.py` 均回報 PASS (0 errors)。

## 最終結果

**PASS**。問題數：0。
- 沒有發現靜態連結、頁數、導覽、互動或水平溢出問題。

## 限制與待人工複核

- 沒有執行完整 GLSL shader 編譯；程式碼是教育用片段。
- 瀏覽器驗證不等於 GPU 執行驗證。
- 技術敘述依既有 Wiki；尚未由外部領域專家進行獨立逐項審查。
- 請上傳 GitHub Pages 後再檢查部署網址，因為本次是以瀏覽器載入 HTML 字串驗證樣式與 JavaScript，並非 GitHub Pages 網址的線上驗證。
