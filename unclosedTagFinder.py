#!/usr/bin/env python3
import re
import argparse
import urllib.parse
import urllib.request

htmlRegex = '<[^\!][^>]*>'
# Void elements:
# https://www.w3.org/TR/html/syntax.html#void-elements
voidElementsRegex = '''
</?(?!area|base|br|col|embed|hr|img|input|keygen|link|menuitem|meta|param|source|track|wbr)'
'''
openingTagRegex = '<[^/]'
closingTagRegex = '</'

parser = argparse.ArgumentParser(
    description='Check HTML source for unclosed tags.'
)
parser.add_argument(
    '-f',
    '--file',
    help='HTML file to parse (remote or local).'
)
parser.add_argument(
    '-i',
    '--input',
    help='HTML text to parse (a quote-delimited string).'
)
args = parser.parse_args()
if args.file:
    urlCheck = urllib.parse.urlparse(args.file)
    if urlCheck.scheme or urlCheck.netloc:
        htmlFile = urllib.request.urlopen(args.file)
    else:
        htmlFile = open(args.file)
    # Technically, we only need
    # conversion to a string for
    # remote files, but it doesn't
    # hurt to do it for both.
    html = str(htmlFile.read())
    htmlFile.close()
else:
    html = args.input
tags = re.compile(htmlRegex, flags=re.I | re.M)
tagList = re.findall(tags, html)

devoidedTagList = list(
    filter(
        lambda tag: re.match(
            voidElementsRegex,
            tag
        ),
        tagList
    )
)

openingTagList = list(
    filter(
        lambda tag: re.match(openingTagRegex, tag),
        devoidedTagList
    )
)
closingTagList = list(
    filter(
        lambda tag: re.match(closingTagRegex, tag),
        devoidedTagList
    )
)

numberOfOpeningTags = len(openingTagList)
numberOfClosingTags = len(closingTagList)

filteredClosingTagList = list(
    map(lambda tag: re.sub('/', '', tag), closingTagList)
)

if numberOfOpeningTags == numberOfClosingTags:
    print()
    print("Your HTML is perfectly matched. You're \033[1;32mawesome\033[1;m!")
    print()
else:
    print()
    print('The following tags are \033[1;41munclosed\033[1;m:')
    print()
    print(set(openingTagList).difference(filteredClosingTagList))
    print()
