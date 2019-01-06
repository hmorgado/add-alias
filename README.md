# Add Alias
This script add aliases to your `~/.bashrc` file like this:
```
$ dist/addalias gs 'git status'
Added new alias: alias gs='git status'
```
You can either run it as a script or compile it into a _one-file_.

### Run it:
```
$ python3.5 addalias.py gs 'git status'
Added new alias: alias gs='git status'
```

### Compile:
```
$ virtualenv --python=$(which python3.5) .env
$ . .env/bin/activate
$ pip install -r requirements.txt
$ .env/bin/pyinstaller --onefile addalias.py
$ dist/addalias gs 'git status'
Added new alias: alias gs='git status'
```
