# ai-901_azure

Laby do egzaminu AI-901 (Microsoft Azure AI Fundamentals). Plan zadań i postęp: `PLAN.md`.

## Repo jest PUBLICZNE

Wszystko, co trafia do commita, widzi każdy w internecie. Nigdy nie commituj:

- kluczy API, tokenów, haseł, connection stringów ani zawartości `.env`,
- endpointów konkretnych zasobów Azure, identyfikatorów subskrypcji i tenantów,
- danych klientów i danych osobowych: prawdziwych faktur, nagrań rozmów, opinii, zdjęć z danymi.

Zasady:

- Konfiguracja idzie do `.env` (poza gitem). Nowe zmienne dopisuj do `.env.example` z pustą wartością.
- Wyniki labów i pliki wejściowe z prawdziwymi danymi trzymaj w `output/` (poza gitem). Do repo trafiają tylko syntetyczne dane testowe.
- W kodzie używaj `DefaultAzureCredential`, a nie kluczy wpisanych na sztywno.
- Przed każdym commitem przejrzyj `git diff --cached` i przeszukaj go pod kątem sekretów i adresów e-mail. Jeśli coś budzi wątpliwość, zapytaj użytkownika przed commitem.
- Commity w tym repo idą z adresu noreply GitHuba ustawionego w lokalnym `git config`. Nie zmieniaj go na prywatny adres.

## Praca w repo

- Środowisko: `source .venv/bin/activate`, zależności w `requirements.txt`, test konfiguracji: `python check_env.py`.
- Po ukończeniu zadania odhacz je w `PLAN.md`.
- Notatki z części A planu idą do `notes/`.
- Wszystko związane z AI-901 trzymaj tutaj, a nie w innych repo użytkownika.
