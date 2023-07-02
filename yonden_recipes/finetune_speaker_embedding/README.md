# Speaker Embedding Fine-tuning

(ECAPA-TDNN)[https://arxiv.org/abs/2005.07143]の事前学習されたSpeaker EmbeddingをFine-tuningするRecipeです。

## Data Preparation
YONDENのデータを学習可能にするために、spk2wavfileのデータをSpeech Brain用にconvertします。
以下が例です。

```sh
python scripts/prepare_data.py \
    --input-file /ahc/work/yonden/yuta-nis/corpora/yonden_speaker_recognition/spk2wavfile.txt \
    --output-file /ahc/work/yonden/yuta-nis/corpora/yonden_speaker_recognition/manifest.csv

100%|█████████████████| 4085/4085 [00:34<00:00, 119.94it/s
```

