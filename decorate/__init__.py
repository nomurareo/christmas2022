__author__ = 'nomurareo'

from random import Random

default_snowflakes = (
    '*',  # snowflake
    '.',  # small snow
    'o',  # middle snow
    '\u2666',  # diamond
    '\u2744'  # snowflake
)


def _text_to_lines(text):
    line = ''
    count = -1

    for char in text:
        if char == '\n':
            yield line
            line = ''
            continue
        line += char


def snow(ratio=.7, *, snow_flakes=default_snowflakes, min_snowflakes=0, max_snowflakes=6, replace_only_whitespace=True):
    _random = Random()

    def apply_snow(text):
        snow_text = list(text)
        start_index = 0
        end_index = len(text) - 1
        skip = False

        for last_index, char in enumerate(text, start=0):
            if skip:
                continue

            not_blank_line = cap_snowflakes = last_index - start_index
            if char == '\n' or last_index == end_index and not_blank_line:
                for _ in range(_random.randrange(min_snowflakes, cap_snowflakes if max_snowflakes > cap_snowflakes else max_snowflakes)):
                    snow_text[_random.randrange(start_index, last_index+1)] = snow_flakes[_random.randrange(0, len(snow_flakes))]
                start_index = last_index

        return ''.join(snow_text)

    return apply_snow
