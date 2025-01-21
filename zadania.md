# Zadania do wykonania:
Uwaga usunąć przed przesłaniem !

## Zadanie 1
- [x] obraz z tagiem latest budowany jest z wybranej gałęzi np. main
- [x] Pull Requesty / Merge Requesty lub bezpośrednie pushe do repozytorium może wykonywać 
wyłącznie właściciel repozytorium
- [x] Nowe gałęzie może tworzyć dowolny użytkownik
- [x] Wypchnięcie zmiany do nowej gałęzi ma skutkować uruchomieniem procesu cicd, który zbuduje 
obraz dockerowy o tagu :beta
Powyższe chyba działają

- [ ] Przed zbudowaniem jakiejkolwiek wersji proces CICD musi uruchomić: testy jednostkowe, testy 
SCA, testy SAST oraz testy DAST

## Zadanie 2
- [ ] Przygotować nową gałęź kodu, w której dodana zostaną 2 nowe podatności bezpieczeństwa - mogą 
to być podatności typu wstrzyknięcia kodu, podatności które wykorzystują podatność w bibliotece 
opensource lub inne - ważne żeby faktycznie można było zaprezentować, że kod w nowej 
gałęzi zawiera podatność bezpieczeństwa która prowadzi do wystąpienia incydentu. Czyli - 
jeśli dodano lub zmieniono kod tak aby można było wykorzystać podatność SQL Injection ta 
podatność powinna być możliwa do wykorzystania, analogicznie w przypadku podatności w 
bibliotekach  opensource,  nie  wystarczy  dodać  do  pliku  pom.xml  lub  requirements.txt 
biblioteki, która zawiera podatność - ta podatność musi być możliwa do wykorzystania 
- [ ] Zweryfikować, czy proces CICD uruchomiony na nowej gałęzi się nie powiedzie (tutaj czytaj uwagi 
w kolejnej części)