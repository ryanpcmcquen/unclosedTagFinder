import re

html = '''
<!doctype html>
<html>
<div>
    <span>Foo
</div>
</html>
'''

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
    map(lambda str: re.sub('/', '', str), closingTagList)
)

if numberOfOpeningTags == numberOfClosingTags:
    print('Your HTML is perfectly matched.')
else:
    print('The following elements are unclosed:')
    print(set(openingTagList).difference(filteredClosingTagList))
