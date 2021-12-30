## About
This is a simple Pomodoro timer for Tmux.

## Requirements
To use this project you need a Linux OS. You need a sox package installed to be
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
# Add this in your tmux.conf

# Settings needed to operate with tmux-pomodoro
set -g status-interval 1
set -g status-right '#(curl localhost:9876/status)'
bind w run-shell 'curl localhost:9876/start-work > /dev/null'
bind s run-shell 'curl localhost:9876/start-rest > /dev/null'
bind u run-shell 'python3 ~/.pomodoro-tmux/server.py start'
bind m run-shell 'python3 ~/.pomodoro-tmux/server.py stop'
bind y run-shell 'python3 ~/.pomodoro-tmux/server.py restart'
```

A bit more detailed overview of the settings.

* `set -g status-interval 1` The frequency of your status line redraws in sec.
* `set -g status-right '#(curl localhost:9876/status)'` Content that will be
  drawn on the right section of your status line. Bear in mind that if you have
  set something already. This will overwrite it. If this is the case you should
  add `#(curl localhost:9876/status)` to the existing `status-right` setting.

``` bash
# Let's say this is your existing `status-right` setting in `tmux.conf`.
status-right '#{=22:pane_title} %H:%M %d-%b-%y'
# Just add `#(curl localhost:9876/status)` in the beginning of the setting.
status-right '#(curl localhost:9876/status) #{=22:pane_title} %H:%M %d-%b-%y'
```

With `bind <any key> run-shell` you bind a key to run a given shell script.

* `curl localhost:9876/start-work > /dev/null` Starts a Pomodoro work session.
* `curl localhost:9876/start-rest > /dev/null` Starts a Pomodoro rest session.
* `python3 ~/.pomodoro-tmux/server.py start` Starts the server and daemonizes
  the process.
* `python3 ~/.pomodoro-tmux/server.py start` Stops the server and kills the
  daemon process.
* `python3 ~/.pomodoro-tmux/server.py restart` Restarts the process.



### Contributing
Bug reports and pull requests are always welcome.

### License
[MIT](./LICENSE.md)
