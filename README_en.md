[🇰🇷 Korean](README.md) | [🇺🇸 English](README_en.md)

# AI Bot 🤖

**Intelligent assistant connecting the power of Google Gemini and Perplexity to Mattermost.**

## 🚀 What is it?

AI Bot is a Python-based CLI tool that seamlessly integrates cutting-edge Large Language Models (LLMs) into your team's
communication hub, Mattermost. Share generative AI responses and real-time search results with your team instantly, with
zero complex configuration.

## ✨ Key Features

- **Dual Intelligence**: Switch freely between **Google Gemini** for creativity and speed, and **Perplexity Pro** for
  real-time information retrieval.
- **Seamless Integration**: Automatically sends responses to Mattermost channels in a clean, Markdown-formatted style.
- **Developer Ready**: Optimized for script and workflow automation with a simple CLI interface.

## 🛠 Quick Start

### 1. Prerequisites

Install the required libraries.

```bash
pip install -r requirements.txt
```

### 2. Configuration

Set your API keys in the `.env` file.

```properties
GEMINI_API_KEY=your_gemini_key
PPLX_API_KEY=your_perplexity_key
MATTERMOST_WEBHOOK_URL=your_webhook_url
```

### 3. Usage

Select your desired model and run immediately.

**Real-time Search with Perplexity (Sonar Pro)**

```bash
python ai_bot.py --prompt "Summarize 2024 Generative AI tech trends" --model perplexity
```

**Creative Answers & Coding with Gemini (Default)**

```bash
python ai_bot.py --prompt "Write a Python decorator pattern example"
```

---
Built for speed and simplicity.
