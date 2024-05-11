import os
from datetime import datetime
import subprocess
import re
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import shutil
import psutil
import time
import threading

class Logger:
  """
  Klasa Logger do obsługi operacji związanych z logowaniem.
  """
  # Stała formatu logu
  LOG_FORMAT = "[{timestamp}] {message}\n"

  @staticmethod
  # Metoda do logowania wiadomości
  def log(message: str, log_file: str = "log.txt"):
    """
    Loguje wiadomość z timestampem.

    Args:
    - message (str): Wiadomość do zalogowania.
    - log_file (str): Ścieżka do pliku z logami.
    """
    # Pobierz aktualny znacznik czasu
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Sformatuj wpis do logu z użyciem stałej LOG_FORMAT
    log_entry = Logger.LOG_FORMAT.format(timestamp=timestamp, message=message)

    try:
      # Otwórz plik logu w trybie dołączania i zapisz wpis
      with open(log_file, 'a') as log:
        log.write(log_entry)
    #W przypadku błędu zapisu do pliku logu, wyświetl komunikat o błędzie        
    except Exception as e:
      print(f"Błąd zapisu do pliku logu: {e}")

class FileMonitor:    
  """
  Klasa FileMonitor do monitorowania informacji związanych z systemem.
  """    
  def monitor_procesow(self):
    """
    Monitoruje działające procesy i wyświetla związane z nimi informacje.
    """
    try:
      # Uruchom komendę tasklist w celu uzyskania informacji o procesach
      result = subprocess.run(['tasklist', '/fo', 'csv', '/nh'], capture_output=True, text=True)

      # Przetwarzaj każdą linię wyniku
      for line in result.stdout.splitlines():
        process_info = line.split(',')

        # Pobierz podstawowe informacje o procesie
        process_name = process_info[0].strip('""')
        process_pid = process_info[1].strip('""')

        # Sprawdź dostępność informacji i przypisz odpowiednie wartości
        process_status = process_info[2].strip('""') if len(process_info) >= 3 else "N/A"
        process_cpu = process_info[3].strip('""') if len(process_info) >= 4 else "N/A"
        process_memory = process_info[4].strip('""') if len(process_info) >= 5 else "N/A"
        process_cpu_usage = process_info[5].strip('""') if len(process_info) >= 6 else "N/A"
        process_kernel_time = process_info[7].strip('""') if len(process_info) >= 8 else "N/A"

        # Loguj i wyświetl informacje o procesie
        Logger.log(f"Proces: {process_name}, Status: {process_status}, PID: {process_pid}, CPU: {process_cpu}, Pamięć: {process_memory}, Obciążenie CPU: {process_cpu_usage}, Czas CPU systemu: {process_kernel_time}")
        print(f"Proces: {process_name}, Status: {process_status}, PID: {process_pid}, CPU: {process_cpu}, Pamięć: {process_memory}, Obciążenie CPU: {process_cpu_usage}, Czas CPU systemu: {process_kernel_time}")

    except Exception as e:
        # W przypadku błędu podczas monitorowania procesów, wyświetl komunikat o błędzie
        print(f"Błąd: {e}")
        # Loguj błąd, w tym przypadku można dodać informacje o błędnym procesie
        Logger.log(f"Błąd podczas monitorowania procesów. Proces: {process_name}")

