# Projekt: Narzędzia do monitorowania i analizy systemu operacyjnego

Autor: Radosław Stawiszyński
Rok: 2023/2024
Wydział: Informatyka

## 1. Dokumentacja Programu Monitorującego System Operacyjny

W niniejszym dokumencie przedstawiam program do monitorowania i analizy systemu operacyjnego. Omówię cele projektu, kluczowe aspekty związane z jego działaniem oraz interakcję z programem.

### Cele Projektu

Głównym celem programu jest umożliwienie praktycznego monitorowania i analizy różnych elementów funkcjonowania systemu operacyjnego. Projekt zakłada stworzenie zestawu narzędzi w języku Python, które pozwolą użytkownikowi zrozumieć i kontrolować mechanizmy zarządzania systemem operacyjnym.

### Interakcja z Programem

Podczas korzystania z programu, prezentowane są funkcje narzędzia, kluczowe fragmenty kodu oraz sposób efektywnej współpracy z programem.

### Wsparcie Systemowe

Program został zaprojektowany z myślą o prostocie i dostępności. Wystarczy, że masz zainstalowanego Pythona, aby czerpać korzyści z mojego narzędzia.

### Dokumentacja Techniczna

W razie potrzeby, dostępna jest pełna dokumentacja programu, zawierająca szczegółowe informacje dotyczące implementacji, wykorzystanych technologii i ewentualnych wymagań systemowych.

### Wnioski

Mam nadzieję, że po zapoznaniu się z programem zyskasz nowe spojrzenie na działanie systemu operacyjnego. To narzędzie jest gotowe do pomocy w zgłębianiu tajników Pythona i systemu operacyjnego.

## 2. Monitor Systemu Plików i Narzędzia

To repozytorium zawiera kolekcję skryptów w języku Python, które dostarczają różne funkcje monitorowania systemu plików oraz narzędziowe.

### Instalacja

Aby zainstalować monitor systemu plików i narzędzia, wykonaj następujące kroki:

Sklonuj repozytorium na swój lokalny komputer za pomocą poniższej komendy:

Copy code:
git clone https://github.com/username/file-system-monitor-and-utilities.git
Przejdź do katalogu sklonowanego repozytorium:

Copy code:
cd file-system-monitor-and-utilities

Zainstaluj wymagane zależności Pythona za pomocą poniższej komendy:

Copy code:
pip install -r requirements.txt

Użycie
Po zakończeniu instalacji możesz korzystać z różnych skryptów dostarczonych w repozytorium. Poniżej znajduje się krótka prezentacja każdego skryptu i sposób ich użycia:

- FileMonitor.py: Ten skrypt dostarcza monitorowanie w czasie rzeczywistym działających procesów na twoim systemie.

- FileAnalizaSys.py: Pozwala analizować użycie pamięci działających procesów.

- FileExplorer.py: Zapewnia interfejs eksploratora plików, który umożliwia nawigację po systemie plików.

- FileIOMonitor.py: Monitoruje operacje wejścia/wyjścia na dysku w systemie.

- NetworkActivityMonitor.py: Monitoruje aktywność sieciową w systemie.

- UserManager.py: Pozwala zarządzać kontami użytkowników w systemie.

- SystemServiceMonitor.py: Monitoruje usługi systemowe w systemie.

### Dodatkowe uwagi

Upewnij się, że masz niezbędne uprawnienia do instalowania i uruchamiania tych skryptów na swoim systemie.

## 3. Biblioteki Wykorzystane w Projekcie

Projekt wykorzystuje różne biblioteki Pythona do monitorowania systemu plików. Poniżej znajdziesz krótkie wprowadzenie do każdej z używanych bibliotek:

- os: Dostarcza funkcje do interakcji z systemem operacyjnym.
- datetime: Obsługuje daty i czasy, używane do rejestrowania zdarzeń w logach.
- subprocess: Umożliwia uruchamianie nowych procesów.
- re: Pozwala na przetwarzanie tekstów za pomocą wyrażeń regularnych.
- matplotlib.pyplot: Narzędzie do tworzenia wykresów.
- shutil: Umożliwia operacje na plikach i katalogach.
- psutil: Interfejs do monitorowania zasobów systemowych.
- time: Dostarcza funkcje związane z pomiar czasu.
- threading: Moduł do zarządzania wątkami.

Te biblioteki stanowią solidne podstawy do skutecznego monitorowania i zarządzania systemem plików.

## 4. Przewodnik Użytkownika

### Instrukcje Obsługi Programu

Program File System Monitor and Utilities oferuje kilka głównych funkcji, które umożliwiają monitorowanie i zarządzanie różnymi aspektami systemu plików w systemie Windows 10 Pro. Poniżej znajdziesz instrukcje dotyczące obsługi poszczególnych funkcji:

### Monitor Procesów:

