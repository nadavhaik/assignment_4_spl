import sys

from context_manager import ContextManager


def main():
    print("Calling make -pizza..")
    cm = ContextManager(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    cm.run()
    print("                                                      ▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓                                          ")
    print("                                              ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                         ")
    print("                                      ▒▒▒▒▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓                                        ")
    print("                                ▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▓▓                                        ")
    print("                            ▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓                                        ")
    print("                        ▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓░░░░                                      ")
    print("                      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒░░░░░░░░░░                                    ")
    print("                    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓▒▒░░░░░░░░░░▓▓▓▓▓▓▓▓                                  ")
    print("                ▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░██▓▓▓▓▓▓▓▓▓▓                                ")
    print("             ▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓░░░░                            ")
    print("           ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░  ▓▓▓▓▓▓▓▓  ░░░░                            ")
    print("          ▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓▓▓▓▒▒░░░░░░░░░░░░▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░      ░░░░                          ")
    print("          ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░          ░░░░                        ")
    print("      ▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓  ░░░░░░                      ")
    print("    ▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░██▓▓▓▓▓▓▓▓▓▓  ░░░░░░                    ")
    print("  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░████▓▓▓▓▓▓▓▓░░░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ░░                    ")
    print("  ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ░░░░░░                ")
    print("  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒░░░░░░░░▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████▓▓▓▓▓▓▓▓░░    ░░░░░░░░              ")
    print("  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░      ░░░░              ")
    print("  ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░      ░░░░            ")
    print("  ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒░░░░░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░██▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░      ░░░░          ")
    print("    ▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░░░░░░░░░░░████▓▓▓▓▓▓▓▓░░░░░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░    ░░░░░░        ")
    print("      ▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓░░░░░░░░░░░░░░████░░░░░░░░░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░▓▓▓▓▓▓▓▓░░░░░░░░    ░░░░        ")
    print("          ▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░████▓▓▓▓▓▓▓▓░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░    ░░░░░░      ")
    print("              ▒▒▒▒▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░    ░░░░░░      ")
    print("                  ▒▒▒▒▒▒▒▒▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░    ░░░░░░    ")
    print("                    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░  ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████▓▓▓▓▓▓▓▓░░░░░░░░    ░░░░░░    ")
    print("                            ▒▒▒▒▒▒░░░░  ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░    ░░░░░░    ")
    print("                                  ▒▒░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░░░░░░░  ")
    print("                                  ▒▒░░    ▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    ░░░░░░  ")
    print("                                    ░░░░      ░░░░░░  ▒▒▒▒░░░░░░░░░░░░░░░░▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░  ░░░░░░  ")
    print("                                    ░░░░░░      ░░░░  ░░▒▒░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░    ░░░░  ")
    print("                                      ░░░░      ░░░░░░░░  ▒▒░░░░░░  ░░░░▒▒▒▒▒▒▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░      ░░  ")
    print("                                        ░░░░    ░░░░  ░░  ░░░░░░░░  ░░░░▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░  ")
    print("                                          ░░░░  ░░░░░░░░    ░░░░░░  ░░▒▒        ▒▒▒▒▒▒▒▒▒▒▓▓░░░░░░░░░░░░░░  ░░  ")
    print("                                            ░░░░░░░░▒▒      ░░░░░░░░░░░░              ▒▒▒▒▒▒░░░░  ▒▒▓▓▒▒░░  ░░  ")

if __name__ == "__main__":
    main()
