
from xml.dom.minidom import parse, parseString
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'hello.xml'));

dom = parse(f)  # parse an open file


print(__location__)
print(__file__)
print(os.path.realpath(__file__))
print(os.getcwd())



print(dom.toxml())