Wybierz opcję nr 1 z menu.
Program wyświetli informacje na temat działających procesów, takie jak nazwa procesu, PID, status, zużycie CPU, zużycie pamięci i czas jądra.
Aby zakończyć monitorowanie procesów, naciśnij klawisz "0" w menu.

### Analiza Pamięci:

Wybierz opcję nr 2 z menu.
Program umożliwia analizę zużycia pamięci przez działające procesy. Wyniki są sortowane według zużycia pamięci.
Zużycie pamięci wyświetlone zostaje w postaci grafiki.
Aby zakończyć analizę pamięci, naciśnij klawisz "0" w menu.

### Eksplorator Systemu Plików:

Wybierz opcję nr 3 z menu.
Program zapewnia interfejs eksploratora plików, pozwalając na nawigację po systemie plików, przeglądanie właściwości plików, tworzenie nowych plików i katalogów, modyfikację istniejących plików oraz kopiowanie i usuwanie plików i katalogów.
Aby zakończyć korzystanie z eksploratora, naciśnij klawisz "0" w menu.

### Monitor Wejścia-Wyjścia:

Wybierz opcję nr 4 z menu.
Program monitoruje operacje wejścia-wyjścia (I/O) na dyskach systemowych, wyświetlając ilość danych odczytywanych i zapisywanych na każdym dysku w określonych interwałach.
Aby zakończyć monitorowanie I/O, naciśnij klawisz "0" w menu.

### Analiza Aktywności Sieciowej:

Wybierz opcję nr 5 z menu.
Program monitoruje aktywność sieciową, wyświetlając informacje o otwartych portach, aktywnych połączeniach i użyciu przepustowości sieciowej.
Aby zakończyć monitorowanie aktywności sieciowej, naciśnij klawisz "0" w menu.

### Konta Użytkowników:

Wybierz opcję nr 6 z menu.
Program umożliwia zarządzanie kontami użytkowników, wyświetlając listę użytkowników, dodając nowych użytkowników, usuwając istniejących użytkowników oraz modyfikując właściwości użytkowników.
Aby zakończyć zarządzanie kontami użytkowników, naciśnij klawisz "0" w menu.

### Monitor Usług Systemowych:

Wybierz opcję nr 7 z menu.
Program umożliwia monitorowanie usług systemowych, wyświetlając listę wszystkich usług, uruchamiając i zatrzymując wybrane usługi oraz modyfikując ich właściwości.
Aby zakończyć monitorowanie usług systemowych, naciśnij klawisz "0" w menu.

## Przykłady Użycia wraz z Oczekiwanymi Rezultatami

Poniżej przedstawione są przykłady użycia programu wraz z oczekiwanymi rezultatami dla każdej głównej funkcji:

### Monitor Procesów:

Użytkownik uruchamia monitor procesów, a następnie obserwuje na bieżąco informacje o działających procesach.

### Analiza Pamięci:

Użytkownik uruchamia analizę pamięci, a następnie otrzymuje posortowaną listę procesów według zużycia pamięci.

### Eksplorator Systemu Plików:

Użytkownik korzysta z eksploratora systemu plików do nawigacji, przeglądania właściwości plików, tworzenia nowych plików i katalogów oraz modyfikacji istniejących plików.

### Monitor Wejścia-Wyjścia:

Użytkownik uruchamia monitor I/O, a następnie obserwuje ilość danych odczytywanych i zapisywanych na dyskach systemowych.

### Analiza Aktywności Sieciowej:

Użytkownik uruchamia monitor aktywności sieciowej, a następnie uzyskuje informacje o otwartych portach, aktywnych połączeniach i użyciu przepustowości sieciowej.

### Konta Użytkowników:

Użytkownik korzysta z funkcji zarządzania kontami użytkowników, wyświetlając listę użytkowników, dodając nowych użytkowników, usuwając istniejących użytkowników oraz modyfikując właściwości użytkowników.

### Monitor Usług Systemowych:

Użytkownik uruchamia monitor usług systemowych, a następnie przegląda listę usług, uruchamia i zatrzymuje wybrane usługi oraz modyfikuje ich właściwości.

Teraz możesz swobodnie korzystać z programu i dostosowywać go do własnych potrzeb zgodnie z opisanymi funkcjami i przykładami użycia. W razie dodatkowych pytań lub problemów, skorzystaj z opcji pomocy lub skontaktuj się z właścicielem programu.

## 5. Podsumowanie / Informacje Końcowe

Program został zoptymalizowany i przetestowany na systemie Windows 10 Pro.
W przypadku korzystania z innego systemu operacyjnego, niektóre funkcje mogą nie działać poprawnie.
Jeśli napotkasz jakiekolwiek problemy lub masz pytania, śmiało skorzystaj z dokumentacji lub skontaktuj się z właścicielem programu.
Dziękujemy za skorzystanie z File System Monitor and Utilities. Mamy nadzieję, że program spełnił Twoje oczekiwania i ułatwił zarządzanie systemem plików. Życzymy udanych monitorowań i efektywnego zarządzania!
