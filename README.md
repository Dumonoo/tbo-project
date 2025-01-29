# Projekt TBO Zespół nr 5

## Członkowie zespołu:
- Michał Łezka
- Dominik Nowak
- Maciej Domański
- Jonatan Kasperczak

## Wstęp

Projekt z przedmiotu TBO opiera się na stworzeniu procesu CICD do wybranej aplikacji który będzie uruchamiał odpowiednie testy i następnie (jeżeli testy przejdą pozytywnie) tworzył build aplikacji i go publikował.

## Wybrana aplikacja
Jako aplikację do przetestowania procesu CICD wybraliśmy projekt udostępniany w ramach laboratorium nr 2, będący prostą aplikacją w Flask stworzoną przy użycia języka Python.

# Projekt procesu CICD

Nasz proces CICD został utworzony przy pomocy GitHub Actions i składa się z kilku rodzajów testów:
Utworzone rodzaje testów to:
- jednostkowe
- SCA
- SAST
- DAST

Pomyślne zakończenie testów skutkuje zbudowaniem aplikacji i jej publikację.

Przykładowe wyniki testów można zobaczyć w Jobie: ...
Będzie on później używany jako porównanie czy testy wykrywają nowe podatnośći w 2 części projektu.


### test SCA

Test SCA został przeprowadzony za pomocą pyupio/safety (podobnie jak w trakcie lab 2).
Tworzy on obraz dockerowy, pobiera pyupio/safety i przeprowadza test.
Nie użyto klucza API, co oznacza, że baza podatności jest aktualizowana co miesiąc, w przyszłości można utworzyć konto na Safety CLI, aby mieć dostęp do lepszej bazy danych podatności.

Wynik testu został umieszczony jako artefakt pod nazwą "sca raport", jest w nim plik .txt który zawiera listę podatnych paczek, do jakiej wersji owe podatności są oraz opisy tych podatności.


### test SAST 

W przypadku testów statycznych bezpieczeństwa aplikacji (SAST) wykorzystano skaner Bandit. Proces przebiegu tego zadania jest prosty i obejmuje analizę wszystkich plików w projekcie. 

Wyniki testu są zapisywane w artefakcie `bandit-report.html`, który można pobrać z widoku artefaktów. Jeśli podczas skanowania zostaną wykryte jakiekolwiek podatności, test zakończy się niepowodzeniem, co spowoduje przerwanie całego pipeline'u.


### test DAST

DAST (Dynamic Application Security Testing) to metoda testowania bezpieczeństwa aplikacji webowych, która polega na dynamicznej analizie działającej aplikacji. Narzędzia DAST działają podobnie do atakujących – wysyłają zapytania do aplikacji, analizują odpowiedzi i sprawdzają, czy występują podatności, takie jak:

- SQL Injection
- Cross-Site Scripting (XSS)
- Problemy z nagłówkami bezpieczeństwa
- Brak odpowiednich mechanizmów uwierzytelniania i autoryzacji
DAST nie wymaga dostępu do kodu źródłowego aplikacji (w przeciwieństwie do SAST – Static Application Security Testing), ponieważ analizuje jedynie interakcje na poziomie HTTP/S.

W pipeline CI/CD aplikacja jest najpierw pobierana z repozytorium, a następnie budowana i uruchamiana w kontenerze Docker na lokalnym porcie 5000. Następnie narzędzie OWASP ZAP przeprowadza test DAST, skanując aplikację pod kątem podatności. Jeśli zostaną wykryte problemy, proces CI/CD może zostać zatrzymany. Wynik jest widoczny jako artefakt "zap_scan".


### testy jednostkowe

Dokumentacja wygenerowana przez chatGPT 4o

Repozytorium zawiera zestaw testów jednostkowych i bezpieczeństwa dla aplikacji. Testy napisane są w `pytest` i sprawdzają:
- **Walidację danych** w modelach (`Books`, `Customers`, `Loans`).
- **Odporność aplikacji** na **SQL Injection**, **XSS**, **IDOR** i inne ataki.
- **Poprawność API i widoków** aplikacji.

---

## **🧪 Struktura Testów**
| 📁 **Folder** | 📝 **Plik** | 🛠 **Opis Testów** |
|--------------|------------|------------------|
| `tests/books/` | `test_models.py` | Walidacja modelu `Book` |
| `tests/core/` | `test_views.py` | Testy widoków aplikacji |
| `tests/customers/` | `test_models.py` | Walidacja modelu `Customer` |
| `tests/customers/` | `test_security.py` | Testy podatności SQL Injection |
| `tests/customers/` | `test_xss.py` | Testy podatności XSS |
| `tests/loans/` | `test_models.py` | Walidacja modelu `Loan` |
| `tests/` | `conftest.py` | Konfiguracja testów i baza testowa |

