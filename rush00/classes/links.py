from bs4 import BeautifulSoup
import requests


class Links:
    """
    Analyzing data from links.csv
    """
    def __init__(self, path_to_the_file):
        """
        Put here any fields that you think you will need.
        """
        self.path = path_to_the_file
        with open(self.path, "r") as f:
            data = f.readlines()[1:].rstrip("\n").split("\n")
            self.ibdm_keys = dict([i[0] for i in data], [i[1] for i in data])
            self.tmdb_keys = dict([i[0] for i in data], [i[2] for i in data])
        self.url_format = "https://www.imdb.com/title/tt{}"


    @lru_cache(128 * 1024 * 1024)
    def _get_all_fields_to_movie(self, movie_id):
        
    
    def get_imdb(self, list_of_movies, list_of_fields):
        """
        The method returns a list of lists [movieId, field1, field2, field3, ...]
        for the list of movies given as the argument (movieId).
        For example, [movieId, Director, Budget, Cumulative Worldwide Gross, Runtime].
        The values should be parsed from the IMDB webpages of the movies.
     Sort it by movieId descendingly.
        """

        for movie_id in list_of_movies:
            url = self.url_format.format(self.ibdm_keys[str(movie_id)][1])
            data = requests.get(url)
            soup = BeautifulSoup(data)
            soup = soup.find_all('div', {'class' : 'ipc-page-content-container'})[5]
            soupset = soup.find_all('li', {'class', 'ipc-metadata-list__item'})

            dict_of_soup = {}
            for soup in soupset:
                label_soup = soup.find({'class' : 'ipc-metadata-list-item__label'})
                if label_soup is None:
                    continue
                label = label_soup.text

                text_soup = soup.find('ipc-metadata-list-item__content-container')
                if text_soup is not None:
                    text_soup = text_soup.text
                dict_of_soup[label] = str(text_soup)




        return imdb_info
        
    def top_directors(self, n):
        """
        The method returns a dict with top-n directors where the keys are directors and 
        the values are numbers of movies created by them. Sort it by numbers descendingly.
        """
        return directors
        
    def most_expensive(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are their budgets. Sort it by budgets descendingly.
        """
        return budgets
        
    def most_profitable(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are the difference between cumulative worldwide gross and budget.
     Sort it by the difference descendingly.
        """
        return profits
        
    def longest(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are their runtime. If there are more than one version â€“ choose any.
     Sort it by runtime descendingly.
        """
        return runtimes
        
    def top_cost_per_minute(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
the values are the budgets divided by their runtime. The budgets can be in different currencies â€“ do not pay attention to it. 
     The values should be rounded to 2 decimals. Sort it by the division descendingly.
        """
        return costs