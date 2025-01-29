# Projekt TBO Zespół nr 5

## Członkowie zespołu:
- Michał Łezka
- Dominik Nowak
- Maciej Domański
- Jonatan Kasperczak

## Wybrana aplikacja
Jako aplikację do przetestowania procesu CICD wybraliśmy projekt udostępniany w ramach laboratorium nr 2, będący prostą aplikacją w Flask stworzoną przy użycia języka Python.

# Projekt procesu CICD

Proces CICD składa się z kilku rodzajów testów których pomyślne zakończenie skutukje zbudowaniem i publikacją builda aplikacji.
Utworzone rodzaje testów to:
- jednostkowe
- SCA
- SAST
- DAST

### test SCA

Test SCA został przeprowadzony za pomocą pupio/safety (podobnie jak w trakcie lab 2).
Tworzy on obraz dockerowy, pobiera pupio/safety i przeprowadza test.
Nie użyto klucza API, co oznacza, że baza podatności jest aktualizowana co miesiąc, w przyszłości można utworzyć konto na Safety CLI, aby mieć dostęp do lepszej bazy danych podatności.

Wynik testu został umieszczony jako artefakt pod nazwą "sca raport", jest w nim plik .txt który zawiera listę podatnych paczek, do jakiej wersji owe podatności są oraz opisy tych podatności.

# Próba wprowadzenia podatności