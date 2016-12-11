# coding=utf-8

import tempfile
import unittest

import os
from btls.mail import render_template, send_mail


def load_env(auto=True):
    if os.path.exists('.env'):
        print('Importing environment from .env...')
        env_dict = {}
        with open('.env') as fp:
            for line in fp.readlines():
                var = line.strip().split('=')
                if len(var) == 2:
                    env_dict[var[0]] = var[1]

        if auto:
            os.environ.update(env_dict)

        return env_dict


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

    def test_send_mail(self):
        load_env()
        to = os.environ.get('TEST_MAIL_TO')
        send_mail(to, 'mail from unittest', 'hello btls')


if __name__ == '__main__':
    unittest.main()
