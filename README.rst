parsedocinfo
******************

``parsedocinfo`` reads an rST file to find
docinfo `field lists`__ and writes them out
as a key-value pair in a JSON list like this:

..  code-block:: javascript

    [["<field1_key>", "<field1_value>"],
    ["<field2_key>", "<field2_value>"],
    //...
    ]

__ https://www.sphinx-doc.org/en/master/usage/restructuredtext/field-lists.html

Usage
=========

..  code-block:: shell

    python parsedocinfo --input input_file.rst --output output_file.json

Example
===============

Running ``parsedocinfo`` on the following rST content:

..  code-block:: rst

    :title: This is a title
    :status: Pending
    :date: 2021-08-13T004152

Produces JSON like this:

..  code-block:: javascript

    [["title", "This is a title"],
    ["status": "Pending"],
    ["date": "2021-08-13T004152"]]

