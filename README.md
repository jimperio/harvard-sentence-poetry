# harvard-sentence-poetry

Generate poem-like text from Harvard sentences ([wiki](https://www.google.com)).

## Sample usage:
```
$ python composer.py -h
usage: composer.py [-h] [-s NUM_STROPHES] [-l NUM_LINES] [--refrain]

Generate poem-like text.

optional arguments:
  -h, --help            show this help message and exit
  -s NUM_STROPHES, --num-strophes NUM_STROPHES
                        Number of strophes (stanzas) to generate. (Default: 2
                        to 4)
  -l NUM_LINES, --num-lines NUM_LINES
                        Number of lines per strophe. (Default: 2 to 4, varying
                        per strophe)
  --refrain             Use a refrain. (Default: no refrain)
$ python composer.py --num-strophes 3 --num-lines 4 --refrain | cowsay
 _________________________________________
/ Hemp is a weed found in parts of the    \
| tropics. He lay prone and hardly moved  |
| a limb. The pencils have all been used. |
| There are many ways to do these things. |
|                                         |
| The hogs were fed chopped corn and      |
| garbage. Pour the stew from the pot     |
| into the plate. Watch the log float in  |
| the wide river. There are many ways to  |
| do these things.                        |
|                                         |
| Pitch the straw through the door of the |
| stable. Shape the clay gently into      |
| block form. Pages bound in cloth make a |
| book. There are many ways to do these   |
\ things.                                 /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

## Notes:
  * Sentences were retrieved from http://www.cs.columbia.edu/~hgs/audio/harvard.html.
