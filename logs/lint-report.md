# Wiki 自動檢查與修正紀錄

檢查日期：2026-11-23

## 第 1 輪（實際執行）

指令：`python scripts/lint_wiki.py`

結果：**FAIL，2 個本地相對連結失效**。

- `README.md` 指向 `logs/lint-report.md`，此檔尚未建立。
- `wiki/index.md` 指向 `../logs/lint-report.md`，此檔尚未建立。

**修正方式**：先完成本檢查紀錄檔，再重跑 lint。這屬於檔案相依問題，不代表 Wiki 來源內容有錯。

## 第 2 輪

指令：`python scripts/lint_wiki.py`

結果：**PASS，0 個錯誤**。六份來源摘要、六篇 Wiki 條目、必備欄位及本地 Markdown 相對連結均通過靜態檢查。

## 檢查涵蓋範圍

- 六筆來源 ID 唯一、來源 URL 不重複。
- 六篇來源摘要存在、六篇 Wiki 條目存在。
- Wiki 條目的必備章節、來源 ID／URL 和索引關聯存在。
- 所有 Markdown 相對檔案連結指向現有檔案。

**未涵蓋**：公開來源日後是否改版或失效、所有專業論述的人工正確性驗證、GLSL 編譯執行、HTML 簡報（尚未製作）。
