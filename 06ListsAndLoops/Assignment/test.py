import unittest
import yaml
import inspect
import main
import os

def test_function_definition(test_case, module, function_name, expected_num_args):
    # check the function is defined
    function_defined = hasattr(module, function_name)
    test_case.assertTrue(function_defined, f"{function_name} is not defined in {module.__name__}")

    # check the function takes correct # arguments
    function = getattr(module, function_name)
    signature = inspect.signature(function)
    num_arguments = len(signature.parameters)

    test_case.assertEqual(num_arguments, expected_num_args, f"{function_name} should take {expected_num_args} argument(s)")

def execute_test(test_case, module, function_name, data):
    test_function_definition(test_case, module, function_name, len(data[function_name][0]["input"]))
    func = getattr(module, function_name)
    for row in data[function_name]:
      with test_case.subTest(arguments=row["input"]):
          arguments = row["input"]
          expected_result = row["output"]
          result = func(*arguments)
          test_case.assertEqual(result, expected_result, f"{function_name}({', '.join(map(str, arguments))}) was expected to return:\n{expected_result}\nInstead, it returned:\n{result}\n")

class TestFunctions(unittest.TestCase):
    longMessage = False

    @classmethod
    def setUpClass(cls):
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(__location__, "testing_data.yaml"), "r") as file:
            cls.data = yaml.safe_load(file)

    def test_count_failing_grades(self):
        execute_test(self, main, "count_failing_grades", self.data)

    def test_count_act_scores(self):
        execute_test(self, main, "count_act_scores", self.data)
    
    def test_number_sum(self):
        execute_test(self, main, "number_sum", self.data)

    def test_average_act_score(self):
        execute_test(self, main, "average_act_score", self.data)
    
    def test_all_true(self):
        execute_test(self, main, "all_true", self.data)

    def test_any_true(self):
        execute_test(self, main, "any_true", self.data)

    def test_mostly_true(self):
        execute_test(self, main, "mostly_true", self.data)
    
    def test_has_vowel(self):
        execute_test(self, main, "has_vowel", self.data)
    
    def test_all_the_same(self):
        execute_test(self, main, "all_the_same", self.data)

    def test_increasing(self):
        execute_test(self, main, "increasing", self.data)

    def test_is_incrementing(self):
        execute_test(self, main, "is_incrementing", self.data)

    def test_has_adjacent_repeat(self):
        execute_test(self, main, "has_adjacent_repeat", self.data)

    def test_sum_with_skips(self):
        execute_test(self, main, "sum_with_skips", self.data)
    
if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False, catchbreak=False)
