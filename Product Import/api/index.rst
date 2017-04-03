.. include:: ../../toc_default.txt


Integration
###########

Deliveries are made to Marketplace by posting **XML**-formatted data to the endpoint for the corresponding :doc:`data type <../data-types>`.

Responses are returned with a HTTP status code and possibly a body in **JSON**-format.

Each delivery that is acceptable (according to the data contract) receives a :doc:`receipt <../receipts>`. Make sure to store this, as it is the key to :doc:`tracking <../tracking>` the progress of the delivery.


Endpoints
=========

The base URL for the imports is as follows::

	http://import.api.marketplace.cdon.com

Append the name of the data type like so::

	http://import.api.marketplace.cdon.com/product
	http://import.api.marketplace.cdon.com/price
	http://import.api.marketplace.cdon.com/availability
	http://import.api.marketplace.cdon.com/media


Data Contracts
==============

As mentioned in :doc:`validation <../validation>`, a pre-validation is performed on the delivery. This validation is based on a data contract specified in a set of :abbr:`XSD (XML Schema Definition)` files.

The location of the schema files is:

http://schemas.cdon.com/marketplace/

Use these files to generate XML and validate against them to avoid submitting invalid data.
