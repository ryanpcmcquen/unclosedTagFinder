import re

html = '''
<html>
<div>
    <span>Foo
</div>
</html>
'''

openingTags = re.compile('<\\w*>', flags=re.I | re.M)
closingTags = re.compile('<\/\\w*>', flags=re.I | re.M)

openingTagList = re.findall(openingTags, html)
numberOfOpeningTags = len(openingTagList)
closingTagList = re.findall(closingTags, html)
numberOfClosingTags = len(closingTagList)

#filteredClosingTagList = [re.sub('/', '', str) for str in closingTagList]
filteredClosingTagList = list(
    map(lambda str: re.sub('/', '', str), closingTagList)
)

#print(filteredClosingTagList)

if numberOfOpeningTags == numberOfClosingTags:
    print('Your HTML is perfectly matched.')
else:
    print('The following elements are unclosed:')
    print(set(openingTagList).difference(filteredClosingTagList))
