import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_table_data(table) -> list:
    # Extract the table data
    table_data = []
    for row in table.find_all("tr"):
        row_data = [cell.get_text(strip=True) for cell in row.find_all("td")]
        if row_data:
            table_data.append(row_data)
    return table_data


def add_table_headers(table, df: pd.DataFrame) -> None:
    # Set the column names if available in the table
    header_row = table.find("tr")
    if header_row:
        headers = [header.get_text(strip=True) for header in header_row.find_all("th")]
        if headers:
            df.columns = headers


def get_table_dataframe(table) -> pd.DataFrame:
    table_data = get_table_data(table)
    df = pd.DataFrame(table_data)
    add_table_headers(table, df)
    return df


def get_forex_dict(df: pd.DataFrame) -> dict:
    return df.to_dict(orient="index")


if __name__ == '__main__':
    # Send a GET request to the website
    url = "https://www.xm.com/forex-trading"
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table element using its HTML tag and any relevant attributes
    table = soup.find("table")

    # # Convert table to a pandas DataFrame
    df = get_table_dataframe(table)
    # Print the DataFrame
    print(df)
