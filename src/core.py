import xml.etree.cElementTree as ElementTree


def command_new(table):
    print(f'New\t\\\\{table}')
    for x in range(10):
        print('\tAttr = &Attr')
    print('EndNew')


def command_read(table):
    pass


def command_update(table):
    pass


def command_delete(table):
    pass


def command_abm(table):
    command_read(table)
    command_new(table)
    command_update(table)
    command_delete(table)


# TODO: Creates variables and copies them to the clipboard so they can be pasted in GX
def create_var(table):
    pass


def descartes(elements):
    xml = ElementTree.Element('object-definition', libraryName="Dlya.Basic", libraryVersion="1.0", designer="WebUI", designerDate="06/02/2013")
    for element in elements:
        if element == 'form':
            ElementTree.SubElement(xml, 'form')
        if element == '':
            pass
    xml_tree = ElementTree.ElementTree(xml).write('xml.xml')
