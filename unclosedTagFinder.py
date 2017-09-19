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
args = parser.parse_args()

htmlFile = open(args.filename)
html = htmlFile.read()
tags = re.compile('<[^\!][^>]*>', flags=re.I | re.M)
tagList = re.findall(tags, str(html))
htmlFile.close()
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
    map(lambda str: re.sub('/', '', str), closingTagList)
)

if numberOfOpeningTags == numberOfClosingTags:
    print('Your HTML is perfectly matched.')
else:
    print('The following elements are unclosed:')
    print(set(openingTagList).difference(filteredClosingTagList))
