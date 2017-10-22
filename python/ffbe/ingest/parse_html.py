from html.parser import HTMLParser
import requests

class gamepedia_parser(HTMLParser) :
  def __init__(self) :
    HTMLParser.__init__(self)
    self.pf = False
    self.allowed_tags = ['table', 'li']
  def handle_starttag(self, tag, attrs):
    if tag in self.allowed_tags :
      print("Encountered a start tag:", tag)
      self.pf = True
    elif self.pf :
      print("Encountered a start tag:", tag)
  def handle_endtag(self, tag):
    if tag in self.allowed_tags :
      print("Encountered an end tag :", tag)
      self.pf = False
    elif self.pf :
      print("Encountered a end tag:", tag)
  def handle_data(self, data):
    if self.pf :
      if len(data) == 0 :
        print('Empty Data')
      else :
        print("Encountered some data  :", data)

def main() :
  c = gamepedia_parser()
  #c.feed('<html><head><title>Test</title></head>'
  #          '<body><h1>Parse me!</h1></body></html>')
  url = 'https://exvius.gamepedia.com'
  #r = requests.get(url + '/Warrior_of_Light')
  #r = requests.get(url + '/Category:Equipment')
  r = requests.get(url + '/Cotton_Robe')
  c.feed(r.text)

if '__main__' == __name__ :
  main()
