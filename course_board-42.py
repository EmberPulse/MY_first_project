# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: CourseBoard
import sys, os

ANSI = {
    "RESET": "\033[0m",
    "BOLD": "\033[1m",
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "BLUE": "\033[34m",
    "MAGENTA": "\033[35m",
    "CYAN": "\033[36m",
    "WHITE": "\033[37m",
    "GRAY": "\033[90m",
}

def _is_terminal():
    return hasattr(sys.stdout, "isatty") and sys.stdout.isatty()

def _is_color_enabled():
    return os.environ.get("NO_COLOR", "").lower() not in ("true", "1") and _is_terminal()

def _colorize(text, code):
    if _is_color_enabled() and code:
        return f"{ANSI[code]}{text}{ANSI['RESET']}"
    return text

def print_header(title):
    print(_colorize(f"{ANSI['BOLD']}{ANSI['CYAN']}╔══════════════════════════╗{ANSI['RESET']}", "CYAN"))
    print(_colorize(f"{ANSI['BOLD']}{ANSI['CYAN']}║ {title} {ANSI['RESET']}", "CYAN"))
    print(_colorize(f"{ANSI['BOLD']}{ANSI['CYAN']}╚══════════════════════════╝{ANSI['RESET']}", "CYAN"))

def print_section(title):
    print(_colorize(f"\n{ANSI['BOLD']}{ANSI['YELLOW']}══ {title} ══{ANSI['RESET']}", "YELLOW"))

def print_status(label, value, color):
    print(_colorize(f"  {label}: {value}", color))

def print_item(name, status, progress, deadline):
    status_color = ANSI["GREEN"] if status else ANSI["RED"]
    print(_colorize(f"  • {name} [{status_color}{status}{ANSI['RESET']}] {progress}% {deadline}", "BOLD"))

def print_summary(courses):
    total = sum(c["progress"] for c in courses)
    avg = total / len(courses) if courses else 0
    print(_colorize(f"\n  Сводка: {total} из {len(courses) * 100}% пройдено, средний прогресс: {avg:.1f}%", "BOLD"))
