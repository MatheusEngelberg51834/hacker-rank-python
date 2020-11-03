from html.parser import HTMLParser

n = int(input())

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if attrs != []:
            for attr in attrs:
                print('->', attr[0], '>', attr[1])
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)

acc = True

for _ in range(n):

    if acc == True:
        line = str(input())
        if '<!--' in line:
            acc = False
            line = ''
            print('banana')

    if acc == False:
        line = str(input())
        if '-->' not in line:
            line = ''
        else:
            line = ''
            acc = True
          
    parser = MyHTMLParser()
    parser.feed(line)