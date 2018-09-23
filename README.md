# DnD
Tools For Basic DnD

Reference the rules [here][1].

[1]: http://media.wizards.com/2016/downloads/DND/PlayerBasicRulesV03.pdf "Wizards.com Basic Rules"

Currently the only script that should be run from the command line is characterInit.py. Try it out:

```shell
$ git clone https://github.com/jzlandis/DnD.git
$ cd ./DnD/.
$ python characterInit.py
```
If the terminal window isn't big enough the script will crash with this error: `_curses.error: addstr() returned ERR`

On proper startup you should get the following:

```curses
              -_____          -_____
                ' | -,          ' | -,
               /| |  |` \\/\\  /| |  |`
               || |==|| || ||  || |==||
              ~|| |  |, || || ~|| |  |,
               ~-____,  \\ \\  ~-____,
              (               (


  ,- _~. ,,                             ,
 (' /|   ||      _           _         ||
((  ||   ||/\\  < \, ,._-_  < \,  _-_ =||=  _-_  ,._-_
((  ||   || ||  /-||  ||    /-|| ||    ||  || \\  ||
 ( / |   || || (( ||  ||   (( || ||    ||  ||/    ||
  -____- \\ |/  \/\\  \\,   \/\\ \\,/  \\, \\,/   \\,
           _/


       ,- _~.                     ,
      (' /|                 _    ||
     ((  ||   ,._-_  _-_   < \, =||=  /'\\ ,._-_
     ((  ||    ||   || \\  /-||  ||  || ||  ||
      ( / |    ||   ||/   (( ||  ||  || ||  ||
       -____-  \\,  \\,/   \/\\  \\, \\,/   \\,


ASCII art created with PyFiglet
Press Any Button to Continue

```
