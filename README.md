# unclosedTagFinder
Find unclosed tags in HTML source.

Usage:
```py
$ ./unclosedTagFinder.py -f foo.html 
The following elements are unclosed:
{'<span class="bar">'}
```

TODO:
[X] Read file input.
[X] Accomodate tag names with attributes.
[ ] Read remote files.
[ ] Accomodate multiple files.
[ ] Accomodate user input.
[ ] Add a GUI.
[ ] Improve command line commands and output.
[ ] Give line numbers of unclosed tags.
[ ] Fix code?