#!/usr/bin/env python3

class MyString:

  def __init__(self,value='') -> None:
      self.value = value

  @property
  def value(self):
      return self._value
  
  @value.setter
  def value(self, value):
      if type(value) == str:
          self._value = value
      else:
          print("The value must be a string.")

  def is_sentence(self):
      last_character = self.value[len(self.value)-1]
      if last_character == '.':
          return True
      else:
          return False
      #or an easier way is to use the below string
      #return self.value.endswith('.')

  def is_question(self):
      return self.value.endswith('?')
  
  def is_exclamation(self):
      return self.value.endswith('!')
  
  def count_sentences(self):
      count = 0
      prev_char = ''
      for char in self.value:
          if char in ['.', '!', '?'] and prev_char.isalpha():
              count+=1
          prev_char = char
      return count 