class FileAnalizaSys:
    def convert_memory_str_to_bytes(self, memory_str):
        """
        Konwertuje ciąg reprezentujący zużycie pamięci do bajtów.

        Args:
        - memory_str (str): Ciąg reprezentujący zużycie pamięci z jednostką (np. '8 K').

        Returns:
        - int: Wartość zużycia pamięci w bajtach.
        """
        units = {'K': 1024, 'M': 1024 ** 2, 'G': 1024 ** 3, 'T': 1024 ** 4}
        match = re.match(r'(\d+)\s*([KMG]?)', memory_str)
        if match:
            value, unit = match.groups()
            return int(value) * units.get(unit, 1)
        else:
            raise ValueError(f"Nieprawidłowy format pamięci: {memory_str}")

    def analiza_pamieci(self, sort_by_memory=True, filter_threshold=None):
        """
        Analizuje zużycie pamięci przez działające procesy.

        Args:
        - sort_by_memory (bool): Określa, czy wyniki mają być posortowane według zużycia pamięci.
        - filter_threshold (float): Prog zużycia pamięci, poniżej którego procesy nie będą uwzględniane.

        Returns:
        - List: Lista słowników reprezentujących procesy i ich zużycie pamięci.
        """        
        try:
            # Uruchomienie komendy tasklist w celu uzyskania informacji o procesach
            result = subprocess.run(['tasklist', '/fo', 'csv', '/nh'], capture_output=True, text=True)

            processes = []
            for line in result.stdout.splitlines():
                process_info = line.split(',')

                process_name = process_info[0].strip('""')
                process_memory = process_info[4].strip('""')

                # Sprawdzenie progów zużycia pamięci
                if filter_threshold is not None and self.convert_memory_str_to_bytes(process_memory) < filter_threshold:
                    continue
                
                # Dodanie informacji o procesie do listy
                processes.append({
                    'ProcessName': process_name,
                    'MemoryUsage': process_memory
                })

            # Sortowanie wyników według zużycia pamięci, jeśli wymagane
            if sort_by_memory:
                processes = sorted(processes, key=lambda x: self.convert_memory_str_to_bytes(x['MemoryUsage']), reverse=True)

            # Wyświetlenie wyników
            self.display_results(processes)
            return processes

        except Exception as e:
            print(f"Błąd: {e}")
            # Zapis błędu w logach przy użyciu klasy Logger
            Logger.log("Błąd podczas analizy pamięci.")

    def display_results(self, processes):
        """
        Wyświetla wyniki analizy pamięci.

        Args:
        - processes (List): Lista słowników reprezentujących procesy i ich zużycie pamięci.
        """
        if not processes:
            print("Brak procesów spełniających kryteria.")
        else:
            for process in processes:
                print(f"Proces: {process['ProcessName']}, Pamięć: {process['MemoryUsage']}")

            # Wyświetlenie wykresu słupkowego przedstawiającego zużycie pamięci
            self.plot_memory_usage(processes)

    def plot_memory_usage(self, processes):
            process_names = [process['ProcessName'] for process in processes]
            memory_usages = [self.convert_memory_str_to_bytes(process['MemoryUsage']) for process in processes]

            plt.figure(figsize=(10, 6))
            plt.bar(process_names, memory_usages, color='blue')
            plt.xlabel('Procesy')
            plt.ylabel('Zużycie pamięci (Bajty)')
            plt.title('Zużycie pamięci przez procesy')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()

            # Zapisz wykres do pliku 
            plt.savefig('memory_usage_chart.png')

            # Wyświetl wykres 
            plt.show()

