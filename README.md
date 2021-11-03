## About
This is a simple Pomodoro timer for Tmux.

## Requirements
To use this project you need a Linux OS. You need sox package installed to be
able to get a sound notification at the end of each session.
##### Ubuntu:
```
sudo apt install sox
```

## Install
```
git clone https://github.com/DNonov/pomodoro-tmux
./install.sh
```

## Description
This project consists of a daemon process running an HTTP server and a client
(Tmux). Tmux is running curl against the server every second and the response is
printed on the Tmux's status line. The control over the server and the daemon
process is implemented via some Tmux settings.

```bash
# Settings needed to operate with tmux-pomodoro
set -g status-interval 1
set -g status-right '#(curl localhost:9876/status)'
bind w run-shell 'curl localhost:9876/start-work > /dev/null'
bind s run-shell 'curl localhost:9876/start-rest > /dev/null'
bind u run-shell 'python3 ~/.pomodoro-tmux/server.py start'
bind m run-shell 'python3 ~/.pomodoro-tmux/server.py stop'
bind y run-shell 'python3 ~/.pomodoro-tmux/server.py restart'
```
### Contributing
Bug reports and pull requests are always welcome.

### License
[MIT](./LICENSE.md)
