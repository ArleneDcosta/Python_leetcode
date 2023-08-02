# web_scraping helper
import requests
from bs4 import BeautifulSoup
import os
import sys
from google.cloud import bigquery
import datetime
import pandas as pd
from urllib.request import Request, urlopen
# Creating an Environmental Variable for the service key configuration
#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/opt/airflow/dags/configs/ServiceKey_GoogleCloud.json'

# Create a client
#bigquery_client = bigquery.Client()


def _get_soup(chart):
    '''
    Get the BeautifulSoup object from a url.
    Args:
        - chart(str) = chart to scrape
            Options: 'most_popular_movies', 'top_250_movies', 'top_english_movies', 'top_250_tv'
    Returns:
        - soup(BeautifulSoup) = BeautifulSoup object
    '''

    # Send a get request and parse using BeautifulSoup
    if chart == 'most_popular_movies':
        url = 'https://www.imdb.com/chart/moviemeter?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=470df400-70d9-4f35-bb05-8646a1195842&pf_rd_r=5V6VAGPEK222QB9E0SZ8&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=toptv&ref_=chttvtp_ql_2'

    if chart == 'top_250_movies':
        url = 'https://www.imdb.com/chart/top?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=470df400-70d9-4f35-bb05-8646a1195842&pf_rd_r=5V6VAGPEK222QB9E0SZ8&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=toptv&ref_=chttvtp_ql_3'

    if chart == 'top_english_movies':
        url = 'https://www.imdb.com/chart/top-english-movies?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=470df400-70d9-4f35-bb05-8646a1195842&pf_rd_r=3YMHR1ECWH2NNG5TPH1C&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=boxoffice&ref_=chtbo_ql_4'

    if chart == 'top_250_tv':
        url = 'https://www.imdb.com/chart/tvmeter?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=470df400-70d9-4f35-bb05-8646a1195842&pf_rd_r=J9H259QR55SJJ93K51B2&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=topenglish&ref_=chttentp_ql_5'

    response = requests.get(url)
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(url, headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page)
    # print(response.text)
    # soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def _scrape_movies(soup):
    '''
    Scrape the most popular titles and ratings from the IMDB website.
    Args:
        - soup(BeautifulSoup) = BeautifulSoup object
    Returns:
        - movie_dict(dict) = Dictionary of movie names and ratings
    '''
    # Find all movie names in the url
    movie_names = []
    movie_years = []
    movie_ratings = []
    user_votings = []

    # Find all movie in the url
    titlesRefs = soup.find_all('td', {'class': 'titleColumn'})
    ratingsRefs = soup.find_all('td', {'class': 'ratingColumn imdbRating'})

    # Collect movie title, release year, ratings and user votings
    for title in titlesRefs:
        try:
            movie_names.append(title.find("a").text)
        except:
            print('Missing title. Replacing with -1')
            movie_names.append(-1)

        try:
            movie_years.append(int(title.find("span").text[1:-1]))
        except:
            print('Missing year. Replacing with -1')
            movie_years.append(-1)

    for rating in ratingsRefs:
        try:
            movie_ratings.append(float(rating.find("strong").text))
        except:
            print('Missing rating. Replacing with -1')
            movie_ratings.append(-1)

        try:
            votes_str = rating.find("strong").attrs['title']
            votes_str = votes_str.split(' ')[3]
            votes_int = int(votes_str.replace(',', ''))
            user_votings.append(votes_int)
        except:
            user_votings.append(-1)

    # Create a dataframe
    movie_df = pd.DataFrame({'movie_name': movie_names, 'movie_year': movie_years, 'movie_rating': movie_ratings,
                             'user_votings': user_votings})

    # Add movie_id
    movie_df['movie_id'] = movie_df.index + 1

    # set date
    movie_df['update_date'] = datetime.datetime.today().strftime('%Y-%m-%d')

    # reorder columns
    movie_df = movie_df[['movie_id', 'movie_name', 'movie_year', 'movie_rating', 'user_votings', 'update_date']]

    return movie_df
def main():
    soup = _get_soup(chart='top_250_movies')
    print(soup)
    # movies_df = _scrape_movies(soup)
    # print(movies_df.head())

if __name__ == '__main__':
    main()