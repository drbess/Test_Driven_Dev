import unittest


class TestParse(unittest.TestCase):
    def test_parse_cust_name(self):
        expected_names = ['CUSTOMER A', 'CUSTOMER_B']
        '''This will fail as "cp" is unresolved'''
        parsed_names = cp.parseCustomerNames()
        self.assertEqual(list, type(parsed_names))
        self.assertEqual(expected_names, parsed_names)

# To test, run "python3.7 -m unittest tes_parser.py"
