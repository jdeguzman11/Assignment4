# Justin DeGuzman
# justicd1@uci.edu
# 72329664

#  a4.py

"""Entry point for the Assignment 4 DSU Application."""

from ui import UI


def main() -> None:
    """Starts the DSU Interface."""

    print("Welcome to Distributed Social Platform with API Transclusion")
    print("Type 'admin' to enter admin mode, or press enter to continue.")

    try:
        first = input("> ").strip()
    except EOFError:
        return

    ui = UI()

    if first.lower() == "admin":
        ui.run_admin()
    else:
        ui.run_friendly(first)


if __name__ == "__main__":
    main()
