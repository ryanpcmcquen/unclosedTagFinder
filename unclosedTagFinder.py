#!/usr/bin/env python3
import re
import argparse
import urllib.parse
import urllib.request

htmlRegex = r'\s*<[^\!][^>]*>'
# Void elements:
# https://www.w3.org/TR/html/syntax.html#void-elements
voidElementsRegex = r'\s*</?(?!area|base|br|col|embed|hr|img|input|keygen|link|menuitem|meta|param|source|track|wbr)'
openingTagRegex = r'\s*<[^/]'
closingTagRegex = r'\s*</'

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
    htmlLines = enumerate(str(htmlFile.read()).splitlines(), 1)
    htmlFile.close()
else:
    htmlLines = enumerate(args.input.splitlines(), 1)

tags = re.compile(htmlRegex, flags=re.IGNORECASE | re.MULTILINE)

tagDict = {
    line_number: line for (
        line_number, line
    ) in htmlLines
    if tags.search(line)
}

devoidedTagDict = {
    line_number: tag for line_number, tag in tagDict.items()
    if re.match(
        voidElementsRegex,
        tag
    )
}

openingTagDict = {
    line_number: tag for line_number, tag in devoidedTagDict.items()
    if re.match(
        openingTagRegex,
        tag
    )
}

closingTagDict = {
    line_number: tag for line_number, tag in devoidedTagDict.items()
    if re.match(
        closingTagRegex,
        tag
    )
}

numberOfOpeningTags = len(openingTagDict.items())
numberOfClosingTags = len(closingTagDict.items())

filteredClosingTagDict = {
    line_number: re.sub('/', '', tag) for line_number, tag in closingTagDict.items()
}

if numberOfOpeningTags == numberOfClosingTags:
    print()
    print(
        "Your HTML is perfectly matched. You're \033[1;32mawesome\033[1;m\033[0m!")
    print()
else:
    print()
    print('The following tags are \033[1;41munclosed\033[1;m\033[0m:')
    print()
    print({
        line_number: tag for line_number, tag in openingTagDict.items()
        if tag not in filteredClosingTagDict.values()
    })
    print()
