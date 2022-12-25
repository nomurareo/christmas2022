import time
import functools


from curses import wrapper

from decorate import snow


def main(stdscr, text, delay, effects=None):
    frame = 0
    max_frame = 300

    if not effects:
        effects = []

    while frame < max_frame:
        display = functools.reduce(lambda text, effect: effect(text), effects, text)
        stdscr.clear()
        stdscr.addstr(display)
        stdscr.refresh()
        time.sleep(delay)
        frame += 1


if __name__ == '__main__':
    with open('christmas-2022\\ascii_templates\\christmas_card.txt', 'rt') as file:
        christmas_card = file.read()
        snow_effect = snow(ratio=.8)
        # christmas_card_with_snow = snow_effect(christmas_card)

    wrapper(main, christmas_card, .3, effects=(snow_effect,))
