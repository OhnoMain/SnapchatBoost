#!/usr/bin/env python3
# SnapchatBoost - main.py (anonymous mode)
import os, sys, time, json, platform, webbrowser
from pathlib import Path
from colorama import Fore, Style, init
init(autoreset=True)

try:
    import pyautogui, keyboard
except Exception:
    pyautogui = None
    keyboard = None

DEFAULT_SETTINGS = {
    "loop_delay": 0.2,
    "click_delay": 0.29,
    "position_delay": 0.5,
    "shortcut_count": 1,
    "positions": {},
    "auto_open_readme": True,
    "readme_url": "https://github.com/OhnoMain/SnapchatBoost/blob/main/readme.md",
    "snapchat_login": "https://web.snapchat.com/"
}

BASE_DIR = Path(__file__).parent.resolve()
SETTINGS_PATH = BASE_DIR / "settings.json"
SNAP_IMAGE = BASE_DIR / "snapscore_100k.png"

SNAP_Y = Fore.YELLOW
SNAP_ACC = Fore.LIGHTYELLOW_EX
SNAP_W = Fore.WHITE

def clear():
    os.system("cls" if platform.system() == "Windows" else "clear")

def title(msg):
    if sys.platform.startswith("win"):
        try:
            import ctypes
            ctypes.windll.kernel32.SetConsoleTitleW(msg)
        except:
            pass
    else:
        sys.stdout.write(f"\33]0;{msg}\a")
        sys.stdout.flush()

