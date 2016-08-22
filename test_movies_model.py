import unittest

from assertpy import assert_that

from model.movies import Movies


class MoviesModelTest(unittest.TestCase):
    def setUp(self):
        self.aMovieData = {}
        self.otherMovieData = {}
        self.model = Movies()

    def tearDown(self):
        pass

    def test_get_movie_nonexisting(self):
        result = self.model.get_movie(1)

        assert_that(result).is_false()

    def test_get_movie_existing(self):
        self.model.create_movie(self.aMovieData)
        result = self.model.get_movie(1)

        assert_that(result).contains_key('id')

    def test_create_movie_different_ids(self):
        self.model.create_movie(self.aMovieData)
        self.model.create_movie(self.otherMovieData)

        assert_that(self.aMovieData['id']).is_not_equal_to(self.otherMovieData['id'])

    def test_create_movie_alters_data(self):
        moviedata = {}
        self.model.create_movie(moviedata)

        assert_that(moviedata).contains_key('id')


if __name__ == '__main__':
    unittest.main()
