"""
Simple main method calling our function.
"""
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'get_interfaces.xml'));

print(f)

interfaces = get_configured_interfaces(f)
interfaces = xml.dom.minidom.parseString(interfaces.xml)
interfaces = interfaces.getElementsByTagName("interfaces")
print(interfaces[0].toprettyxml())
