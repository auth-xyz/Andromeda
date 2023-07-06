import requests
from bs4 import BeautifulSoup

url = "http://rsdb.org/full"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

max_slur_number = 10

td_values = []

for i in range(1, max_slur_number + 1):
    slur_id = f"slur_{i}"
    data_id = f"slur_{i}"

    rows = soup.find_all("tr", {"id": slur_id, "data_id": data_id})

    for row in rows:
        first_td = row.find("td")
        a_tag = first_td.find("a")
        if a_tag:
            td_values.append(a_tag.get("href"))

print(td_values)