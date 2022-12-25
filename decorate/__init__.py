__author__ = 'nomurareo'

from random import Random

default_snowflakes = (
    '*',  # snowflake
    '.',  # small snow
    # 'o',  # middle snow
    # '\u2666',  # diamond
    # '\u2744'  # snowflake
)


def snow(ratio=.7, *, snowflakes=default_snowflakes, min_snowflakes=0, max_snowflakes=6, replace_only_whitespace=True):
    _random = Random()

    def apply_snow(text):
        snow_text = list(text)
        start_index = 0
        end_index = len(text) - 1
        skip = False

        for last_index, char in enumerate(text, start=0):
            if skip:
                skip = False
                continue

            not_blank_line = cap_snowflakes = last_index - start_index
            if char == '\n' or last_index == end_index and not_blank_line:
                for _ in range(_random.randrange(min_snowflakes, cap_snowflakes if max_snowflakes > cap_snowflakes else max_snowflakes)):
                    snowflake_index = _random.randrange(start_index, last_index+1)
                    if not replace_only_whitespace or snow_text[snowflake_index] == ' ':
                        snow_text[snowflake_index] = snowflakes[_random.randrange(0, len(snowflakes))]
                start_index = last_index

            skip = _random.random() < 1 - ratio

        return ''.join(snow_text)

    return apply_snow
