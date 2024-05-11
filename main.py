# STAWISZYNSKI RADOSLAW , NR INDEKSU 159088, 
# ROK 2023/2024, WYDZIAL INFORMATYKA, GRUPA D1, SEM 2


from file_def import FileMonitor, FileAnalizaSys, FileExplorer, FileIOMonitor, NetworkActivityMonitor, UserManager, MonitorUslugSystemowych


def display_menu():
    """
    Display the main menu of the program.
    """
    print("\n=== Menu ===")
    print("UWAGA - program stworzony na systemie Windows 10 Pro i tylko dla systemu Windows")
    print("1. Monitor Procesów")
    print("2. Analiza Pamięci")
    print("3. Eksplorator Systemu Plików")
    print("4. Monitor Wejścia-Wyjścia")
    print("5. Analiza Aktywności Sieciowej")
    print("6. Konta Użytkowników")
    print("7. Monitor Usług Systemowych")
    print("0. Wyjście z programu")

def main():
    file_monitor = FileMonitor()
    file_analiza_sys = FileAnalizaSys()
    file_explorer = FileExplorer()
    io_monitor = FileIOMonitor()
    network_monitor = NetworkActivityMonitor()
    manager = UserManager()
    monitor_uslug = MonitorUslugSystemowych()
    
    while True:
      display_menu()
      choice = input("\n Wybierz numer funkcji (0-8): ").strip()

      if choice.isdigit():
        choice = int(choice)

        if 0 <= choice <= 8:
          if choice == 0:
            print("Zamykanie programu. Do widzenia!")
            break

          elif choice == 1:            
            file_monitor.monitor_procesow()
          
          elif choice == 2:
            file_analiza_sys.analiza_pamieci(sort_by_memory=True, filter_threshold=100)
            
          elif choice == 3:
            file_explorer.explore_file_system()

          elif choice == 4:
            io_monitor.monitor_io_operations()
          
          elif choice == 5:
            network_monitor.display_menu(network_monitor)

          elif choice == 6:
            manager.display_menu()
          
          elif choice == 7:
            monitor_uslug.wyswietl_liste_uslug()

          else:
            print("Nieprawidłowy numer funkcji. Spróbuj ponownie.")
            print()

        else:
          print(f"Nieprawidłowa opcja '{choice}'. Spróbuj jeszcze raz.")

      else:
        print(f"Nieprawidłowy format '{choice}'. Spróbuj jeszcze raz.")


if __name__ == "__main__":
    main()

        
