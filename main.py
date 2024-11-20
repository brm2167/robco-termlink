import curses


def main(stdscr: curses.window):
    stdscr.keypad(True)
    
    curses.curs_set(0)
    curses.start_color()

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)

    attempts: int = 4

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "ROBCO INDUSTRIES (TM) TERMLINK PROTOCOL", curses.color_pair(1))
        stdscr.addstr(1, 0, "ENTER PASSWORD NOW", curses.color_pair(1))

        stdscr.addstr(3, 0, f"{attempts} ATTEMPT(S) LEFT:{' ■' * attempts}", curses.color_pair(1))

        key = stdscr.getch()

        if key == ord('q'):
            break
        elif key == curses.KEY_MOUSE:
            _, x, y, _, button = curses.getmouse()
            top = f"Mouse clicked at {x}, {y} with button {button}"
        else:
            stdscr.addstr(1, 0, f"Key pressed: {chr(key) if key < 256 else key}")

        stdscr.refresh()

curses.wrapper(main)