from operator import truediv
from platform import release


class Movies:
    """
    Analyzing data from movies.csv
    """
    def __init__(self, path_to_the_file="../ml-latest-small/movies.csv"):
        """
        Put here any fields that you think you will need.
        """
        debug = True
        self.path = path_to_the_file
        with open(self.path, "r", encoding="utf-8") as file:
            tmp = list(map(lambda x: x.rstrip("\n").split(","), file.readlines()[1:]))
            tmp = [i if len(i) == 3 else
                [i[0], ",".join(i[1:-1]), i[-1]] for i in tmp]
            tmp = [[i[0], i[1].strip("\""), i[2]] for i in tmp]
            self.data = tmp
        if debug is True:
            self.data = self.data[:15]

    def dist_by_release(self):
        """
        The method returns a dict or an OrderedDict where the
        keys are years and the values are counts.
        You need to extract years from the titles.
        Sort it by counts descendingly.
        """
        release_years = {}
        for film in self.data:
            movie_info = film[1].split(" ")
            year = movie_info[-1][1:-1]
            if release_years.get(year) is None:
                release_years[year] = 0
            release_years[year] += 1
        return release_years
    def dist_by_genres(self):
        """
        The method returns a dict where the keys are genres and the values are counts.
     Sort it by counts descendingly.
        """

        genres = {}
        for film in self.data:
            genres_of_film = film[2].split("|")
            for genre in genres_of_film:
                if genres.get(genre) is None:
                    genres[genre] = 0
                genres[genre] += 1
        genres = dict(sorted(list(genres.items()), key=lambda item:-item[1]))
        return genres
    def most_genres(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and 
        the values are the number of genres of the movie. Sort it by numbers descendingly.
        """
        all_movies = list(zip(
                            [film[1] for film in self.data],
                            [len(film[2].split("|")) for film in self.data]
        ))
        all_movies.sort(key=lambda film: -film[1])
        movies = dict(all_movies[:n])
        return movies


if __name__ == "__main__":
    print(Movies().most_genres(1))