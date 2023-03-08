# New Russian wine

Site of the store of author's wine "New Russian wine".

## Launch
1. Clone project
```bash 
git clone https://github.com/nekto007/wine.git
cd wine
```

2. Install requirements
```bash
pip install -r requirements.txt
```
3. Переменные окружения

Для запуска программы требуется excel файл. По умолчанию указан файл: example.xlsx в .env:
```
PRODUCTS_FILEPATH='example.xlsx'
```
4. Run
if you have specific place to excel file:
```bash 
python main.py path_to_file
```
or you might use default path to file from .env:
```bash 
python main.py
```

5. Open site in browser
[http://127.0.0.1:8000](http://127.0.0.1:8000).

6. This site can be filled with another drinks if needed
- Open ```example.xlsx``` and fill it accordingly
- Repeat steps 4 and 5