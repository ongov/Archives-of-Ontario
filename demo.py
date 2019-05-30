import textract

def test(filename):
    file = open(filename,'r')
    content = ""
    for line in file.readlines():
        content += line
    return content

text = test('text.txt')
print(text.replace('\\n',' '))
