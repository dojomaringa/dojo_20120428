import unittest
from fizzbuzz import fizzbuzz

class TestFizz(unittest.TestCase):
  def assert_fizz(self, numero):
    self.assertEqual(fizzbuzz(numero), "fizz")
    
  def assert_buzz(self, numero):
    self.assertEqual(fizzbuzz(numero), "buzz")
    
  def assert_fizzbuzz(self, numero):
    self.assertEqual(fizzbuzz(numero), "fizzbuzz")
    
  def teste_proprio_numero(self):
    self.assertEqual(fizzbuzz(1), "1")
    self.assertEqual(fizzbuzz(2), "2")
  
  def teste_numero_multiplo_de_tres(self):
    self.assert_fizz(3)
    self.assert_fizz(6)
    self.assert_fizz(9)
  
  def teste_numero_multiplo_de_cinco(self):
    self.assert_buzz(5)
    self.assert_buzz(10)
    self.assert_buzz(20)
  
  def teste_numero_multiplo_de_tres_e_cinco(self):
    self.assert_fizzbuzz(15)
    self.assert_fizzbuzz(30)

    
unittest.main()