# 練習專案七： 小小停車場

## 簡介

這個專案「小小停車場」透過 `gradio` 與 `easyocr` 模組製作出一個以秒計費的停車場網頁應用程式。我們使用了 `easyocr` 進行車牌辨識，透過 `Python` 函數與標準模組進行概念驗證，並以 `gradio` 的介面做出成品，可以至Hugging Face的[連結](https://huggingface.co/spaces/AndrewTsai0411/parking_lot_ocr)參考成品。

## 如何重現 

- 安裝 [Miniconda](https://docs.anaconda.com/miniconda/)
- 依據 `environment.yml` 建立環境：
  
```bash
conda env create -f environment.yml
```

- 啟動環境並執行`python` `app.py` 並前往 http://127.0.0.1:7860 瀏覽成品。