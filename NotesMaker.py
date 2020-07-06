# coding: utf-8
import sys
import json
import csv
import time
import os
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN


print("\n-----------------------------------------------")
print(" \033[1m\033[34mNotes Maker\033[0m (built: June 28 2020) ( MIT )\n")
print(" github: \033[4mhttps://github.com/smpny7/notes-maker\033[0m")
print("-----------------------------------------------\n")

sys.stdout.write('> Checking for input...\n')
time.sleep(0.3)
if sys.stdin.isatty():
    sys.stdout.write('\033[1A> Checking for input... ' + u'\u274c' + '\n')
    sys.stderr.write(
        '\n> \033[1m\033[31mError\033[0m: Please input STDIN via Redirect or Pipe.\n\n')
    sys.stderr.write(
        '> Exit(1)\033[0m\n\n\n')
    sys.exit()
else:
    sys.stdout.write('\033[1A> Checking for input... ' + u'\u2705' + '\n')

try:
    sys.stdout.write('> Checking whether this is a JSON file...\n')
    time.sleep(0.3)
    dec = json.loads(sys.stdin.read())
    sys.stdout.write(
        '\033[1A> Checking whether this is a JSON file... ' + u'\u2705' + '\n')
except:
    sys.stdout.write(
        '\033[1A> Checking whether this is a JSON file... ' + u'\u274c' + '\n')
    sys.stderr.write(
        '\n> \033[1m\033[31mError\033[0m: This file is not JSON.\n\n')
    sys.stderr.write(
        '> Exit(1)\033[0m\n\n\n')
    sys.exit()

try:
    sys.stdout.write('> Converting JSON to CSV file...\n')
    time.sleep(0.3)
    output = []
    bpm = dec['BPM']
    offset = dec['offset']
    for data in dec['notes']:
        arr = [0]*2
        arr[0] = 60.0 * data['num'] / (bpm * data['LPB']) + offset / 10000
        arr[1] = data['block']
        output.append(arr)
    sys.stdout.write(
        '\033[1A> Converting JSON to CSV file... ' + u'\u2705' + '\n')
except:
    sys.stdout.write(
        '\033[1A> Converting JSON to CSV file... ' + u'\u274c' + '\n')
    sys.stderr.write(
        '\n> \033[1m\033[31mError\033[0m: This file is not generated by Notes Editor.\n')
    sys.stderr.write(
        '> \033[1m\033[33mMore details\033[0m: \033[4mhttps://github.com/setchi/NoteEditor/\033[0m\n\n')
    sys.stderr.write(
        '> Exit(1)\033[0m\n\n\n')
    sys.exit()

try:
    sys.stdout.write('> Exporting CSV file...\n')
    time.sleep(0.3)
    with open(dec['name'] + '.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(output)
    sys.stdout.write(
        '\033[1A> Exporting CSV file... ' + u'\u2705' + '\n')
except:
    sys.stdout.write(
        '\033[1A> Exporting CSV file... ' + u'\u274c' + '\n')
    sys.stderr.write(
        '\n> \033[1m\033[31mError\033[0m: Could not export CSV file.\n')
    sys.stderr.write(
        '> \033[1m\033[33mHints\033[0m: Check Permission.\n\n')
    sys.stderr.write(
        '> Exit(1)\033[0m\n\n\n')
    sys.exit()

sys.stdout.write(
    '\n> \033[1m\033[32mSuccess\033[0m: Output to the following location.\n')
sys.stdout.write('> ' + os.path.dirname(os.path.abspath(__file__)) + '/' + dec['name'] + '.csv\n\n\n')