import unittest
import ExampleQuestions
import Constants

class TestExampleQuestions(unittest.TestCase):
    
    def test_question_one(self):
        actual=ExampleQuestions.questionOne(Constants.testString,'EXPOSURE_DURATION')
        self.assertEqual(actual,'192')

    def test_question_two(self):
        actual=ExampleQuestions.questionTwo(Constants.testStringUnit,'EXPOSURE_DURATION')
        self.assertEqual(actual,'192')

    def test_question_three(self):
        actual=ExampleQuestions.questionThree(Constants.testStringUnit,'Seconds','EXPOSURE_DURATION')
        self.assertEqual(actual,0.192) 

    def test_question_four(self):
        actual=ExampleQuestions.questionFour([Constants.testStringMultipleA,Constants.testStringMultipleB,Constants.testStringMultipleC],'Maximum','FOCAL_PLANE_TEMPERATURE')
        self.assertEqual(actual,-25.94)
    
    def test_question_five(self):
        actual=ExampleQuestions.questionFive([Constants.testStringMultipleA,Constants.testStringMultipleB,Constants.testStringMultipleC],'FILTER_NUMBER is 2','EXPOSURE_DURATION')
        self.assertEqual(actual,[192,209])

if __name__ == '__main__':
    unittest.main()

