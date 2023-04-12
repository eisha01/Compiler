import xml.etree.ElementTree as ET

mytree = ET.parse('compiler.xml')

id = input("enter id in order to view the atrributes:")

myroot = mytree.getroot()
print(myroot)
print(myroot.tag)
print(myroot[0].tag)






if id == 'bk101':
    for x in myroot[0]:
        print(x.tag,x.attrib)
        print(x.text)

elif id == 'bk102':
    for x in myroot[1]:
        print(x.tag,x.attrib)
        print(x.text)

elif id == 'bk103':
    for x in myroot[1]:
        print(x.tag,x.attrib)
        print(x.text)

elif id == 'bk104':
    for x in myroot[1]:
        print(x.tag,x.attrib)
        print(x.text)

elif id == 'bk105':
    for x in myroot[1]:
        print(x.tag,x.attrib)
        print(x.text)

elif id == 'bk106':
    for x in myroot[1]:
        print(x.tag,x.attrib)
        print(x.text)

elif id == 'bk107':
    for x in myroot[1]:
        print(x.tag,x.attrib)
        print(x.text)

elif id == 'bk108':
    for x in myroot[1]:
        print(x.tag,x.attrib)
        print(x.text)

elif id == 'bk109':
    for x in myroot[1]:
        print(x.tag,x.attrib)
        print(x.text)


elif id == 'bk110':
    for x in myroot[1]:
        print(x.tag,x.attrib)
        print(x.text)


elif id == 'bk111':
    for x in myroot[1]:
        print(x.tag,x.attrib)
        print(x.text)

elif id == 'bk112':
    for x in myroot[1]:
        print(x.tag,x.attrib)
        print(x.text)


else:
    print('enter again')