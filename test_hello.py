import unittest

import hello


class HelloTest(unittest.TestCase):
    def setUp(self):
        hello.app.config['TESTING'] = True
        self.app = hello.app.test_client()

    def tearDown(self):
        pass

    def test_hello(self):
        rv = self.app.get('/')
        assert "Hello, World!" in rv.data


if __name__ == '__main__':
    unittest.main()
