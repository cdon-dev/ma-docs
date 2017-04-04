.. include:: ../../toc_default.txt


Order Return Address
####################

To use the Delivery Note API you first need to register a return address in the Marketplace admin. Thereafter you can fetch your address ids and use them in the delivery note API call.

Request Example
===============

.. code-block:: none

	 GET https://admin.marketplace.cdon.com/api/returnaddress HTTP/1.1
	 Accept: application/json
	 Authorization: api <apiKey>


Response Example - JSON
=======================

.. code-block:: json

	{
	  "DisplayName": "Display name",
	  "AddressId": "8f8355a0-768f-45cb-b877-aeb5d127c766",
	  "StreetAddress": "SomeStreet 3",
	  "PostalCode": "34450",
	  "City": "Malmö",
	  "Country": "Sweden",
	  "COAddress": null,
	  "BoxAddress": null,
	}


Response Attributes
===================

.. _table-order-response-attributes:

+-----------------------+-------------+-----------------------------------------------------------+
| Variable              | Type        | Description                                               |
+=======================+=============+===========================================================+
| DisplayName           | string      | Display name for the return address.                      |
+-----------------------+-------------+-----------------------------------------------------------+
| AddressId             | guid        | An id which refers to your return address.                |
+-----------------------+-------------+-----------------------------------------------------------+
| StreetAddress         | string      | The street address.                                       |
+-----------------------+-------------+-----------------------------------------------------------+
| PostalCode            | string      | The street postal code your return address resides in.    |
+-----------------------+-------------+-----------------------------------------------------------+
| City                  | string      | The city your return address resides in.                  |
+-----------------------+-------------+-----------------------------------------------------------+
| Country               | string      | The country your return address resides in.               |
+-----------------------+-------------+-----------------------------------------------------------+
| COAddress             | string      | CO address of you return address.                         |
+-----------------------+-------------+-----------------------------------------------------------+
| BoxAddress            | string      | Box address of you return address.                        |
+-----------------------+-------------+-----------------------------------------------------------+
