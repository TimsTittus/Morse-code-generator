#python program to convert a text into morse code
morse_code_dict = {
  'A': '.-',
  'B' : '.--',
  'C' : '.---',
  'D' : '..-',
  'E' : '..--',
  'F' : '...-',
  'G' : '-.',
  'H' : '-..',
  'I' : '-...',
  'J' : '--..',
  'K' : '..--',
  'L' : '.-.-',
  'M' : '-.-.',
  'N' : '.--.',
  'O' : '-..-',
  'P' : '.-.',
  'Q' : '-.-',
  'R' : '----',
  'S' : '....',
  'T' : '-.--',
  'U' : '.-..',
  'V' : '---.',
  'W' : '--.-',
  'X' : '-----',
  'Y' : '.....',
  'Z' : '-.--.'
}
#to trans text to morse
def text_to_morse(text):
  return''.join(morse_code_dict.get(char.upper(),'')
for char in text)

#to trans morse to text
def morse_to_text(morse_code):
  return ' '.join(key for key,value in morse_code_dict.items()
       if value == morse_code)

#example
text = input("Enter the text :")
morse_code = text_to_morse(text)
print("Text to morse code: ",morse_code)