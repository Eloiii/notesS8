from bs4 import BeautifulSoup
import requests
import secret


async def main():
    res = []
    response = requests.get(
        'https://chamilo.univ-grenoble-alpes.fr/main/document/document.php',
        params=secret.params,
        cookies=secret.cookies,
        headers=secret.headers,
    )

    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', attrs={'class': 'table'})
    rows = table.find_all('tr')[1:]

    for row in rows:
        res.append(row.find_all('td')[1].find('a').text)

    return res
