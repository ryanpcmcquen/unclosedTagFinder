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
    help='HTML text to parse (passed as a quote-delimited string).'
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
    print('''
        Your HTML is perfectly matched. You're awesome!
    ''')
else:
    print('The following elements are unclosed:')
    print(set(openingTagList).difference(filteredClosingTagList))
