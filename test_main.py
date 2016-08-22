import unittest

import main


class MainTest(unittest.TestCase):
    def setUp(self):
        main.app.config['TESTING'] = True
        self.app = main.app.test_client()

    def tearDown(self):
        pass

    def test_hello(self):
        rv = self.app.get('/')
        assert "Hello, World!" in rv.data

    def test_get_movie_nonexisting(self):
        response = self.app.get('/movies/1')
        assert response.status_code == 404


if __name__ == '__main__':
    unittest.main()