---

## **📂 Opis Plików Testowych**

### **📌 `tests/books/test_models.py`**
**Sprawdza:**
✅ Poprawne tworzenie obiektu `Book`.  
✅ Walidację pól (`name`, `year_published`, `book_type`).  
✅ Ochronę przed **błędnymi danymi** w modelu.  

**Metoda walidacji:**
- Tworzy obiekt `Book()` i sprawdza, czy jest poprawny.
- Oczekuje `ValueError`, jeśli dane są nieprawidłowe.

---

### **📌 `tests/core/test_views.py`**
**Sprawdza:**
✅ Dostępność głównej strony (`index`).  
✅ Poprawność odpowiedzi HTTP (`200 OK`).  
✅ Ochronę przed **błędnym HTML i XSS**.  

**Metoda walidacji:**
- Wysyła `GET /` i sprawdza zawartość HTML (`<!DOCTYPE html>`).

---

### **📌 `tests/customers/test_models.py`**
**Sprawdza:**
✅ Walidację danych klientów (`name`, `pesel`, `appNo`).  
✅ Odrzucanie pustych pól lub niepoprawnych wartości.  
✅ Ochronę przed **błędnymi danymi wejściowymi**.  

**Metoda walidacji:**
- Tworzy obiekt `Customer()`, oczekując poprawnych wyników.
- Dla błędnych danych oczekuje `ValueError`.

---

### **📌 `tests/customers/test_security.py`**
**Sprawdza:**
✅ Ochronę przed **SQL Injection**.  
✅ Poprawność obsługi wstrzykniętych zapytań SQL.  
✅ Bezpieczeństwo zapytań ORM (SQLAlchemy).  

**Metoda walidacji:**
- Wprowadza SQL Injection (`' OR 1=1 --`) i sprawdza, czy system je blokuje.

---

### **📌 `tests/customers/test_xss.py`**
**Sprawdza:**
✅ Ochronę przed **XSS (Cross-Site Scripting)**.  
✅ Poprawność sanitizacji pól (`name`, `city`, `street`).  
✅ Oczekiwanie `ValueError`, jeśli XSS zostanie wykryty.  

**Metoda walidacji:**
- Tworzy `Customer()` z XSS payloadami (`<script>alert('XSS')</script>`).
- Sprawdza, czy XSS został usunięty lub zablokowany.

---

### **📌 `tests/loans/test_models.py`**
**Sprawdza:**
✅ Poprawne tworzenie obiektu `Loan`.  
✅ Walidację pól (`loan_date`, `return_date`).  
✅ Ochronę przed **niepoprawnym formatem daty**.  

**Metoda walidacji:**
- Tworzy `Loan()` z poprawnymi danymi i sprawdza, czy `loan.id != None`.
- Sprawdza, czy złe wartości dat podnoszą `ValueError`.

---

### **📌 `tests/conftest.py`**
**Zawiera:**
✅ Konfigurację testów.  
✅ **Baza testowa SQLite (in-memory).**  
✅ **Fixures** dla `Book`, `Customer`, `Loan` (przykładowe dane).  

**Metoda działania:**
- Tworzy i usuwa bazę danych dla testów.
- Konfiguruje klienta testowego (`client()`).

---

## **🚀 Uruchamianie Testów**
Aby uruchomić **wszystkie testy**:
```bash
pytest
```

# Próba wprowadzenia podatności

W tej części projektu naszym celem była próba wprowadzenia 2 podatności do repozytorium poprzez utworzenie nowego brancha i stworzenie nowego Pull Request'a do głównego brancha.
Jako iż część testów nie przechodzi gdyż wybrana przez nas aplikacja ma w sobie oryginalnie podatności będziemy ukazywać poniżej screeny sprzed i po próbe jej wprowadzenia aby pokazać, że nasze testy je wykrywają.
Job który używamy do porównania: ...

Wybrane przez nas podatności to:
- ...
- ...

### Podatność ...

Owa podatność polega na ...
Link do joba który wykrył ową podatność: ...

Screen przed testem:
...

Screen po teście:
...

### Podatność ...

Owa podatność polega na ...
Link do joba który wykrył ową podatność: ...

Screen przed testem:
...

Screen po teście:
...
