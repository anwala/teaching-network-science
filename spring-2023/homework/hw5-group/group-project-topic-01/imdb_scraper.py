'''
imdb_scraper.py
Scrape IMDb director credits and movie crew
Alexander C. Nwala 
W&M DATA 340-02 - Network Science

Requirements:
* BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/ (pip install beautifulsoup4)
* NwalaTextUtils: https://github.com/oduwsdl/NwalaTextUtils (pip install NwalaTextUtils)
* PyMovieDb: https://github.com/itsmehemant7/PyMovieDb (pip install PyMovieDb)
* isoduration: https://github.com/bolsote/isoduration (pip install isoduration)
'''
import json

from bs4 import BeautifulSoup
from datetime import timedelta
from isoduration import parse_duration
from warnings import warn

from NwalaTextUtils.textutils import derefURI
from NwalaTextUtils.textutils import genericErrorInfo
from NwalaTextUtils.textutils import getPgTitleFrmHTML

from PyMovieDb import IMDB

def get_full_credits_for_director(dir_id):

    def get_movie_link(mov_elm, mov_year):
        
        mov_links = mov_elm.find_all('a')

        for m in mov_links:
            
            title = m.text.strip()
            m = m['href'].strip()
            mov_year = mov_year.text.strip() if mov_year is not None else ''

            if( m.startswith('/title/tt') ):
                movie_note = mov_elm.text.replace(title, '').replace(mov_year, '')
                movie_note = ' '.join(movie_note.split())
                return {'title': title, 'uri': f'https://www.imdb.com{m}', 'year': mov_year, 'note': movie_note}

        return {}

    def get_movies_section(soup):

        film_sections = soup.find_all(class_='filmo-category-section')
    
        for fs in film_sections:
            is_director_section = fs.find('div')
            if( is_director_section is not None and is_director_section.get('id', '').startswith('director-') ):
                return fs
        
        return None

    uri = f'https://www.imdb.com/name/{dir_id}/fullcredits/'
    html_pg = derefURI(uri)
    title = ''

    try:
        soup = BeautifulSoup(html_pg, 'html.parser')
        title = getPgTitleFrmHTML(html_pg)
        title = title.split('-')[0].strip()
    except:
        genericErrorInfo()
        return {}


    movies = get_movies_section(soup)
    if( movies is None ):
        return {}
    
    dir_credits = {'director_name': title, 'imdb_uri': uri, 'credits': []}
    movies = movies.find_all('div', class_='filmo-row')        
    for m in movies:
        
        m = get_movie_link(m, m.find(class_='year_column'))
        if( len(m) != 0 ):
            dir_credits['credits'].append(m)
        
    return dir_credits

def get_full_crew_for_movie(title_id, set_imdb_details=False):

    def get_crew_table_dets(crew_tab):
    
        crew = []    
        rows = crew_tab.find_all('tr')

        for r in rows:
            
            dets = {}
            cols = r.find_all('td')
            
            for c in cols:
                
                class_name = c.get('class', '')
                if( class_name == '' ):
                    continue

                
                class_name = class_name[0].lower().strip()
                if( class_name in ['name', 'credit'] ):
                
                    dets[class_name] = c.text.strip()
                    link = c.find('a')
                    if( link is not None ):
                        dets['link'] = link.get('href', '')
                        dets['link'] = 'https://www.imdb.com'+dets['link']
            

            if( len(dets) != 0 ):
                crew.append(dets)

        return crew

    full_credits = {}
    uri = f'https://www.imdb.com/title/{title_id}/fullcredits/'
    html_pg = derefURI(uri)

    try:
        soup = BeautifulSoup(html_pg, 'html.parser')
        title = getPgTitleFrmHTML(html_pg)
        title = title.split('-')[0].strip()
    except:
        genericErrorInfo()
        return {}


    soup = soup.find('div', id='fullcredits_content')
    if( soup is None ):
        return {}

    headers = soup.find_all(class_='dataHeaderWithBorder')
    tables = soup.find_all('table')
    
    if( len(headers) != len(tables) ):
        warn(f'len(headers) != len(tables), check for result for integrity: {uri}')


    full_credits = {'title_uri': uri, 'title': title, 'full_credits': [], 'imdb_details': get_movie_imdb_details(title_id) if set_imdb_details is True else {}}
    for i in range(len(headers)):
        
        h = headers[i]
        h = ' '.join(h.text.split())
        
        crew = []
        if( i < len(tables) ):
            crew = get_crew_table_dets(tables[i])
        
        full_credits['full_credits'].append({'role': h, 'crew': crew})

    return full_credits

def get_movie_imdb_details(title_id):
    
    try:
        imdb = IMDB()
        movie = imdb.get_by_id(title_id)
        return json.loads(movie)
    except:
        genericErrorInfo()
        return {}

def get_movie_duration_seconds(title_id, movie=None):

    try:
        if( movie is None ):
            imdb = IMDB()
            movie = imdb.get_by_id(title_id)
            movie = json.loads(movie)

        #duration example: PT2H7M
        duration = movie.get('duration', '')
        if( duration is None or duration == '' ):
            return -1
            
        duration = parse_duration(duration)
    except:
        genericErrorInfo()
        return -1
    
    delta = timedelta(
        days=int(duration.date.years)*365 + int(duration.date.months)*30 + int(duration.date.days), 
        weeks=int(duration.date.weeks),
        hours=int(duration.time.hours),
        minutes=int(duration.time.minutes),
        seconds=int(duration.time.seconds)
    )

    return delta.total_seconds()


def is_feature_film(title_id, movie=None):

    if( get_movie_duration_seconds(title_id, movie=movie) >= 70*60 ):
        #feature film must be at least 70 minutes long
        return True

    return False

def is_feature_film_v2(title_id):

    full_credits = {}
    uri = f'https://www.imdb.com/title/{title_id}/'
    html_pg = derefURI(uri)

    try:
        soup = BeautifulSoup(html_pg, 'html.parser')
    except:
        genericErrorInfo()
        return False

    header = soup.find('h1')
    if( header is None ):
        return False

    year_rating_duration = header.find_next('ul', class_='ipc-inline-list')
    if( len(year_rating_duration) == 0 ):
        return False
    year_rating_duration = list(year_rating_duration)

    #duration example: 1h 39m
    duration = year_rating_duration[-1].text.split(' ')

    total_seconds = 0
    for d in duration:

        try:
            d = d.strip()
            if( d.endswith('h') ):
                total_seconds += int(d.replace('h', '')) * 60 * 60
            elif( d.endswith('m') ):
                total_seconds += int(d.replace('m', '')) * 60
            elif( d.endswith('s') ):
                total_seconds += int(d.replace('s', ''))
        except:
            genericErrorInfo()

    if( total_seconds >= 70*60 ):
        #feature film must be at least 70 minutes long
        return True

    return False
