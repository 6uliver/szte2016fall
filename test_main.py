from flask import json
import unittest

import main


class MainTest(unittest.TestCase):
    def setUp(self):
        self.a_movie_data = {"title": "Interstellar", "year": 2014, "director": "Christopher Nolan"}

        main.app.config['TESTING'] = True
        self.app = main.app.test_client()

    def tearDown(self):
        self.app.application.movies.__init__();

    def test_hello(self):
        rv = self.app.get('/')
        assert "Hello, World!" in rv.data

    def test_get_movie_nonexisting(self):
        response = self.app.get('/movies/1')
        assert response.status_code == 404

    def test_create_new_movie(self):
        response = self.app.post('/movies/'
                                 , data=json.dumps(self.a_movie_data)
                                 , content_type='application/json')
        assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()
