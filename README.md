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
3. Environment variables

An Excel file with beverage data is required to run the program. Create an .env file in the same folder, 
where the script is and put the data in VARIABLE=value format there:
```
PRODUCTS_FILEPATH='path_to_file'
```
4. Run
if you have specific place to Excel file:
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