class FileExplorer:
    def display_menu_2(self):
        """
        Wyświetla menu eksploratora systemu plików.
        """
        print("\n=== Eksplorator Systemu Plików ===")
        print("1. Wyświetl zawartość bieżącego folderu lub podaj ścieżkę do folderu")
        print("2. Wyświetl właściwości pliku/folderu")
        print("3. Utwórz plik")
        print("4. Utwórz katalog")
        print("5. Zmodyfikuj plik")
        print("6. Skopiuj plik")
        print("7. Usuń plik")
        print("8. Skopiuj katalog")
        print("9. Usuń katalog")
        print("0. Powrót do głównego menu")

    def explore_file_system(self):
        """
        Główna funkcja eksploratora systemu plików.
        """
        while True:
            self.display_menu_2()
            choice = input("\n Wybierz numer funkcji (0-9): ").strip()

            if choice.isdigit():
                choice = int(choice)

                if choice == 0:
                    print("Powrót do głównego menu.")
                    break

                elif choice == 1:
                    self.display_current_folder_content()

                elif choice == 2:
                    self.display_file_properties()

                elif choice == 3:
                    self.create_file()

                elif choice == 4:
                    self.create_directory()

                elif choice == 5:
                    self.modify_file()

                elif choice == 6:
                    self.copy_file()

                elif choice == 7:
                    self.delete_file()

                elif choice == 8:
                    self.copy_directory()

                elif choice == 9:
                    self.delete_directory()

                else:
                    print(f"Nieprawidłowa opcja '{choice}'. Spróbuj jeszcze raz.")

            else:
                print(f"Nieprawidłowy format '{choice}'. Spróbuj jeszcze raz.")
    
    def display_current_folder_content(self):
        """
        Wyświetla zawartość bieżącego folderu.
        """
        current_folder = input("\nPodaj ścieżkę folderu (naciśnij Enter, aby użyć bieżącego folderu): ").strip() or os.getcwd()
        print(f"\nZawartość folderu: {current_folder}")

        try:
            with os.scandir(current_folder) as entries:
                for entry in entries:
                    entry_type = "Folder" if entry.is_dir() else "Plik"
                    print(f"{entry_type}: {entry.name}")

        except Exception as e:
            print(f"Błąd podczas wyświetlania zawartości folderu: {e}")
            Logger.log(f"Błąd podczas wyświetlania zawartości folderu {current_folder}: {e}")

    def display_file_properties(self):
        """
        Wyświetla właściwości pliku/folderu.
        """
        file_name = input("\nPodaj nazwę pliku/folderu (możesz podać ścieżkę do dowolnego pliku lub folderu): ").strip()

        try:
            file_stats = os.stat(file_name)

            # Konwersja czasu do czytelnej formy
            modification_time = datetime.fromtimestamp(file_stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')

            print("\nWłaściwości pliku/folderu:")
            print(f"Rozmiar: {file_stats.st_size} bajtów")
            print(f"Czas ostatniej modyfikacji: {modification_time}")

        except Exception as e:
            print(f"Błąd podczas wyświetlania właściwości pliku/folderu: {e}")
            Logger.log(f"Błąd podczas wyświetlania właściwości pliku/folderu {file_name}: {e}")

    def create_file(self):
        file_path = input("Podaj ścieżkę i nazwę nowego pliku (np. C:/Users/informatyka/Desktop/eco_plik.txt): ")
        content = input("Czy chcesz wprowadzić zawartość pliku? (T/N): ").lower()
        
        if content == "t":
            content = input("Podaj zawartość pliku: ")

        try:
            with open(file_path, 'w') as file:
                file.write(content)
            Logger.log(f"Utworzono plik: {file_path}")
            print(f"Utworzono plik: {file_path}")
        except Exception as e:
            print(f"Błąd: {e}")

    def create_directory(self):
        dir_path = input("Podaj ścieżkę do nowego katalogu (np. C:/Users/informatyka/Desktop/eco_data/): ")

        try:
            os.makedirs(dir_path, exist_ok=True)
            Logger.log(f"Utworzono katalog: {dir_path}")
            print(f"Utworzono katalog: {dir_path}")
        except Exception as e:
            print(f"Błąd: {e}")

    def modify_file(self):
        file_path = input("Podaj ścieżkę do pliku do modyfikacji: ")
        new_content = input("Podaj nową zawartość pliku: ")

        try:
            with open(file_path, 'w') as file:
                file.write(new_content)
            Logger.log(f"Zmodyfikowano plik: {file_path}")
            print(f"Zmodyfikowano plik: {file_path}")
        except Exception as e:
            print(f"Błąd: {e}")

    def copy_file(self):
        source_path = input("Podaj ścieżkę do pliku źródłowego: ")
        destination_path = input("Podaj ścieżkę do pliku docelowego: ")

        try:
            shutil.copy2(source_path, destination_path)
            Logger.log(f"Skopiowano plik z {source_path} do {destination_path}")
            print(f"Skopiowano plik z {source_path} do {destination_path}")
        except Exception as e:
            print(f"Błąd: {e}")

    def delete_file(self):
        file_path = input("Podaj ścieżkę do pliku do usunięcia: ")

        try:
            os.remove(file_path)
            Logger.log(f"Usunięto plik: {file_path}")
            print(f"Usunięto plik: {file_path}")
        except Exception as e:
            print(f"Błąd: {e}")

    def copy_directory(self):
        source_path = input("Podaj ścieżkę do katalogu źródłowego: ")
        destination_path = input("Podaj ścieżkę do katalogu docelowego: ")

        try:
            shutil.copytree(source_path, destination_path)
            Logger.log(f"Skopiowano katalog z {source_path} do {destination_path}")
            print(f"Skopiowano katalog z {source_path} do {destination_path}")
        except Exception as e:
            print(f"Błąd: {e}")

    def delete_directory(self):
        dir_path = input("Podaj ścieżkę do katalogu do usunięcia: ")

        try:
            shutil.rmtree(dir_path)
            Logger.log(f"Usunięto katalog: {dir_path}")
            print(f"Usunięto katalog: {dir_path}")
        except Exception as e:
            print(f"Błąd: {e}")

class FileIOMonitor:
    def __init__(self, interval=1):
        self.interval = interval
        self.running = True

    def monitor_io_operations(self):
        print(">>> W celu zakończenia programu wciśnij Ctrl + C <<<")
        time.sleep(self.interval * 4)
        try:            
            while self.running:
                io_counters = psutil.disk_io_counters(perdisk=True)
                
                for disk, counter in io_counters.items():
                    read_bytes = counter.read_bytes
                    write_bytes = counter.write_bytes

                    log_message = f"I/O on Disk '{disk}': Read {read_bytes} bytes, Write {write_bytes} bytes"
                    Logger.log(log_message)
                    print(log_message)                    

                time.sleep(self.interval)

        except KeyboardInterrupt:
            print("Program interrupted by user.")
        except Exception as e:
            print(f"Error: {e}")
            Logger.log("Error during I/O monitoring.")

    def stop_monitoring(self):
        self.running = False

class NetworkActivityMonitor:
    def __init__(self, interval=1, log_file="network_activity.log"):
        self.interval = interval
        self.log_file = log_file
        self.logger = Logger()

        self.is_running = False

    def start_monitoring(self):
        self.is_running = True
        self.monitor_thread = threading.Thread(target=self.monitor_network_activity)
        self.monitor_thread.start()

    def stop_monitoring(self):
        self.is_running = False
        self.monitor_thread.join()

    def monitor_network_activity(self):
        try:
            while self.is_running:
                open_ports = self.get_open_ports()
                active_connections = self.get_active_connections()
                network_stats = psutil.net_io_counters()

                self.write_to_log(open_ports, active_connections, network_stats)

                psutil.net_io_counters.cache_clear()
                time.sleep(self.interval)
        except Exception as e:
            print(f"Error: {e}")

    def get_open_ports(self):
        open_ports = []
        for conn in psutil.net_connections(kind='inet'):
            if conn.status == psutil.CONN_LISTEN:
                open_ports.append(conn.laddr.port)
        return open_ports

    def get_active_connections(self):
        active_connections = []
        for conn in psutil.net_connections(kind='inet'):
            if conn.status == psutil.CONN_ESTABLISHED:
                connection_info = {
                    'local_address': conn.laddr.ip,
                    'local_port': conn.laddr.port,
                    'remote_address': conn.raddr.ip,
                    'remote_port': conn.raddr.port
                }
                active_connections.append(connection_info)
        return active_connections

    def write_to_log(self, open_ports, active_connections, network_stats):
        log_message = "\n=== Network Activity Log ===\n"
        log_message += f"Open Ports: {open_ports}\n"
        log_message += "\nActive Connections:\n"
        for connection in active_connections:
            log_message += f"{connection['local_address']}:{connection['local_port']} -> {connection['remote_address']}:{connection['remote_port']}\n"
        log_message += f"\nBandwidth Usage: {network_stats.bytes_sent} bytes sent, {network_stats.bytes_recv} bytes received\n"

        self.logger.log(log_message, self.log_file)

    @staticmethod
    def display_menu(network_monitor):
        while True:
            print("\n=== Network Monitoring ===")
            print("1. Start Monitoring")
            print("2. Stop Monitoring")
            print("3. Wyjście")

            choice = input("Wybierz opcje (1-3): ")

            if choice == "1":
                network_monitor.start_monitoring()
            elif choice == "2":
                network_monitor.stop_monitoring()
            elif choice == "3" or choice.lower() == "q":
                break
            else:
                print("Niewłaściwy wybór. Spróbuj jeszcze raz.")

class UserManager:
    def __init__(self):
        self.logged_in_users = set()
        self.logger = Logger()

    def login_user(self, username):
        self.logged_in_users.add(username)
        log_message = f"Użytkownik '{username}' zalogował się."
        self.logger.log(log_message)

    def logout_user(self, username):
        self.logged_in_users.discard(username)
        log_message = f"Użytkownik '{username}' wylogował się."
        self.logger.log(log_message)

    def get_logged_in_users(self):
        return list(self.logged_in_users)

    def log_user_activity(self, action, username):
        message = f"{action} użytkownika: {username}"
        print(message)
        self.logger.log(message)

    def display_menu(self):
        while True:
            print("\n=== Zarządzanie Użytkownikami ===")
            print("1. Zaloguj użytkownika")
            print("2. Wyloguj użytkownika")
            print("3. Wyświetl zalogowanych użytkowników")
            print("4. Wyjście")

            choice = input("Wybierz opcję (1-4): ")

            if choice == "1":
                username = input("Podaj nazwę użytkownika do zalogowania: ")
                self.login_user(username)
                self.log_user_activity("Zalogowanie", username)
            elif choice == "2":
                username = input("Podaj nazwę użytkownika do wylogowania: ")
                self.logout_user(username)
                self.log_user_activity("Wylogowanie", username)
            elif choice == "3":
                logged_in_users = self.get_logged_in_users()
                print("Zalogowani użytkownicy:", logged_in_users)
                log_message = f"Zalogowani użytkownicy: {', '.join(logged_in_users)}"
                self.logger.log(log_message)
            elif choice == "4":
                break
            else:
                print("Nieprawidłowa opcja. Spróbuj ponownie.")

class MonitorUslugSystemowych:
    def __init__(self):
        self.logger = Logger()

    def wyswietl_liste_uslug(self):
        try:
            # Pobiera liste dzialajacych uslug/daemonow
            wynik = subprocess.run(["sc", "query", "type=", "service", "state=", "all"], capture_output=True, text=True, encoding='cp1250', errors='replace')
            lista_uslug = wynik.stdout.splitlines()

            # Sprawdza czy proces zakonczyl sie poprawnie
            if wynik.returncode == 0:
                lista_uslug = wynik.stdout.splitlines()

                # Zapisuje liste do pliku logu
                log_message = f"\n=== Lista Uslug Systemowych ===\n{datetime.now()}\n"
                log_message += "\n".join(lista_uslug)
                self.logger.log(log_message)

                # Wyswietla liste w konsoli
                for linia in lista_uslug:
                    print(linia)

            else:
                print("Blad podczas pobierania listy uslug.")

        except Exception as e:
            print(f"Blad: {e}")








