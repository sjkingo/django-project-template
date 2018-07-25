#!/usr/bin/env python3

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    import sys
    execute_from_command_line(sys.argv)
