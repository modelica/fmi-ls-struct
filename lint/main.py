# validate the examples in the docs folder

from lxml import etree
from pathlib import Path
from fmpy import read_model_description

for filename in Path("../docs/examples").glob("*modelDescription.xml"):
    print(f"Parsing '{filename}'...")
    read_model_description(str(filename))

for filename in Path("../docs/examples").glob("*terminalsAndIcons.xml"):
    print(f"Parsing '{filename}'...")
    schema = etree.XMLSchema(file="fmi3TerminalsAndIcons.xsd")
    root = etree.parse(filename)
    assert schema.validate(root), f"Validation failed: {schema.error_log}"
