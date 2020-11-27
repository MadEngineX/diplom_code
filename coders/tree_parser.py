def parse_tree(filename):
    import xml.etree.ElementTree as ET
    tree = ET.parse(filename)
    root = tree.getroot()
    a = []
    a1 = ''
    a2 = ''
    for child_of_root in root:
        for child_of_root2 in child_of_root:
            for child_of_root3 in child_of_root2:
                for child_of_root4 in child_of_root3:
                    for child_of_root5 in child_of_root4:
                        #print(child_of_root.text())
                        print(child_of_root.attrib)
                        a1 = str(child_of_root.attrib) + \
                             str(child_of_root2.attrib) +\
                             str(child_of_root3.attrib) + \
                             str(child_of_root4.attrib) + \
                             str(child_of_root5.attrib)
                        # a2 = str(child_of_root.items()['value']) + \
                        #      str(child_of_root2.items()) +\
                        #      str(child_of_root3.items()) + \
                        #      str(child_of_root4.items()) + \
                        #      str(child_of_root5.items())
                        a.append(a1)
                        a.append(a2)
                        # print('a1 ' + a1)
                        # print('a2 ' + a2)
    print(root[0][1].text)
    return a

print(parse_tree('viterby_tree.xml'))


