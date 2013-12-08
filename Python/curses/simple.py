# Simple example of using Python curses
import curses

def main():
    # starting
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbrake()
    stdscr.keypad(True)

    stdscr.refresh()
    stdscr.getkey()
    #ending
    curses.nocbrake()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

if __name__ == '__main__':
    main()
