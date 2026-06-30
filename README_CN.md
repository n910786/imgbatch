# imgbatch

[![CI](https://github.com/n910786/imgbatch/actions/workflows/ci.yml/badge.svg)](https://github.com/n910786/imgbatch/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/imgbatch.svg)](https://badge.fury.io/py/imgbatch)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**批量图片处理命令行工具** — 抠图、格式转换、尺寸调整。Python 编写。

## 功能

- **抠图** — 阈值算法去除白/绿背景，或 AI（rembg）智能抠图
- **格式转换** — PNG、JPG、WebP、BMP、TIFF 互转
- **尺寸调整** — 按宽高或比例缩放，自动保持长宽比
- **递归处理** — 支持子目录遍历
- **进度条** — tqdm 实时反馈

## 安装

```bash
pip install imgbatch
```

如需 AI 抠图功能：
```bash
pip install imgbatch[ai]
```

## 快速上手

```bash
# 去除白色背景
imgbatch cutout ./照片 -o ./照片_去底

# JPG 转 PNG
imgbatch convert ./照片 -f png -o ./照片_png

# 等比缩放到 50%
imgbatch resize ./照片 -s 0.5 -o ./照片_小图

# AI 智能抠图
imgbatch cutout ./照片 --ai
```

## 命令详解

### `cutout` — 背景去除

```
imgbatch cutout 输入目录 [选项]

选项:
  -o, --output-dir PATH    输出目录（默认: 输入目录_cutout）
  -t, --threshold INT      白色阈值 0-255（默认: 240）
  --ai                     使用 rembg AI 引擎
  -r, --recursive          递归处理子目录
```

### `convert` — 格式转换

```
imgbatch convert 输入目录 [选项]

选项:
  -o, --output-dir PATH    输出目录
  -f, --format [png|jpg|jpeg|webp|bmp|tiff]  目标格式
  -q, --quality INT        JPG/WebP 质量（默认: 90）
  -r, --recursive          递归处理子目录
```

### `resize` — 尺寸调整

```
imgbatch resize 输入目录 [选项]

选项:
  -o, --output-dir PATH    输出目录
  -w, --width INT          目标宽度
  -H, --height INT         目标高度
  -s, --scale FLOAT        缩放比例（如 0.5）
  -r, --recursive          递归处理子目录
```

## 开源协议

MIT © n910786
