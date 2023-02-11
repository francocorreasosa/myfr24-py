import pprint
from hashlib import sha256
from bs4 import BeautifulSoup
from datetime import datetime


def parse_flights(html: str):
    soup = BeautifulSoup(html)
    header = []
    rows = []

    for i, flight in enumerate(soup.find("table").find_all("tr")):
        if i == 0:
            header = [el.text.strip() for el in flight.find_all("th")]
        else:
            row = {}
            flight_data = enumerate([el.text.strip() for el in flight.find_all("td")])

            for i, item in flight_data:
                key = header[i]
                row[key] = item

            row["Id"] = sha256(
                f"{row['Date']}:{row['Flight'] if 'Flight' in row else 'PRIV'}".encode()
            ).hexdigest()

            row["Class"] = row[""].split("\n")[0]
            row["Kind"] = row[""].split("\n")[1]
            row["Date"] = datetime.strptime(row["Date"], "%Y-%M-%d")

            row.pop("")

            rows.append(row)

    return rows
