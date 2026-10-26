html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>seni çok seviyorum selin</title>
</head>
<body>

    <h1 id="header">
        aşkım seni çok seviyorum 
    </h1>

    <div class="Soru 1"> 
        <h2>
            beni seviyor musun?
        </h2>

        <ul>
            <li>evet</li>
            <li>evet</li>
            <li>evet</li>
        </ul>
    </div>

        <div class="Soru 2"> 
        <h2>
            bana aşık mısın?
        </h2>

        <ul>
            <li>yes</li>
            <li>yes</li>
            <li>yes</li>
        </ul>
    </div>

    <div class="Soru 3"> 
        <h2>
            beni seviyor musun?
        </h2>

        <ul>
            <li>ja</li>
            <li>ja</li>
            <li>ja</li>
        </ul>
    </div>

<img src="foto.jpg" alt="">

<a class="sister" href="http://example1.com/elsie" id="link1">Elsie</a>
<a class="sister" href="http://example2.com/elsie" id="link1">Elsie</a>
<a class="sister" href="http://example3.com/elsie" id="link1">Elsie</a>

</body>
</html>
"""


from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')

result = soup.prettify()
result = soup.title
result = soup.head
result = soup.body

result = soup.title.name
result = soup.title.string
result = soup.h1
result = soup.h2.name
result = soup.h2.string
result = soup.h1.string
result = soup.find_all('h2')
result = soup.find_all('h2')[0]
result = soup.div
result = soup.find_all('div')[1]
result = soup.find_all('div')[1].ul.find_all('li')

result = soup.div.findChildren()
result = soup.div.findNextSibling()
result = soup.div.findNextSibling().findNextSibling().findPreviousSibling()

result = soup.find_all('a')

for link in result:
    print(link.get('href'))

# print(result)