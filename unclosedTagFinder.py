#!/usr/bin/env python3
import re
import argparse


parser = argparse.ArgumentParser(
    description='Check HTML source for unclosed tags.'
)
parser.add_argument(
    '-f',
    '--filename',
    help='HTML file to parse.'
)
parser.add_argument(
    '-i',
    '--input',
    help='HTML text to parse (a quote-delimited string).'
)
args = parser.parse_args()
if args.filename:
    htmlFile = open(args.filename)
    html = htmlFile.read()
    htmlFile.close()
else:
    html = args.input
tags = re.compile('<[^\!][^>]*>', flags=re.I | re.M)
tagList = re.findall(tags, html)

'''
Filter out void elements:
https://www.w3.org/TR/html/syntax.html#void-elements
area, base, br, col, embed, hr, img, input, keygen, link, menuitem, meta, param, source, track, wbr
'''

openingTagList = list(
    filter(
        lambda tag: re.match('<[^/]', tag),
        tagList
    )
)
closingTagList = list(
    filter(
        lambda tag: re.match('</', tag),
        tagList
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
