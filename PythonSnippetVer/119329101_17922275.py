import xml.etree.ElementTree as ET


xml = """<?xml version="1.0" encoding="UTF-8"?>
<body>
    <approved-by approved="no">
        <name>AB</name>
        <signature>errrrrn</signature>
    </approved-by>
</body>
"""

tree = ET.fromstring(xml)
sh = tree.find('approved-by')
sh.set('approved', 'yes')

print ET.tostring(tree)