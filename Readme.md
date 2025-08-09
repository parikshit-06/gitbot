# gitbot

[![PyPI Version](https://img.shields.io/pypi/v/gitbot)](https://pypi.org/project/gitbot)  
[![License](https://img.shields.io/github/license/parikshit-06/gitbot)](LICENSE)

## Overview

**gitbot** is a lightweight, context-aware CLI tool designed to analyze the current state of your Git repository and provide actionable suggestions for your next Git commands. It also helps automate common workflows such as syncing branches and generating commit messages, saving you time and reducing errors.

---

## Features

- Shows unstaged, staged, and untracked files count  
- Displays current branch and remote ahead/behind status  
- Suggests Git commands like `git add`, `git commit`, `git pull`, and `git push`  
- Generates simple commit message templates based on staged files  
- Automates `fetch`, `rebase`, and `push` operations with a single `sync` command  
- Interactive prompts for resolving rebase conflicts  

---

## Installation

Install from PyPI:

```bash
pip install gitbot
````

Or install from source:

```bash
git clone https://github.com/parikshit-06/gitbot.git
cd gitbot
pip install -e .
```

---

## Usage

Run the tool inside a Git repository folder:

```bash
gitbot --status
```

Get a suggested commit message based on staged changes:

```bash
gitbot --commit-msg
```

Automatically fetch, rebase, and push your branch:

```bash
gitbot --sync
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---