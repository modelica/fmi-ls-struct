# validate the examples in the docs folder

from lxml import etree
from pathlib import Path
from fmpy import read_model_description

ORDERING_CONSTRAINT_TYPE = "org.fmi-standard.fmi-ls-struct.orderingConstraint"
ORDERING_CONSTRAINT_VALUES = {
    "unordered",
    "decreasing",
    "increasing",
    "strictlyIncreasing",
    "strictlyDecreasing",
}

for filename in Path("../docs/examples").glob("*modelDescription.xml"):
    print(f"Parsing '{filename}'...")
    read_model_description(str(filename))

for filename in Path("../docs/examples").glob("*terminalsAndIcons.xml"):
    print(f"Parsing '{filename}'...")
    schema = etree.XMLSchema(file="fmi3TerminalsAndIcons.xsd")
    root = etree.parse(filename)
    assert schema.validate(root), f"Validation failed: {schema.error_log}"
    for member in root.xpath("//TerminalMemberVariable"):
        annotations = member.xpath(
            f"./Annotations/Annotation[@type='{ORDERING_CONSTRAINT_TYPE}']"
        )
        assert len(annotations) <= 1, (
            f"At most one {ORDERING_CONSTRAINT_TYPE} annotation is allowed "
            f"for '{member.get('variableName')}'"
        )
        if annotations:
            annotation = annotations[0]
            value = (annotation.text or "").strip()
            assert value in ORDERING_CONSTRAINT_VALUES, (
                f"Invalid ordering constraint '{value}' for "
                f"'{member.get('variableName')}'"
            )
            assert len(annotation) == 0, (
                f"The {ORDERING_CONSTRAINT_TYPE} annotation must contain text only "
                f"for '{member.get('variableName')}'"
            )
