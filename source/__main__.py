#!/usr/bin/env python3

import asyncio
import subprocess as sp
from pathlib import Path
from gpiozero import Button
from signal import pause

but = Button(2, hold_time=1)

MAINPATH = '.'
COMMAND = 'ps aux'
PROGRAM = '__main__.py'

mainpath = Path(MAINPATH).resolve()

def toggle():
	print("BRAVO, 1 SECONDO")
	pid = get_pid(PROGRAM)

	if pid:
		kill_proc(pid)
	else:
		run_proc(PROGRAM)


def get_pid(program):
	b_response = sp.check_output(COMMAND.split(' '))
	s_response = b_response.decode()
	response_list = s_response.split('\n')
	
	for row in response_list:
		if program in row:
			splitted = row.split(' ')
			splitted = list(filter(lambda x: x != '', splitted))
			return int(splitted[1])
	
	return None

	
async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')
    
def kill_proc(pid):
	asyncio.run(run(f'kill -9 {pid}'))
		
def run_proc(program):
	asyncio.run(run(f'{mainpath}/{program} > /dev/null 2>&1 &'))
		

but.when_held = toggle
pause()