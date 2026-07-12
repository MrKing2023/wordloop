# WordLoop v4.1 测试报告

测试日期：2026-07-12

## 数据检查

- CET-6 基础词条：5407；
- 其中同时带 CET-4 标签：3451；
- 未带 CET-4 标签：1956；
- CET-6 增强学习卡：100；
- 基础词条 ID 与单词去重检查：通过；
- 增强卡 ID 与目标词去重检查：通过；
- 100 张增强卡全部能在基础词库中找到对应 `cet6` 标签词条：通过。

## 学习卡质量规则

每张卡均通过：

- 必填字段检查；
- 英文例句和中文翻译非空；
- 目标答案或正确词形在英文句中恰好出现一次；
- `clozePrefix + clozeAnswer + clozeSuffix` 完整还原原句；
- `acceptedAnswers` 包含本题答案；
- 至少包含常见搭配、相关表达、词族和扩展例句；
- `libraryId` 为 `cet6`。

## 代码检查

通过 `node --check`：

- `public/app.js`；
- `public/enhancements.js`；
- `public/plan_v3.js`；
- `public/lexicon_v4.js`。

通过 Python 编译检查：

- `tools/lexicon_builder/*.py`。

## 页面和状态流程测试

在模拟浏览器环境中完成：

1. 打开词库中心，显示 v4.1、5407 基础词条和 CET-6 入口；
2. 打开基础词库浏览器，默认显示 50 行；
3. 启用 CET-6，成功导入 100 张卡片；
4. 自动生成 100 词、默认 5 天的学习计划；
5. 第一天第一个目标词为 `environmental`；
6. 进入练习并输入正确答案，成功显示详细学习面板；
7. 切回核心 200 后，恢复 200 词独立计划；
8. 全程未捕获 JavaScript 页面错误。

## HTTP 静态资源检查

本地静态服务器返回：

- `index.html`：WordLoop v4.1；
- `data/cet6/cet6_cards_100.json`：100 张卡；
- `data/cet6/cet6_lexicon.json`：5407 条词条。

## 文件大小

- `cet6_lexicon.json`：约 2.42 MB；
- `cet6_cards_100.json`：约 151 KB。

当前体积适合 CloudBase 和 Cloudflare 静态部署。基础词库仅在进入浏览器时按需下载，100 张学习卡仅在首次启用 CET-6 时写入本地状态。
