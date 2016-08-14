#!/usr/bin/python
from libqtile.command import Client
c = Client()
agenda = open('agenda.txt','r').read().rstrip('\n')
print agenda
c.widget['textbox'].update(text=agenda)
