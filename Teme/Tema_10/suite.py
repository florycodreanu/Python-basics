import unittest

import HtmlTestRunner

from Tema_10.test1_alerts import Alerts
from Tema_10.test2_auth import Authentication
from Tema_10.test3_context_menu import ContextMenu
from Tema_10.test4_keys import Keyboard
from Tema_10.test5_firefox import Firefox
from tema_09 import Login


class TestSuite(unittest.TestCase):

    def test_suite(self):
        teste_de_rulat = unittest.TestSuite()
        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(Authentication),
            unittest.defaultTestLoader.loadTestsFromTestCase(ContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(Keyboard),
            unittest.defaultTestLoader.loadTestsFromTestCase(Firefox),
            unittest.defaultTestLoader.loadTestsFromTestCase(Login)
        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='TestReport',
            report_name='Smoke Test Result'
        )

        runner.run(teste_de_rulat)
