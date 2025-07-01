#!/bin/bash
# Automatically start EmulationStation on terminal login
if [ "$(tty)" = "/dev/tty1" ]; then
  emulationstation
fi
