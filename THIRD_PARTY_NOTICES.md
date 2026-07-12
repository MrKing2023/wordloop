# 第三方数据与许可说明

## ECDICT

- 项目：ECDICT — Free English to Chinese Dictionary Database
- 仓库：`https://github.com/skywind3000/ECDICT`
- 许可证：MIT License
- WordLoop 使用范围：单词、音标、中英文释义、考试标签、词频和词形变化等基础字段。

WordLoop 当前数据范围：

- CET-6：ECDICT 中带 `cet6` 标签的 5407 条本地提取结果；
- 考研英语：上述本地结果中同时带 `ky` 与 `cet6` 标签的 4112 条核心交集。

这些数量只描述本项目当前数据提取范围，不代表唯一或官方考试大纲词数。

## WordLoop 原创学习内容

以下文件中的英文学习语境、中文翻译、用法提醒、搭配说明、近义表达区别、词族整理和扩展例句为 WordLoop 项目重新撰写和整理：

```text
public/data/cet6/cet6_cards_100.json
public/data/kaoyan/kaoyan_cards_100.json
```

本版本没有复制 qwerty-learner、TypeWords 等 GPL 项目的词库数据，从而避免把其许可证义务混入当前发布数据。

再发布 ECDICT 衍生数据时，应继续保留 ECDICT 项目名称、仓库地址、版权声明和 MIT License。
