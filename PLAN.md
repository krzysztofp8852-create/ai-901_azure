# AI-901 (Microsoft Azure AI Fundamentals): zadania praktyczne pokrywające cały zakres egzaminu

*Stan: 26.10.2026*

Zakres oparty na oficjalnym study guide, wersja „Skills measured as of April 15, 2026” ([Microsoft Learn: Study guide for Exam AI-901](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901)). Egzamin ma dwie domeny:

| Domena | Waga |
|---|---|
| Identify AI concepts and capabilities | **40–45%** |
| Implement AI solutions by using Microsoft Foundry | **55–60%** |

Rzeczy z study guide, które wpływają na kształt zadań:

- Od kandydata oczekuje się **znajomości składni Pythona** i zasobów Azure, a nie tylko teorii ([study guide, „Audience profile”](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901)). Dlatego ok. połowa zadań to małe aplikacje w Pythonie.
- Microsoft pisze wprost: „You should be familiar with REST APIs, SDKs, and CLIs” ([tamże](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901)).
- Próg zdania to **700/1000** ([tamże](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901)). AI-901 zastępuje AI-900 ([Microsoft Learn: Azure AI Fundamentals](https://learn.microsoft.com/en-gb/credentials/certifications/azure-ai-fundamentals/)).

Każde zadanie ma cel, kroki i **kryterium ukończenia**. Na końcu jest tabela, która przypisuje każdy z 29 punktów study guide do konkretnego zadania.

---

## 0. Przygotowanie środowiska (ok. 1–2 h)

- [ ] **Z0.1** Załóż subskrypcję Azure (darmowe konto lub firmowa) i od razu ustaw **alert budżetowy** (np. 20 USD) w Cost Management.
- [ ] **Z0.2** W [portalu Foundry](https://ai.azure.com) utwórz zasób Foundry i projekt w osobnej grupie zasobów, np. `rg-ai901-lab`. Wszystkie laby trzymaj w tej grupie, a po skończeniu nauki usuń ją jednym poleceniem.
- [ ] **Z0.3** Zainstaluj Azure CLI, zaloguj się (`az login`) i nadaj sobie na projekcie rolę pozwalającą wywoływać modele (np. *Azure AI User*). Używaj uwierzytelniania bez kluczy (`DefaultAzureCredential` z pakietu `azure-identity`), a klucze API tylko tam, gdzie usługa inaczej nie działa.
- [x] **Z0.4** Utwórz repo `ai-901_azure` z venv i plikiem `.env` (endpoint projektu, nazwy wdrożeń). Plik `.env` dopisz do `.gitignore`.

**Ukończone, gdy:** `az account show` zwraca właściwą subskrypcję, projekt jest widoczny w portalu Foundry, a w repo działa `python -c "import azure.identity"`.

---

## Część A: koncepcje (domena 1, 40–45%)

To zadania „na papierze” z krótkimi eksperymentami. Wyniki zapisuj jako notatki w `notes/` w repo, bo przydadzą się do powtórki.

### A1. Karta Responsible AI (ok. 2 h)

Pokrywa sześć zasad: fairness, reliability & safety, privacy & security, inclusiveness, transparency, accountability.

- [ ] Weź realny projekt (np. bot obsługi zapytań dla składu budowlanego). Dla **każdej z 6 zasad** zapisz jedno konkretne ryzyko, jedno działanie ograniczające i to, czym w Azure je realizujesz (filtry treści, Azure AI Content Safety, logowanie, człowiek w pętli, informacja „rozmawiasz z AI”, proces odwołań).
- [ ] Przypisz zasadę do scenariusza (odpowiedzi pod spodem):
  1. Model scoringowy systematycznie gorzej ocenia wnioski kobiet.
  2. Bot podaje błędne dawkowanie, gdy pytanie jest nietypowo sformułowane.
  3. Rozmowy z danymi klientów są logowane bez szyfrowania i bez limitu retencji.
  4. Aplikacja głosowa nie radzi sobie z osobami z wadą wymowy i nie ma alternatywy tekstowej.
  5. Klient nie wie, że rozmawia z AI, ani dlaczego jego wniosek odrzucono.
  6. W firmie nikt nie odpowiada za decyzje systemu i nie ma ścieżki odwołania.

<details><summary>Odpowiedzi</summary>

1 fairness · 2 reliability & safety · 3 privacy & security · 4 inclusiveness · 5 transparency · 6 accountability
</details>

**Ukończone, gdy:** potrafisz z pamięci wymienić 6 zasad i do każdej podać przykład naruszenia oraz środek zaradczy.

### A2. Jak działają modele generatywne (ok. 1,5 h)

- [ ] Napisz notatkę na jedną stronę, własnymi słowami: tokeny, embeddingi, architektura transformer i mechanizm uwagi (attention), przewidywanie kolejnego tokena, okno kontekstu, temperatura jako „losowość próbkowania”, halucynacje, grounding/RAG, różnica między modelem bazowym, modelem dostrojonym (fine-tuned) a modelem rozumującym (reasoning).
- [ ] Eksperyment: w Pythonie (`tiktoken`) policz tokeny tego samego akapitu po polsku i po angielsku. Zapisz, ile razy więcej tokenów zużywa polski i co to znaczy dla kosztów i okna kontekstu.

**Ukończone, gdy:** umiesz w 2 minuty wyjaśnić komuś, „dlaczego model halucynuje i jak grounding temu zapobiega”.

### A3. Dobór modelu do zadania (ok. 1,5 h)

- [ ] W katalogu modeli Foundry porównaj 5 modeli w tabeli: duży model czatu, mały/„mini”, model rozumujący, mały model open (np. z rodziny Phi), model embeddingów i model generowania obrazów. Kolumny: modalności wejścia/wyjścia, okno kontekstu, orientacyjny koszt, dostępność w Twoim regionie. Skorzystaj z widoku porównania i benchmarków w katalogu.
- [ ] Dla 5 scenariuszy wybierz model i uzasadnij w jednym zdaniu: chatbot FAQ o dużym ruchu, analiza złożonej umowy, wyszukiwanie semantyczne w bazie dokumentów, rozumienie zdjęć z budowy, generowanie grafiki na social media.

**Ukończone, gdy:** tabela jest gotowa, a każdy wybór ma uzasadnienie oparte na możliwościach modelu, nie tylko na „najlepszy”.

### A4. Opcje wdrożenia i parametry konfiguracji (ok. 1,5 h)

- [ ] Rozpisz w tabeli typy wdrożeń modeli w Foundry: *Global Standard*, *Data Zone Standard*, *Standard* (regionalny), *Provisioned* (PTU), *Batch*. Dla każdego podaj, gdzie przetwarzane są dane, jak się płaci i kiedy go użyć. Osobno zapisz, czym jest wdrożenie *serverless API* a czym *managed compute* dla modeli spoza rodziny OpenAI. Nazwy i warianty sprawdź w aktualnej dokumentacji Foundry, bo zmieniają się dość często.
- [ ] Opisz parametry: `temperature`, `top_p`, maksymalna liczba tokenów odpowiedzi, `frequency_penalty`/`presence_penalty`, sekwencje stop, komunikat systemowy, limit TPM/RPM wdrożenia.

**Ukończone, gdy:** potrafisz odpowiedzieć na pytanie typu „dane nie mogą opuścić UE, ruch jest przewidywalny i duży: które wdrożenie?”.

### A5. Mapa workloadów AI (ok. 1 h)

- [ ] Przypisz każdemu scenariuszowi workload (generative AI, agentic AI, analiza tekstu, mowa, computer vision, generowanie obrazów, ekstrakcja informacji) i usługę w Foundry:
  1. Transkrypcja nagrań z infolinii z rozróżnieniem, kto mówi.
  2. Odczyt NIP, kwoty i pozycji z faktur PDF.
  3. Ocena, czy opinie w Google są pozytywne czy negatywne.
  4. Asystent, który sam sprawdza stan magazynu w API i rezerwuje towar.
  5. Generowanie opisów produktów do sklepu.
  6. Liczenie palet na zdjęciu z magazynu.
  7. Czytanie komunikatów głosowych kierowcy w aplikacji.
  8. Znalezienie w nagraniach szkoleń fragmentu, w którym omawiane jest BHP.
  9. Wykrywanie i maskowanie numerów PESEL w mailach.
  10. Tworzenie grafik na social media z opisu tekstowego.
  11. Odpowiadanie na pytania o regulamin firmy na podstawie jej dokumentów.
  12. Odczyt tablic rejestracyjnych z kamery przy bramie.

<details><summary>Odpowiedzi</summary>

1 mowa (STT + diaryzacja) · 2 ekstrakcja informacji (Content Understanding) · 3 analiza tekstu (sentyment) · 4 agentic AI · 5 generative AI · 6 computer vision (detekcja obiektów) · 7 mowa (TTS) · 8 ekstrakcja informacji z wideo (Content Understanding) · 9 analiza tekstu (wykrywanie PII) · 10 generowanie obrazów · 11 generative AI z groundingiem (agent z wyszukiwaniem w plikach / RAG) · 12 computer vision (OCR)
</details>

**Ukończone, gdy:** masz co najmniej 11/12 poprawnych bez zaglądania do odpowiedzi.

### A6. Techniki analizy tekstu (ok. 1 h)

- [ ] Zbierz 5 prawdziwych opinii klientów po polsku. Ręcznie oznacz w każdej: słowa kluczowe, encje (osoba, miejsce, organizacja, data, kwota), sentyment (pozytywny/neutralny/negatywny/mieszany) i napisz streszczenie w jednym zdaniu.
- [ ] Zapisz różnicę między streszczeniem **ekstrakcyjnym** (wybór zdań z tekstu) a **abstrakcyjnym** (nowy tekst) oraz między rozpoznawaniem encji (NER) a wykrywaniem danych osobowych (PII).

**Ukończone, gdy:** masz „złoty zestaw” ręcznych oznaczeń, który w zadaniu B6 porównasz z wynikiem usługi.

### A7. Rozpoznawanie i synteza mowy (ok. 1 h)

- [ ] Wypisz możliwości **speech-to-text**: rozpoznawanie w czasie rzeczywistym i wsadowe, szybka transkrypcja, diaryzacja mówców, identyfikacja języka, modele niestandardowe (custom speech), tłumaczenie mowy.
- [ ] Wypisz możliwości **text-to-speech**: głosy neuronowe, SSML (pauzy, tempo, wysokość, wymowa), głosy niestandardowe (custom voice) i to, dlaczego ich użycie jest objęte ograniczonym dostępem (zasady RAI).
- [ ] W *Speech playground* w Foundry napisz fragment SSML po polsku z pauzą 500 ms, wolniejszym tempem jednego zdania i poprawioną wymową skrótu. Odsłuchaj wynik.

**Ukończone, gdy:** SSML działa, a Ty umiesz wskazać, kiedy wybrać transkrypcję wsadową, a kiedy w czasie rzeczywistym.

### A8. Computer vision i generowanie obrazów (ok. 1 h)

- [ ] Rozróżnij w notatce: klasyfikację obrazu, detekcję obiektów, segmentację, OCR, generowanie opisów (captioning), tagowanie, analizę twarzy (i dlaczego część funkcji jest ograniczona). Osobno: generowanie obrazu z tekstu, edycję/inpainting oraz rozumienie obrazu przez model multimodalny (obraz jako wejście promptu).
- [ ] Do każdej techniki dopisz jeden przykład biznesowy z Twojej branży.

**Ukończone, gdy:** potrafisz wyjaśnić różnicę „detekcja obiektów vs klasyfikacja” i „model wizyjny vs model multimodalny z wejściem obrazowym”.

### A9. Ekstrakcja informacji z tekstu, obrazów, audio i wideo (ok. 1 h)

- [ ] Zrób tabelę: modalność (tekst / dokument / obraz / audio / wideo) → co da się wyciągnąć (pola, tabele, encje, transkrypt, segmenty, klatki kluczowe) → narzędzie (Azure Language, Azure Content Understanding, model multimodalny z promptem).
- [ ] Dopisz, kiedy lepiej użyć gotowego analizatora (prebuilt), kiedy własnego schematu pól, a kiedy wystarczy prompt do LLM. Kryteria: powtarzalność, struktura wyjścia, koszt, potrzeba oceny pewności (confidence) i wskazania źródła (grounding).

**Ukończone, gdy:** tabela pokrywa wszystkie 5 modalności.

---

## Część B: implementacja w Microsoft Foundry (domena 2, 55–60%)

Każde zadanie kończy się działającym kodem w repo `ai-901_azure`. Nazwy pakietów i metod SDK w Foundry zmieniają się szybko, więc przed kodowaniem przejdź aktualny quickstart z dokumentacji Foundry. Opis zadania mówi, *co* zbudować, a nie podaje gotowego API.

### Aplikacje generatywne i agenci

#### B1. System prompt i user prompt (ok. 2 h)

- [ ] Napisz 3 wersje system promptu dla asystenta obsługi klienta: (a) minimalną, (b) z rolą, tonem, zakresem tematów i zasadą „nie wiem → przekaż człowiekowi”, (c) jak (b) plus 2–3 przykłady (few-shot) i wymuszony format odpowiedzi (np. JSON z polami `odpowiedz`, `pewnosc`, `eskalacja`).
- [ ] Przygotuj 10 pytań testowych: 6 typowych, 2 spoza zakresu, 2 próby prompt injection („zignoruj poprzednie instrukcje…”).
- [ ] Puść wszystkie 30 kombinacji w playgroundzie i zanotuj w tabeli, która wersja jak się zachowała.

**Ukończone, gdy:** wersja (c) poprawnie odmawia pytań spoza zakresu i zwraca poprawny JSON w co najmniej 9/10 przypadków.

#### B2. Wdrożenie modelu i praca w portalu (ok. 1 h)

- [ ] Wdróż lekki model czatu (dostępny w Twoim regionie model typu „mini”) jako *Global Standard*.
- [ ] W *chat playground*: ustaw system prompt z B1, zmieniaj `temperature` (0 / 0,7 / 1,5) na tym samym pytaniu kreatywnym i zanotuj różnice.
- [ ] Obejrzyj i skonfiguruj filtr treści wdrożenia (kategorie i progi), sprawdź limity TPM.
- [ ] Skorzystaj z opcji „View code”, żeby zobaczyć, jak to samo wywołanie wygląda w Pythonie.

**Ukończone, gdy:** model odpowiada w playgroundzie, a Ty wiesz, gdzie w portalu zmienić filtr treści i limit przepustowości.

#### B3. Lekki klient czatu z Foundry SDK (ok. 2–3 h)

- [ ] Napisz w Pythonie aplikację konsolową (`chat.py`), która łączy się z projektem Foundry przez SDK (`azure-ai-projects` + `azure-identity`) i rozmawia z modelem z B2.
- [ ] Wymagania: system prompt wczytywany z pliku, **historia rozmowy** (multi-turn), strumieniowanie odpowiedzi, komenda `/reset`, obsługa błędu 429 (ponowienie z odczekaniem).

**Ukończone, gdy:** model pamięta w 3. pytaniu to, co powiedziałeś w 1., a kod nie zawiera klucza API.

#### B4. Pojedynczy agent w portalu (ok. 2 h)

- [ ] W Foundry Agent Service utwórz agenta z instrukcjami (np. „asystent działu handlowego składu budowlanego”).
- [ ] Dodaj narzędzie **wyszukiwania w plikach** i wgraj 2–3 dokumenty (cennik, regulamin dostaw, FAQ). Opcjonalnie dodaj **code interpreter** i każ policzyć koszt zamówienia.
- [ ] Przetestuj agenta w playgroundzie: 5 pytań, na które odpowiedź jest w dokumentach, i 2, na które jej nie ma. Sprawdź cytowania i ślady (traces) wywołań narzędzi.

**Ukończone, gdy:** agent cytuje właściwy dokument i przyznaje się do braku wiedzy, zamiast zmyślać.

#### B5. Lekki klient aplikacji agenta (ok. 2 h)

- [ ] Napisz `agent_client.py`, który przez SDK wywołuje agenta z B4, prowadzi wieloturową rozmowę i wypisuje odpowiedzi razem ze źródłami (cytowaniami).
- [ ] Dodaj logowanie identyfikatora rozmowy, żeby dało się ją odnaleźć w portalu.

**Ukończone, gdy:** rozmowa z konsoli jest widoczna w portalu Foundry jako ta sama konwersacja.

### Tekst i mowa

#### B6. Aplikacja z analizą tekstu (ok. 2–3 h)

- [ ] Przygotuj CSV z ok. 20 opiniami klientów (w tym 5 z zadania A6).
- [ ] Napisz `text_analysis.py`, który przez Azure Language w Foundry Tools robi dla każdej opinii: wykrycie języka, sentyment (z opinion mining), frazy kluczowe, encje, wykrycie i zamaskowanie PII oraz streszczenie. Wynik zapisz do CSV/JSON.
- [ ] Porównaj wynik z ręcznymi oznaczeniami z A6. Następnie zrób to samo jednym promptem do LLM z B2 i zanotuj różnice w jakości, koszcie i strukturze wyników.

**Ukończone, gdy:** masz plik wynikowy i jeden akapit wniosków „usługa wyspecjalizowana vs LLM”.

#### B7. Odpowiedź na pytanie zadane głosem (model multimodalny) (ok. 2 h)

- [ ] Wdróż model przyjmujący **audio na wejściu** (z dostępnych w katalogu modeli multimodalnych z obsługą audio).
- [ ] Nagraj po polsku plik `.wav` z pytaniem i wyślij go do modelu z kodu. Odbierz odpowiedź tekstową (a jeśli model to obsługuje, także audio) i zapisz ją.

**Ukończone, gdy:** zadajesz pytanie głosem i dostajesz sensowną odpowiedź bez osobnego kroku transkrypcji.

#### B8. Aplikacja z Azure Speech in Foundry Tools (ok. 2–3 h)

- [ ] Napisz `voice_loop.py` (SDK `azure-cognitiveservices-speech`): rozpoznawanie mowy `pl-PL` z mikrofonu lub pliku → tekst wysłany do klienta czatu z B3 → odpowiedź przeczytana polskim głosem neuronowym (z SSML z A7).
- [ ] Wariant dodatkowy: tłumaczenie mowy PL→EN.
- [ ] Porównaj to podejście (STT → LLM → TTS) z B7 (jeden model multimodalny) pod kątem opóźnienia, kontroli nad głosem i kosztu.

**Ukończone, gdy:** pełna pętla głosowa działa, a porównanie z B7 jest zapisane.

### Computer vision i generowanie obrazów

#### B9. Obraz jako wejście promptu (ok. 1,5 h)

- [ ] Wyślij do modelu multimodalnego (np. tego z B2, jeśli przyjmuje obrazy) 3 zdjęcia: paragon lub fakturę, zdjęcie z placu budowy i wykres. Zadaj do każdego 2 pytania.
- [ ] Przetestuj przekazanie obrazu przez URL i przez base64. Sprawdź, jak ustawienie szczegółowości (`detail`) wpływa na odpowiedź i zużycie tokenów.

**Ukończone, gdy:** model poprawnie odczytuje kwotę z paragonu i trend z wykresu.

#### B10. Generowanie obrazów (ok. 1,5 h)

- [ ] Wdróż model generowania obrazów dostępny w Twoim regionie.
- [ ] Wygeneruj grafikę promującą produkt w 3 wariantach promptu. Zmieniaj rozmiar i jakość, a jeśli model to obsługuje, wykonaj edycję istniejącego obrazu.
- [ ] Wyślij prompt, który powinien zablokować filtr treści, i zanotuj, jak wygląda odmowa. Sprawdź, czy wygenerowany plik zawiera metadane pochodzenia (Content Credentials), i zapisz, z którą zasadą RAI to się łączy (transparency).

**Ukończone, gdy:** masz 3 obrazy w repo i notatkę o filtrach i oznaczaniu pochodzenia.

#### B11. Lekka aplikacja z funkcjami wizji (ok. 2 h)

- [ ] Napisz `catalog.py`: dla folderu ze zdjęciami (np. produktów) generuje opis, tagi i tekst odczytany z obrazu (OCR), a wynik zapisuje do JSON. Użyj Azure Vision (Image Analysis) **albo** modelu multimodalnego. Najlepiej zrób oba warianty i porównaj.

**Ukończone, gdy:** dla 10 zdjęć powstaje plik JSON z opisem, tagami i tekstem.

### Ekstrakcja informacji (Azure Content Understanding)

#### B12. Dokumenty i formularze (ok. 2 h)

- [ ] W Foundry przetestuj gotowy analizator dokumentów (np. dla faktur) na 3 fakturach PDF.
- [ ] Utwórz **własny analizator** ze schematem pól, np. numer zamówienia, NIP sprzedawcy, data dostawy, tabela pozycji (nazwa, ilość, cena). Przetestuj go na 5 dokumentach i sprawdź wartości pewności (confidence) oraz wskazania źródła w dokumencie.

**Ukończone, gdy:** własny analizator poprawnie wyciąga pola z co najmniej 4 z 5 dokumentów.

#### B13. Obrazy (ok. 1 h)

- [ ] Utwórz analizator dla zdjęć, np. tabliczek znamionowych urządzeń lub zdjęć uszkodzeń: pola typu producent, model, numer seryjny lub rodzaj i opis uszkodzenia. Przetestuj na 5 zdjęciach.

**Ukończone, gdy:** pola wracają w ustrukturyzowanym JSON.

#### B14. Audio i wideo (ok. 2 h)

- [ ] **Audio:** nagraj ok. 2-minutową symulowaną rozmowę z klientem. Zdefiniuj analizator, który zwróci transkrypt, streszczenie oraz pola: intencję klienta, wspomniane produkty, termin i to, czy potrzebny jest kontakt zwrotny.
- [ ] **Wideo:** weź krótki film (1–3 min, np. instruktaż). Wyciągnij segmenty z opisami, transkrypt i klatki kluczowe, a następnie znajdź moment, w którym pojawia się określony temat.

**Ukończone, gdy:** z rozmowy wychodzi poprawna intencja, a w wideo udaje się wskazać znacznik czasu szukanego tematu.

#### B15. Lekka aplikacja do ekstrakcji (ok. 2–3 h)

- [ ] Napisz `extract.py`, który bierze folder z mieszanymi plikami (PDF, JPG, WAV, MP4), dobiera analizator z B12–B14 według typu pliku i wywołuje Content Understanding (REST API lub SDK, jeśli jest dostępne dla Twojej wersji API). Poprawnie obsłuż **operację długotrwałą**: wyślij plik, odpytuj o status, odbierz wynik. Wyniki zbierz do jednego JSON/CSV.

**Ukończone, gdy:** jeden przebieg skryptu przetwarza folder z co najmniej 4 typami plików bez ręcznej ingerencji.

---

## Część C: projekt łączący (opcjonalnie, 1–2 dni)

- [ ] **„Asystent biura obsługi składu budowlanego”**: agent z B4/B5 z wiedzą z dokumentów, który przyjmuje pytania głosowe (B8 lub B7), przetwarza wgrane faktury i zdjęcia (B15), podsumowuje sentyment opinii z ostatniego tygodnia (B6) i ma dołączoną kartę Responsible AI (A1).
- [ ] Na koniec: usuń grupę zasobów `rg-ai901-lab` (`az group delete -n rg-ai901-lab`) i sprawdź w Cost Management, że nic nie nalicza kosztów.

To przy okazji gotowy materiał demo/portfolio dla klientów.

---

## Część D: powtórka przed egzaminem

- [ ] Zrób darmowy **Practice Assessment** (dostępny w AI Skills Navigator, wymaga zalogowania) ([study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901)). Zrób go na starcie i tydzień przed egzaminem.
- [ ] Przejdź **exam sandbox**, żeby poznać interfejs egzaminu ([aka.ms/examdemo](https://aka.ms/examdemo)).
- [ ] Przejrzyj notatki z części A i odpowiedzi do A1/A5 bez podglądania.
- [ ] Przed egzaminem sprawdź na stronie study guide, czy nie pojawiła się nowa wersja „Skills measured”. Microsoft aktualizuje ją okresowo i najpierw zmienia wersję angielską ([tamże](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901)).

---

## Pokrycie: punkt study guide → zadanie

| # | Punkt z study guide | Zadania |
|---|---|---|
| 1 | Fairness | A1 |
| 2 | Reliability and safety | A1, B1 (prompt injection) |
| 3 | Privacy and security | A1, B6 (PII), Z0.3 (uwierzytelnianie bez kluczy) |
| 4 | Inclusiveness | A1, A7 |
| 5 | Transparency | A1, B10 (Content Credentials) |
| 6 | Accountability | A1 |
| 7 | How generative AI models work | A2 |
| 8 | Appropriate AI model based on capabilities | A3 |
| 9 | Deployment options and configuration parameters | A4, B2 |
| 10 | Scenarios for common AI workloads (generative, agentic, text, speech, vision, extraction) | A5 |
| 11 | Text analysis techniques (keywords, entities, sentiment, summarization) | A6, B6 |
| 12 | Speech recognition and synthesis | A7, B8 |
| 13 | Computer vision and image-generation models | A8, B9–B11 |
| 14 | Extracting information from text, images, audio, video | A9, B12–B15 |
| 15 | Effective system and user prompts | B1 |
| 16 | Deploy a model and interact in the Foundry portal | B2 |
| 17 | Lightweight chat client with the Foundry SDK | B3 |
| 18 | Single-agent solution in the Foundry portal | B4 |
| 19 | Lightweight client application for an agent | B5 |
| 20 | Lightweight application with text analysis | B6 |
| 21 | Spoken prompts with a multimodal model | B7 |
| 22 | Lightweight application with Azure Speech in Foundry Tools | B8 |
| 23 | Visual input in prompts with a multimodal model | B9 |
| 24 | New visual outputs with generative models | B10 |
| 25 | Lightweight application with vision capabilities | B11 |
| 26 | Content Understanding: documents and forms | B12 |
| 27 | Content Understanding: images | B13 |
| 28 | Content Understanding: audio and video | B14 |
| 29 | Lightweight application with Content Understanding | B15 |

Wszystkie 29 punktów z wersji z 15.04.2026 ma przypisane zadanie.

**Szacunkowy czas:** część A ok. 12 h, część B ok. 28–35 h, razem z przygotowaniem i powtórką ok. **45–50 h**, czyli 3–4 tygodnie przy ok. 2 h dziennie.

---

## Nota metodologiczna

- Zakres (domeny, wagi, 29 punktów, profil kandydata, próg 700) pochodzi bezpośrednio z oficjalnego study guide Microsoft Learn, zaktualizowanego 14.07.2026.
- Treść zadań, podział na kroki, kryteria ukończenia i szacunki czasu to **moja interpretacja**, a nie materiał Microsoftu. Microsoft nie publikuje liczby pytań ani czasu trwania egzaminu w study guide, więc tych danych tu nie podaję.
- Nazw konkretnych modeli, typów wdrożeń i metod SDK celowo nie podaję jako pewnych: w Foundry zmieniają się co kilka miesięcy. Przed każdym labem sprawdź aktualny quickstart w dokumentacji Foundry.
- Koszty zależą od regionu i modelu. Alert budżetowy (Z0.1) i usunięcie grupy zasobów (część C) to zabezpieczenie, a nie formalność.
