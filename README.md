# Shader LLM Wiki

**完成範圍：LLM Wiki + 11 頁 HTML 教學簡報 + Graph/Loop 與檢查紀錄**。

這是一個面向已有電腦圖學基礎大學生的 Shader 概念知識庫，依照「先需求訪談、後建立 Wiki」方式開發。共 ingest 6 篇可核對的公開技術教材：每篇保留一份來源摘要和來源登錄；再整理成 6 篇有相互連結的繁體中文 Wiki 條目。

## 網站入口

- [GitHub Pages 專案首頁](https://jimmychao2012.github.io/shader-llm-wiki/)（部署成功後可瀏覽）
- [教學 HTML 簡報](https://jimmychao2012.github.io/shader-llm-wiki/slides/)（部署成功後可瀏覽）
- [重新部署教學](重新部署教學.md)

## 從哪裡開始讀？

- **[Wiki 總索引](wiki/index.md)** — 從這裡開始；GitHub 會直接呈現 Markdown。
- [AGENTS.md](AGENTS.md) — AI 新增或修改條目的工作規範。
- [requirements.md](requirements.md) — 8 題需求訪談，標明使用者選擇及 AI 自訂。
- [sources.json](sources.json) — 六篇來源的 URL、章節及查閱日。
- [logs/ingest-log.md](logs/ingest-log.md) — 兩批 ingest 的紀錄。
- [logs/lint-report.md](logs/lint-report.md) — 自動檢查與限制。

## 檢查方式

在專案根目錄執行：

```bash
python scripts/lint_wiki.py
```

預期所有本地檔案、來源 ID、條目結構通過檢查；**此命令不會驗證外部網站的永久可用性或內容真實度**。

## 目錄

```text
shader-llm-wiki/
├── AGENTS.md
├── README.md
├── requirements.md
├── sources.json
├── raw/                        # 六份來源摘要（不是來源全文）
├── wiki/
│   ├── index.md
│   └── topics/                 # 六篇主題條目
├── scripts/lint_wiki.py
└── logs/                       # ingest 與驗證紀錄
```

## 後續擴充

依 AGENTS.md，先讀來源、登錄 `S07`、建立 `raw/s07-source-note.md`，建立/更新條目並同步索引，最後執行 lint。後續 HTML 簡報需以 Wiki 為唯一資料來源，另立流程與內容驗證。


## 第二階段：教學 HTML 簡報（2026-11-23）

- [開啟教學 HTML 簡報](slides/index.html)：11 張投影片，支援方向鍵及上一頁／下一頁。
- [Graph／Loop 設計](workflow/graph.md)
- [逐頁 Wiki 對照表](workflow/slide-sources.csv)
- [實際驗證紀錄](reports/validation.md)
- [反思](reports/reflection.md)

### GitHub Pages 部署
在 Repository 的 Settings → Pages 選擇 Deploy from a branch → main → /(root)，儲存。
網頁網址格式：`https://jimmychao2012.github.io/shader-llm-wiki/slides/`。
Wiki 以 GitHub Markdown 呈現：`https://github.com/jimmychao2012/shader-llm-wiki/blob/main/wiki/index.md`。

- [作業繳交草稿](submission.md)
- 程式檢查：`python scripts/lint_wiki.py`、`python scripts/lint_slides.py`。
