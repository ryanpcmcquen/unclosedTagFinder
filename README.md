# unclosedTagFinder
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)]()
[![GitHub release](https://img.shields.io/github/release/qubyte/rubidium.svg)]()
[![GitHub issues](https://img.shields.io/github/issues/badges/shields.svg)]()
Find unclosed tags in HTML source.

Usage:
```py
$ ./unclosedTagFinder.py -f foo.html 
The following elements are unclosed:
{'<span class="bar">'}
```

---

TODO:

- [x] Read file input.
- [x] Accomodate tag names with attributes.
- [ ] Read remote files.
- [ ] Accomodate multiple files.
- [ ] Accomodate user input.
- [ ] Add a GUI.
- [ ] Improve command line commands and output.
- [ ] Give line numbers of unclosed tags.
- [ ] Fix code?
- [ ] Include unit tests.

---

Thanks to the Wingware Pro IDE for making Python development even more fun!

![Wingware!](https://wingware.com/images/wingware-button-200x89.png)