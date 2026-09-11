# -*- coding: utf-8 -*-
"""
把 site/materials/ 打包成 site/content/course-materials.zip，
供課程網頁一開始提供的「課程資料夾」下載。

用 zip 而不是直接給 .html 下載連結的原因：
  - 瀏覽器對 .html 連結預設會「開啟」而不是「下載」，直接渲染成一頁字
  - 右鍵另存新檔容易被存成 .htm 或整頁封存目錄，副檔名跑掉
  zip 沒有這個問題：瀏覽器一律下載，解壓縮後就是原始檔案。

用法：
    cd vscode/site
    python3 build_zip.py

注意：materials/build_sample_pptx.py 是產生器腳本本身，不會被打包。
"""
import zipfile
from pathlib import Path

SITE = Path(__file__).parent
MATERIALS = SITE / "materials"
OUT = SITE / "content" / "course-materials.zip"

ARCHIVE_ROOT = "vscode-course-materials"

# 產生器腳本本身，不是課程素材
EXCLUDE = {"build_sample_pptx.py"}


def main() -> None:
    files = sorted(
        p for p in MATERIALS.iterdir() if p.is_file() and p.name not in EXCLUDE
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        for f in files:
            info = zipfile.ZipInfo.from_file(f, arcname=f"{ARCHIVE_ROOT}/{f.name}")
            # UTF-8 檔名旗標，避免中文檔名在 Windows 內建解壓縮變亂碼
            info.flag_bits |= 0x800
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, f.read_bytes())

    print(f"寫入 {OUT}")
    for f in files:
        print(f"  + {f.name}")


if __name__ == "__main__":
    main()
