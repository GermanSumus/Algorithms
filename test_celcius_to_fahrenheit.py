import unittest
from celcius_to_fahrenheit import celcius_to_fahrenheit as c_to_f


class C_to_F(unittest.TestCase):

    def test_celcius(self):
        self.assertEqual(c_to_f(100), 212)
        self.assertEqual(c_to_f(0), 32)
        self.assertEqual(c_to_f(-40), -40)



if __name__ == '__main__':
    unittest.main()


    
