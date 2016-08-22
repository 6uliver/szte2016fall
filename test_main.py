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


if __name__ == '__main__':
    unittest.main()
