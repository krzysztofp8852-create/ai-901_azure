# ai901-lab

Laby do egzaminu AI-901 (Microsoft Azure AI Fundamentals). Plan zadań: `~/Projects/research/2026-10-26-ai-901-zadania-praktyczne.md`.

## Start

```bash
source .venv/bin/activate
python check_env.py
```

Pierwsza konfiguracja od zera:

```bash
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## Struktura

- `notes/` — notatki z części A
- `output/` — wyniki labów (poza gitem)
- `.env` — endpoint projektu Foundry i nazwy wdrożeń (poza gitem)
