# unclosedTagFinder

[![GitHub license](https://img.shields.io/badge/license-MPLv2-blue.svg)](https://raw.githubusercontent.com/ryanpcmcquen/unclosedTagFinder/master/LICENSE)
[![GitHub version](https://img.shields.io/badge/version-1.0.2-orange.svg)](https://github.com/ryanpcmcquen/unclosedTagFinder/releases)
[![GitHub issues](https://img.shields.io/github/issues/ryanpcmcquen/unclosedTagFinder.svg)](https://github.com/ryanpcmcquen/unclosedTagFinder/issues)
[![Twitter](https://img.shields.io/twitter/url/https/github.com/ryanpcmcquen/unclosedTagFinder.svg?style=social)](https://twitter.com/intent/tweet?text=Hey%2C%20check%20this%20out%3A%20https%3A%2F%2Fgithub.com%2Fryanpcmcquen%2FunclosedTagFinder&url=%5Bobject%20Object%5D)

Find unclosed tags in HTML source.

### Usage:

```
$ ./unclosedTagFinder.py -i '<html></html>'

Your HTML is perfectly matched. You're awesome!

$ ./unclosedTagFinder.py -f good_foo.html

Your HTML is perfectly matched. You're awesome!

$ ./unclosedTagFinder.py -f bad_foo.html

The following tags are unclosed:

{7: '    <span class="bar">Foo'}

$ ./unclosedTagFinder.py -f https://whatwg.org

Your HTML is perfectly matched. You're awesome!
```

---

Thanks to the Wingware Pro IDE for making Python development even more fun!

![Wingware!](https://wingware.com/images/wingware-button-200x89.png)
