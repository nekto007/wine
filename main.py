import datetime
from collections import OrderedDict, defaultdict
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape

PRODUCTS_FILEPATH = 'example.xlsx'
now = datetime.datetime.now()
birth_year = 1920
age = now.year - birth_year


def ending_year(age):
    how_old = age % 100
    if 21 > how_old > 4:
        return 'лет'
    how_old = how_old % 10
    if how_old == 1:
        return 'год'
    if 1 < how_old < 5:
        return 'года'
    else:
        return 'лет'


def get_products(filepath):
    df = pandas.read_excel(filepath, na_values=['N/A', 'NA'], keep_default_na=False)
    products = df.to_dict(orient="records")
    products_by_categories = defaultdict(list)
    for product in products:
        products_by_categories[product["Категория"]].append(product)
    sorted_products_by_categories = OrderedDict(sorted(products_by_categories.items()))
    return sorted_products_by_categories


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    rendered_page = template.render(
        age=age,
        years=ending_year(age),
        categories=get_products(PRODUCTS_FILEPATH),
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
