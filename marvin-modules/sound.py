from os import system as terminal
from platform import system as ostype

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

OS = ostype()

def mute_system_audio():
	if OS == 'Darwin':
		os_command = 'osascript -e \'set volume output muted true\''
	elif OS == 'Linux':
		os_command = 'amixer set Master mute'
	else:
		print('No support for your Operating System. (No Windows yet)')

def unmute_system_audio():
	if OS == 'Darwin':
		os_command = 'osascript -e \'set volume output muted false\''
	elif OS == 'Linux':
		os_command = 'amixer set Master unmute'
	else:
		print('No support for your Operating System. (No Windows yet)')