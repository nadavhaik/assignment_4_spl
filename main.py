import sys

from context_manager import ContextManager


def main():
    cm = ContextManager(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    cm.run()


if __name__ == "__main__":
    main()
