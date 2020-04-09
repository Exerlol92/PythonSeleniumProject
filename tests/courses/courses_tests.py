from page_object.courses.register_courses_page import RegisterCoursesPage
from utilities.status import Status
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
from page_object.home.navigation_page import NavigationPage

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class CoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSet(self, oneTimeSetUp):
        self.cp = RegisterCoursesPage(self.driver)
        self.ts = Status(self.driver)
        self.np = NavigationPage(self.driver)

    # @pytest.mark.run(order=1)
    # def test_invalidEnrollment(self):
    #     self.cp.enrollToCourse()
    #     result = self.cp.verifyEnrollFailed()
    #     self.ts.markFinal("Verification of Invalid Enrollment", result, "Negative Test Case")

    @pytest.mark.run(order=1)
    @data(*getCSVData('/Users/Dule-PC/workspace_python/PageObjectModel_framework/testdata.csv'))
    @unpack
    def test_invalidEnrollment(self, course, courseFullName):
        self.cp.enrollToCourse(course, courseFullName)
        result = self.cp.verifyIfEnrollBtnIsDisable()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Negative Test Case")
        self.np.navigateToAllCourses()