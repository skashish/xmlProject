from pathlib import Path
import xml.etree.ElementTree as ET
import hashlib
import string

def xml_dir(pth, et_element=None):

    if et_element is None:
        et_element = ET.Element(pth.name)
    else:
        et_element = ET.SubElement(et_element, pth.name)

    for file in (fle for fle in sorted(pth.iterdir()) if fle.is_file()):
        complete_file_name = 'file name = "'  + file.name + '" hash = "' + md5(str(file)) + '"'
        ET.SubElement(et_element, complete_file_name)

    for directory in (fle for fle in sorted(pth.iterdir()) if fle.is_dir()):
        xml_dir(directory,et_element)

    return(et_element)

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def xml_output(path_of_dir):
    ret = xml_dir(Path(path_of_dir))
    indent(ret)
    strg = ET.tostring(ret, method='xml').decode()
    return(strg)

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return(hash_md5.hexdigest())
   
    
