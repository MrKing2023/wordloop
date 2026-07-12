# WordLoop Lexicon Builder

词库生成工具使用 Python 标准库，不要求安装第三方依赖。

## v4.1 已生成文件

```text
public/data/cet6/cet6_lexicon.json   # 5407 条基础词条
public/data/cet6/cet6_cards_100.json # 100 张增强学习卡
```

基础数据来自 ECDICT。大型原始 CSV 不进入 Git 仓库。

## 从 ECDICT CSV 提取 CET-6

```bash
python tools/lexicon_builder/extract_exam_words.py \
  --input .local-data/ecdict.csv \
  --exam cet6 \
  --output build/cet6_lexicon_full.json
```

## 重建 v4.1 发布数据

```bash
python tools/lexicon_builder/build_cet6_v4_1.py \
  --input build/cet6_lexicon_full.json \
  --lexicon-output public/data/cet6/cet6_lexicon.json \
  --cards-output public/data/cet6/cet6_cards_100.json
```

脚本会检查：

- 增强卡必须为 100 个不同单词；
- 每个单词必须存在于 CET-6 基础词库；
- 每个基础词条必须含 `cet6` 标签；
- 目标答案或正确词形必须在英文句中恰好出现一次；
- 挖空结构必须能完整还原英文原句。

## 其他工具

- `validate_lexicon.py`：基础词库结构检查；
- `make_ai_batches.py`：导出后续 AI 内容生成任务；
- `validate_generated_cards.py`：生成学习卡的字段和答案检查；
- `docs/AI_CONTENT_PIPELINE.md`：大规模内容生成、复核与抽样方案。

## WordLoop v4.2 考研英语

从当前 CET-6 基础词库中筛选同时带 `ky` 标签的词条，并生成考研核心词库与 100 张精选卡：

```bash
python build_kaoyan_v4_2.py \
  --cet6-lexicon ../../public/data/cet6/cet6_lexicon.json \
  --lexicon-output ../../public/data/kaoyan/kaoyan_lexicon.json \
  --cards-output ../../public/data/kaoyan/kaoyan_cards_100.json
```

发布前运行：

```bash
python validate_release_v4_2.py
```

要提取完整 ECDICT `ky` 标签集合，应先取得官方 `ecdict.csv`，然后运行：

```bash
python extract_exam_words.py \
  --input /path/to/ecdict.csv \
  --exam kaoyan \
  --output /path/to/kaoyan_full.json
```
