.. include:: ../../toc_default.txt


API
###

Deliveries are made to Marketplace by posting **XML**-formatted data to the endpoint for the corresponding :doc:`data type <../data-types>`.

Responses are returned with a HTTP status code and possibly a body in **JSON**-format.

Each delivery that is acceptable (according to the data contract) receives a :doc:`receipt <../receipts>`. Make sure to store this, as it is the key to :doc:`tracking <../tracking/index>` the progress of the delivery.


Authentication
==============

For security reasons, all HTTP requests to the API must include a :code:`Authorization` header.

The value of the header shall be the API token, prefixed by the word :code:`api` and a whitespace. Example:

.. code-block:: code

	Authorization: api 5875ca6c-229d-4f4c-a45f-4252b4583538




Data Contracts
==============

As mentioned in :doc:`validation <../validation>`, a pre-validation is performed on the delivery. This validation is based on a data contract specified in a set of :abbr:`XSD (XML Schema Definition)` files.

The location of the schema files is:

https://schemas.cdon.com/product/4.0/

Use these files to generate XML and validate against them to avoid submitting invalid data.


.. toctree::
	:hidden:
	:maxdepth: 1
	:caption: Data Types

	product
	price
	availability
	media
