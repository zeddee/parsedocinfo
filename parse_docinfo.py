from collections import namedtuple
from docutils.core import publish_doctree
from xml import dom
from sys import stdout
from typing import List

DocInfo = namedtuple("DocInfo", 'name body')


def _traverse_docinfo(docinfo_list: List) -> List[DocInfo]:
    """

    """
    out = []
    for i in docinfo_list:
        for node in i.childNodes:
            if node.tagName == "field":
                out.append(_traverse_fields(node))
            else:
                out.append(
                  DocInfo(
                    node.tagName,
                    " ".join(val.nodeValue for val in node.childNodes),
                  )
                )

    return out


def _traverse_fields(field: List) -> DocInfo:

    field_name = field.getElementsByTagName("field_name")[0]
    field_body = field.getElementsByTagName("field_body")[0]

    return DocInfo(
              field_name.firstChild.nodeValue,
              " ".join(val.firstChild.nodeValue for val in field_body.childNodes),
              )


def parse(data: str) -> List[DocInfo]:
    docinfo = publish_doctree(data).asdom().getElementsByTagName("docinfo")

    return _traverse_docinfo(docinfo)
