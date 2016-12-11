# coding=utf-8

import tempfile
import unittest

import os
from btls.mail import render_template


class TestMail(unittest.TestCase):
    template = "<html><head><title>{{ title }}</title></head>" \
               + "<body>{{ body }}</body></html>"
    expected = "<html><head><title>Hello</title></head>" \
               + "<body>Test</body></html>"

    def test_render_template_string(self):
        output = render_template(self.template, title='Hello', body='Test')

        self.assertEqual(output, self.expected)

    def setUp(self):
        self.temp_file = tempfile.mktemp()

    def tearDown(self):
        if os.path.exists(self.temp_file):
            os.remove(self.temp_file)

    def test_render_template_file(self):
        with open(self.temp_file, 'w') as fp:
            fp.write(self.template)

        output = render_template(self.temp_file, title='Hello', body='Test')

        self.assertEqual(output, self.expected)


if __name__ == '__main__':
    unittest.main()
