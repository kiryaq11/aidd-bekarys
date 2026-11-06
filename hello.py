"""Сәлемдесу скрипті: ат сұрап, бүгінгі күнді көрсетеді.

Қосу: python hello.py
Тек стандартты кітапхана қолданылады.
"""

import os
import sys
from datetime import date


def _utf8_console() -> None:
    """Windows-тағы cp1251 консольде Қазақ әріптері дұрыс шығуы үшін."""
    if sys.platform == "win32":
        os.system("chcp 65001 >nul")
    for stream in (sys.stdout, sys.stdin):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def main() -> None:
    _utf8_console()
    name = input("Атыңызды жазыңыз: ").strip()
    if not name:
        name = "досым"
    today = date.today().strftime("%d.%m.%Y")
    print(f"Сәлем, {name}! Бүгін {today}")


if __name__ == "__main__":
    main()
