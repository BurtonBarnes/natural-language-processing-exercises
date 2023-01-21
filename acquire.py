from requests import get
from bs4 import BeautifulSoup
import os
import pandas as pd


url = 'https://codeup.com/blog/'
headers = {'User-Agent': 'Codeup Data Science'}
response = get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

links = [link['href'] for link in soup.select('.more-link')]

articles = []

for url in links:
    
    url_response = get(url, headers=headers)
    soup = BeautifulSoup(url_response.text)
    
    title = soup.find('h1', class_='entry-title').text
    content = soup.find('div', class_='entry-content').text.strip()
    
    article_dict = {
        'title': title,
        'content': content
    }
    
    articles.append(article_dict)
    
blog_article_df = pd.DataFrame(articles)
blog_article_df




# catorgories = ['business', 'sports', 'technology', 'entertainment']
categories = [li.text.lower() for li in soup.select('li')][1:]
categories[0] = 'national'

inshorts = []

for category in categories:
    
    url = 'https://inshorts.com/en/read' + '/' + category
    response = get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    titles = [span.text for span in soup.find_all('span', itemprop='headline')]
    contents = [div.text for div in soup.find_all('div', itemprop='articleBody')]
    
    for i in range(len(titles)):
        
        article = {
            'title': titles[i],
            'content': contents[i],
            'category': category,
        }
        
        inshorts.append(article)
        
        
inshorts_article_df = pd.DataFrame(inshorts)
inshorts_article_df
