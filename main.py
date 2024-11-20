import curses

def main(stdscr: curses.window):
    stdscr.keypad(True)
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)

    top: str = "Press 'q' to quit"
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, top)
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