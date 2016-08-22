from model.movies import Movies

import unittest


class MoviesModelTest(unittest.TestCase):
    def setUp(self):
        self.aMovieData = {}
        self.otherMovieData = {}
        self.model = Movies()

    def tearDown(self):
        pass

    def test_get_movie_nonexisting(self):
        result = self.model.get_movie(1)
        self.assertFalse(result)

    def test_create_movie_different_ids(self):
        self.model.create_movie(self.aMovieData)
        self.model.create_movie(self.otherMovieData)

        self.assertNotEqual(self.aMovieData['id'], self.otherMovieData['id'])

    def test_create_movie_alters_data(self):
        moviedata = {}
        self.model.create_movie(moviedata)
        self.assertIn('id', moviedata)


if __name__ == '__main__':
    unittest.main()
