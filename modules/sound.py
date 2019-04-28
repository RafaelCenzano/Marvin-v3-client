from os import system as terminal
from platform import system as platform

## NOTES ##
# Sounds, Terminal Control
# LINUX change percentage 0% - 100%
# amixer sset 'Master' 50%
# mute
# amixer set Master mute
# unmute
# amixer set Master unmute
# increase
# amixer -D pulse sset Master 1%+
# decrease
# amixer -D pulse sset Master 1%-
# MAC
# set volume 0-100
# osascript -e 'set volume output volume 50'
# mute
# osascript -e 'set volume output muted true'
# unmute
# osascript -e 'set volume output muted false'
# increase
# osascript -e "set volume output volume (output volume of (get volume settings) + 1) --100%"
# decrease
# osascript -e "set volume output volume (output volume of (get volume settings) - 1) --100%"
# WINDOWS
# NONE

OS = platform()

def mute_system_audio():
	if OS == 'Darwin':
		os_command = 'osascript -e \'set volume output muted true\''
	elif OS == 'Linux':
		os_command = 'amixer set Master mute'
	else:
		os_command = None
		print('No support for your Operating System. (No Windows yet)')

	if os_command != None:
		terminal(os_command)

def unmute_system_audio():
	if OS == 'Darwin':
		os_command = 'osascript -e \'set volume output muted false\''
	elif OS == 'Linux':
		os_command = 'amixer set Master unmute'
	else:
		os_command = None
		print('No support for your Operating System. (No Windows yet)')

	if os_command != None:
		terminal(os_command)