#!/bin/bash

# No silent errors
set -e

# Make a dir in user's home dir.
mkdir -p ~/.tmux-pomodoro;

# Copy server.py file into the newly created folder.
cp ./server.py ~/.tmux-pomodoro/server.py;

# Copy rest of the source code as well.
cp -rf ./lib ~/.tmux-pomodoro/lib

# Append all tmux settings to user's tmux.conf
text="# Those are auto generated settings for pomodoro-tmux
set -g status-interval 1
set -g status-right '#(curl localhost:9876/status)'
bind w run-shell 'curl localhost:9876/start-work > /dev/null'
bind s run-shell 'curl localhost:9876/start-rest > /dev/null'
bind u run-shell 'python3 ~/.tmux-pomodoro/server.py start'
bind m run-shell 'python3 ~/.tmux-pomodoro/server.py stop'
bind l run-shell 'python3 ~/.tmux-pomodoro/server.py restart'
"
echo -e "$text" >> ~/tmux.conf
