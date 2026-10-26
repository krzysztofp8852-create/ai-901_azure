# ai-901_azure

Laby do egzaminu AI-901 (Microsoft Azure AI Fundamentals). Plan zadań i postęp: [PLAN.md](PLAN.md).

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
