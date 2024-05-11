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

3. Biblioteki Wykorzystane w Projekcie
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
