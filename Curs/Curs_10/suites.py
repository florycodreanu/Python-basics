import unittest

from Curs_10.alerts import Alerts
from Curs_10.context_menu import ContextMenu
from Curs_10.firefox_plus_auth import AuthenticationInFirefox
from Curs_10.keys import Keyboard

"""
1. pip install html-testRunner
2. Din python packages
"""

import HtmlTestRunner


class TestSuite(unittest.TestCase):

	def test_suite(self):
		test_de_rulat = unittest.TestSuite()
		test_de_rulat.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
								unittest.defaultTestLoader.loadTestsFromTestCase(ContextMenu),
								unittest.defaultTestLoader.loadTestsFromTestCase(AuthenticationInFirefox),
								unittest.defaultTestLoader.loadTestsFromTestCase(Keyboard)])

		runner = HtmlTestRunner.HTMLTestRunner(
				combine_reports=True,  # vrem sa ne genereze un singur raport pentru toate clasele
				report_title="Test Execution Report",
				report_name="Test Results"
		)

		runner.run(test_de_rulat)
