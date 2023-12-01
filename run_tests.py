import unittest
from coverage import Coverage
from unittest.loader import TestLoader
import xmlrunner
import fire
from copy import deepcopy


class TestErrorException(Exception):
    def __init__(self, message: str = ""):
        self.message = message
        self.error = True
        super().__init__(self.message)


class TestNotPassedException(Exception):
    def __init__(self, message: str = ""):
        self.message = message
        self.error = True
        super().__init__(self.message)


def check_no_errors_in_tests(suite: unittest.suite.TestSuite):
    failedTestClass = unittest.loader._FailedTest
    for tests in suite._tests:
        for test in tests:
            if isinstance(test, failedTestClass):
                raise TestErrorException("Failed to load tests.")


def check_if_tests_passed(test_results: xmlrunner.result._XMLTestResult):
    successes = len(test_results.successes)
    failures = len(test_results.failures)
    errors = len(test_results.errors)
    total = successes + failures + errors
    if failures > 0 or errors > 0:
        raise TestNotPassedException(
            f"{successes}/{total} Tests passed. {failures} Tests failed and {errors} Tests had errors."
        )


def main(
    discover_dir: str = "tests",
    discover: str = "test_*",
    test_report_output: str = "test_results.xml",
    coverage_report_output: str = "coverage.xml",
    coverage_omit: list = ["*/tests*", "*/config*.py", "*run_tests.py"],
    ignore_errors: bool = False,
):

    cov = Coverage(omit=coverage_omit)
    cov.start()
    with open(test_report_output, "wb") as output:
        testRunner = xmlrunner.XMLTestRunner(output=output)
        run_suite = TestLoader().discover(discover_dir, discover)
        check_suite = deepcopy(run_suite)
        test_results = testRunner.run(run_suite)
        check_no_errors_in_tests(check_suite)
        check_if_tests_passed(test_results=test_results)
    cov.stop()
    cov.save()

    cov.xml_report(outfile=coverage_report_output, ignore_errors=ignore_errors)
    cov.html_report(ignore_errors=ignore_errors)
    cov.report(ignore_errors=ignore_errors)


if __name__ == "__main__":
    fire.Fire(main)
