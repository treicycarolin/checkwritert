def read_input():
  return input("Enter the dollar amount (e.g., 145.35): ")

def validate_input(dollar_amount):
  if not dollar_amount.replace('.', '').isdigit() or dollar_amount.count('.') != 1:
      raise ValueError("Invalid. Please enter a valid dollar amount.")
  return True

def split_amount(dollar_amount):
  return map(int, dollar_amount.split('.'))

def number_to_words(num):
  under_20 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 
              'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
  tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
  thousands = ['Thousand', 'Million', 'Billion']

  def words(n):
      if n < 20:
          return under_20[n]
      elif n < 100:
          return tens[(n // 10) - 2] + ('' if n % 10 == 0 else ' ' + under_20[n % 10])
      elif n < 1000:
          return under_20[n // 100] + ' Hundred' + ('' if n % 100 == 0 else ' ' + words(n % 100))
      else:
          for i, word in enumerate(thousands, 1):
              if n < 1000 ** (i + 1):
                  return words(n // 1000 ** i) + ' ' + word + ('' if n % 1000 ** i == 0 else ' ' + words(n % 1000 ** i))
  return words(num)

def cents_to_words(cents):
  return number_to_words(cents) if cents else 'Zero'

def format_output(dollar_part, cent_part):
  return f'{dollar_part} dollars and {cent_part}/100'

def print_output(check_format):
  print(f'The amount in words: {check_format}')

def convert_to_check_format(dollar_amount):
  dollars, cents = split_amount(dollar_amount)
  dollar_part = number_to_words(dollars)
  cent_part = cents_to_words(cents)
  return format_output(dollar_part, cent_part)

def check_writer():
  while True:
      try:
          dollar_amount = read_input()
          validate_input(dollar_amount)
          break
      except ValueError as e:
          print(e)

  check_format = convert_to_check_format(dollar_amount)
  print_output(check_format)

if __name__ == '__main__':
  check_writer()
