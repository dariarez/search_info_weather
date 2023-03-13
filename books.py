import requests
import pandas as pd


inquiry = input('Enter the book title or author`s name: ')

url = f'https://www.googleapis.com/books/v1/volumes?q={inquiry}'
response = requests.get(url)
data = response.json()

for i in data['items']:
    volumeinfo = i['volumeInfo']
    df = pd.DataFrame({
        'title' :   [volumeinfo["title"]],
        'authors':  [volumeinfo['authors']],
        'datepub':  [volumeinfo['publishedDate']],
        'pagecount':    [volumeinfo['pageCount']],
        'categories':   [volumeinfo['categories']],
    })
   

    print(df)