def pretty_print(text, color=SNAP_Y, delay=0.005):
    for ch in str(text):
        sys.stdout.write(color + ch + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(delay)
    print("")

def load_settings():
    if SETTINGS_PATH.exists():
        try:
            with open(SETTINGS_PATH, "r") as fh:
                return json.load(fh)
        except:
            return DEFAULT_SETTINGS.copy()
    return DEFAULT_SETTINGS.copy()

def save_settings(data):
    try:
        with open(SETTINGS_PATH, "w") as fh:
            json.dump(data, fh, indent=2)
        return True
    except:
        return False

BANNER_LINES = [
    "███████╗███╗   ██╗ █████╗ ██████╗ ██████╗  ██████╗  ██████╗ ███████╗████████╗",
    "██╔════╝████╗  ██║██╔══██╗██╔══██╗██╔══██╗██╔═══██╗██╔═══██╗██╔════╝╚══██╔══╝",
    "███████╗██╔██╗ ██║███████║██████╔╝██████╔╝██║   ██║██║   ██║███████╗   ██║   ",
    "╚════██║██║╚██╗██║██╔══██║██╔═══╝ ██╔══██╗██║   ██║██║   ██║╚════██║   ██║   ",
    "███████║██║ ╚████║██║  ██║██║     ██████╔╝╚██████╔╝╚██████╔╝███████║   ██║   ",
    "╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   "
]

def print_banner():
    print(SNAP_Y + "          " + "👻")
    for i, line in enumerate(BANNER_LINES):
        cols = [SNAP_Y, SNAP_ACC, SNAP_W]
        print(cols[i % len(cols)] + line + Style.RESET_ALL)
    print(SNAP_ACC + "                             by Ohno (anonymous mode)" + Style.RESET_ALL)
    print("")

def boot_sequence():
    clear()
    print(SNAP_Y + "\n          " + "👻" + "\n")
    steps = ["Powering up subsystems...", "Calibrating camera input...", "Verifying UI...", "Loading engine...", "Finalizing..."]
    for s in steps:
        pretty_print(s, SNAP_ACC, delay=0.004)
        for _ in range(5):
            sys.stdout.write(SNAP_Y + "." + Style.RESET_ALL)
            sys.stdout.flush()
            time.sleep(0.06)
        print("")
    pretty_print("Boot complete ✔", SNAP_Y, delay=0.002)
    time.sleep(0.4)
    clear()

class SnapBot:
    def __init__(self, settings):
        self.settings = settings
        self.sent_snaps = 0
        self.first_try = True

    def get_positions(self):
        if pyautogui is None or keyboard is None:
            pretty_print("pyautogui/keyboard missing; cannot capture positions.", SNAP_W)
            return
        pretty_print("Move mouse to Camera button, press Y", SNAP_W)
        while not keyboard.is_pressed("y"):
            time.sleep(0.05)
        self.settings['positions']['switch_to_camera'] = pyautogui.position()
        time.sleep(self.settings.get('position_delay', 0.5))

        pretty_print("Move to Send To, press Y", SNAP_W)
        while not keyboard.is_pressed("y"):
            time.sleep(0.05)
        self.settings['positions']['send_to'] = pyautogui.position()
        time.sleep(self.settings.get('position_delay', 0.5))

        pretty_print("Move to Shortcut, press Y", SNAP_W)
        while not keyboard.is_pressed("y"):
            time.sleep(0.05)
        self.settings['positions']['shortcut'] = pyautogui.position()
        time.sleep(self.settings.get('position_delay', 0.5))

        pretty_print("Move to Select All, press Y", SNAP_W)
        while not keyboard.is_pressed("y"):
            time.sleep(0.05)
        self.settings['positions']['select_all'] = pyautogui.position()
        time.sleep(self.settings.get('position_delay', 0.5))

    def estimate_time(self, snaps_target):
        loop = float(self.settings.get('loop_delay', 0.2))
        clicks = 6
        click_delay = float(self.settings.get('click_delay', 0.29))
        per_snap = (clicks * click_delay) + loop
        return per_snap * snaps_target

    def send_snap(self, started_time, shortcut_user_count):
        pos = self.settings.get('positions', {})
        if pyautogui is None:
            pretty_print("pyautogui not installed; cannot send.", SNAP_W)
            return
        required = ['switch_to_camera', 'send_to', 'shortcut', 'select_all']
        if not all(k in pos for k in required):
            pretty_print("Positions missing. Configure first.", SNAP_W)
            return

        pyautogui.moveTo(pos['switch_to_camera'])
        if self.first_try:
            pyautogui.click()
            self.first_try = False
        time.sleep(self.settings.get('click_delay', 0.29))
        pyautogui.click()
        time.sleep(self.settings.get('click_delay', 0.29))

        pyautogui.moveTo(pos['send_to'])
        pyautogui.click()
        time.sleep(self.settings.get('click_delay', 0.29))

        pyautogui.moveTo(pos['shortcut'])
        pyautogui.click()
        time.sleep(self.settings.get('click_delay', 0.29))

        pyautogui.moveTo(pos['select_all'])
        pyautogui.click()
        time.sleep(self.settings.get('click_delay', 0.29))

        pyautogui.moveTo(pos['send_to'])
        pyautogui.click()

        self.sent_snaps += 1
        now = time.time()
        pretty_print(f"Sent batch #{self.sent_snaps} ({self.sent_snaps * shortcut_user_count} snaps). Elapsed {int(now - started_time)}s")


def open_help_pages(settings):
    try:
        webbrowser.open(settings.get('readme_url'))
        webbrowser.open(settings.get('snapchat_login'))
    except:
        pass

def ensure_snap_image():
    if not SNAP_IMAGE.exists():
        pretty_print(f"snapscore image missing: {SNAP_IMAGE}", SNAP_W)

def settings_menu(settings):
    clear()
    print_banner()
    pretty_print("Settings (blank keeps current)", SNAP_W)
    try:
        ld = input(f"Loop delay [{settings.get('loop_delay')}]: ").strip()
        if ld:
            settings['loop_delay'] = float(ld)

        cd = input(f"Click delay [{settings.get('click_delay')}]: ").strip()
        if cd:
            settings['click_delay'] = float(cd)

        sc = input(f"Shortcut size [{settings.get('shortcut_count')}]: ").strip()
        if sc:
            settings['shortcut_count'] = int(sc)
    except:
        pretty_print("Invalid input; keeping previous.", SNAP_W)
    save_settings(settings)
    pretty_print("Saved.", SNAP_ACC)
    input("ENTER")

def configure_positions(settings):
    bot = SnapBot(settings)
    bot.get_positions()
    save_settings(settings)
    pretty_print('Saved positions.', SNAP_ACC)
    input('ENTER')

def import_positions(settings):
    path = input("Enter full path to settings.json (or blank): ").strip()
    if not path:
        return
    p = Path(path)
    if not p.exists():
        pretty_print('File not found.', SNAP_W)
        return
    with open(p, 'r') as fh:
        data = json.load(fh)
    if 'positions' in data:
        settings['positions'] = data['positions']
        save_settings(settings)
        pretty_print('Imported.', SNAP_ACC)
    else:
        pretty_print('No positions found', SNAP_W)

def help_menu(settings):
    clear()
    print_banner()
    pretty_print('Help & Instructions', SNAP_Y)
    pretty_print('Auto-opening README and Snapchat Web in your browser...', SNAP_W)
    open_help_pages(settings)
    input('ENTER to return')

def estimate_menu(settings):
    clear()
    print_banner()
    pretty_print('Estimate time for N snaps', SNAP_W)
    try:
        n = int(input('How many snaps? '))
    except:
        pretty_print('Invalid number', SNAP_W)
        input('ENTER')
        return
    bot = SnapBot(settings)
    secs = bot.estimate_time(n)
    pretty_print(f'Estimate: {int(secs)}s', SNAP_ACC)
    input('ENTER')

def exit_screen():
    clear()
    box = (
        "╔════════════════════════════════════════════════╗\n"
        "║   💛 Thank you for using SnapchatBoost!         ║\n"
        f"║   https://github.com/OhnoMain/SnapchatBoost    ║\n"
        "╚════════════════════════════════════════════════╝\n"
    )
    print(SNAP_Y + box + Style.RESET_ALL)

def main():
    title('SnapchatBoost')
    settings = load_settings()
    boot_sequence()
    ensure_snap_image()
    while True:
        clear()
        print_banner()
        pretty_print('1) Start', SNAP_Y)
        pretty_print('2) Settings', SNAP_W)
        pretty_print('3) Configure Positions', SNAP_W)
        pretty_print('4) Import Positions', SNAP_W)
        pretty_print('5) Estimate', SNAP_W)
        pretty_print('6) Help', SNAP_W)
        pretty_print('7) Exit', SNAP_ACC)
        c = input('> ').strip()
        if c == '1':
            bot = SnapBot(settings)
            pretty_print('Starting. ESC to stop.', SNAP_Y)
            started = time.time()
            while True:
                try:
                    if keyboard and keyboard.is_pressed('esc'):
                        pretty_print('Stopping', SNAP_ACC)
                        break
                except:
                    pass
                bot.send_snap(started, settings.get('shortcut_count', 1))
                time.sleep(settings.get('loop_delay', 0.2))
            save_settings(settings)
        elif c == '2':
            settings_menu(settings)
        elif c == '3':
            configure_positions(settings)
        elif c == '4':
            import_positions(settings)
        elif c == '5':
            estimate_menu(settings)
        elif c == '6':
            help_menu(settings)
        elif c == '7':
            save_settings(settings)
            exit_screen()
            break
        else:
            continue

if __name__ == '__main__':
    main()
