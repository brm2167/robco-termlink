import curses
import random

def update_screen(stdscr: curses.window, attempts: int, hex_codes: list[str]):
    stdscr.clear()
    stdscr.addstr(0, 0, "ROBCO INDUSTRIES (TM) TERMLINK PROTOCOL", curses.color_pair(1))
    stdscr.addstr(1, 0, "ENTER PASSWORD NOW", curses.color_pair(1))

    stdscr.addstr(3, 0, f"{attempts} ATTEMPT(S) LEFT:{' ■' * attempts}", curses.color_pair(1))

    for i in range(len(hex_codes)):
        y_pos = 5 + (i % 17)
        x_pos = 21 * (i // 17)
        print(y_pos, x_pos)
        stdscr.addstr(y_pos, x_pos, hex_codes[i], curses.color_pair(1))

    stdscr.refresh()

def main(stdscr: curses.window):
    words_list: dict[int, list[str]] = {}
    with open("wordlist.txt") as words_file:
        for word in next(words_file).split():
            length: int = len(word)
            if length < 3 or length > 12:
                continue

            if length not in words_list:
                words_list[length] = []
            words_list[length].append(word)

    attempts: int = 4

    words_used: list[str] = []
    word_options = words_list[
        list(words_list.keys())[
            random.randrange(0, len(words_list.keys()))
        ]
    ].copy()

    max_words: int = len(word_options)
    if max_words > 16:
        max_words = 16
    
    for i in range(random.randint(4, max_words)):
        words_used.append(
            word_options.pop(random.randrange(0, len(word_options)))
        )

    hex_codes: list[str] = []
    initial_hex = random.randint(61440, 63359)
    for i in range(34):
        hex_codes.append(hex(initial_hex).upper())
        initial_hex += random.randrange(0, 64)

    stdscr.keypad(True)
    
    curses.curs_set(0)
    curses.start_color()

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)

    update_screen(stdscr, attempts, hex_codes)
    while True:
        key = stdscr.getch()

        if key == ord('q'):
            break
        elif key == curses.KEY_MOUSE:
            _, x, y, _, button = curses.getmouse()
            top = f"Mouse clicked at {x}, {y} with button {button}"
        else:
            stdscr.addstr(1, 0, f"Key pressed: {chr(key) if key < 256 else key}")
        update_screen()

curses.wrapper(main)