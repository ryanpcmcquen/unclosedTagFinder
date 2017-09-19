# unclosedTagFinder
[![GitHub license](https://img.shields.io/badge/license-GPLv2-blue.svg)](https://raw.githubusercontent.com/ryanpcmcquen/unclosedTagFinder/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/ryanpcmcquen/unclosedTagFinder.svg)](https://github.com/ryanpcmcquen/unclosedTagFinder/issues)
[![Twitter](https://img.shields.io/twitter/url/https/github.com/ryanpcmcquen/unclosedTagFinder.svg?style=social)](https://twitter.com/intent/tweet?text=Wow%2C%20this%20is%20neat%3A%20https%3A%2F%2Fgithub.com%2Fryanpcmcquen%2FunclosedTagFinder&url=%5Bobject%20Object%5D)

Find unclosed tags in HTML source.

Usage:
```
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
