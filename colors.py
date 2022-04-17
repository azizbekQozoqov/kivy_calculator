from typing import Tuple


def parse_hex(one,two,three, opacity=1) -> Tuple:
    return (one/255, two/255, three/255,opacity)