#!/bin/bash
gcalcli agenda "`date`" --calendar="Особисті завдання" --calendar="Нагадування" --calendar="United Everything Systerm" --military --nostarted | head -2 | tail -1 | cut -d' ' -f4- > agenda.txt
