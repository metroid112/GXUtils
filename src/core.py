import xml.etree.cElementTree as ElementTree


def command_new(table):
    print(f'New\t\\\\{table}')
    for x in range(10):
        print('\tAttr = &Attr')
    print('EndNew')


def descartes(elements):
    xml = ElementTree.Element('object-definition', libraryName="Dlya.Basic", libraryVersion="1.0", designer="WebUI", designerDate="06/02/2013")
    for element in elements:
        if element == 'form':
            ElementTree.SubElement(xml, 'form')
    xml_tree = ElementTree.ElementTree(xml).write('xml.xml')
