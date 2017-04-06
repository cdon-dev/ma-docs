.. include:: ../../toc_default.txt


.. _tracking-import-summary:

Import Summary
##############

The summary will list all products in the delivery, with a brief status of each product's current progress. The foremost reason to use this endpoint is to gain swift access to what products have failed.


Request
=======

The following endpoint accepts the receipt ID to provide a summary of that delivery::

	/import/<receiptId>/summary

The following HTTP status codes can be expected:

* `200`_, accompanied with the response body described below
* `404`_, when the delivery cannot be found, or the data has not yet been received


Response
========

The response body may look similar to this:

.. code-block:: json
	:linenos:
	:emphasize-lines: 15,17,18

	{
	  "IsComplete": false,
	  "CompletedUtc": null,
	  "EstimatedCompletionUtc": null,
	  "Delivery": {
	    "AcceptedUtc": "2017-12-24T14:00:00.0000000Z",
	    "Data": "Product",
	    "ContractVersion": "1.0",
	    "MerchantId": "3ff7cdd47fe243d48e12ff62a1215a87",
	    "ForeignKey": null
	  },
	  "Products": [
	    {
	      "ProductId": "product_a",
	      "Status": "Failed",
	      "StatusCode": 4,
	      "TrackingId": "2f9c550141a5483c837d3c8373a1e93f",
	      "TrackingCode": 1383146305,
	      "Description": "Business constraint violation"
	    }
	  ]
	}

As seen above, the response contains a list of products, in which the ``Status`` (line 15) property is the most significant. It indicates the current **product status**.
It is also reflected as the integer in the property ``StatusCode`` (line 16) to facilitate system integration.
These two properties are populated by a value from the :doc:`product status enumeration <productstatuscode>`.

.. tip::
	The product element also contains two more vital properties: ``TrackingId`` (line 17) and ``TrackingCode`` (line 18).

	The *TrackingId* is the unique identifier for this particular event, whereas the *TrackingCode* is a code identifying the event type (similar to an error code). Please make sure to provide these two properties if contacting support, as they help pin-point the exact event and reason for why something has occurred.




.. _200: https://httpstatuses.com/200
.. _404: https://httpstatuses.com/404
