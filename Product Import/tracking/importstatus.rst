.. include:: ../../toc_default.txt


.. _tracking-import-status:

Import Status
#############

This is the equivalent of the "*is it done yet?*" question.

The **import status** is an aggregate of the status of **all** products in the delivery.

Since the import process is asynchronous, this query will have to be polled every now and then to eventually get the answer when all products have been processed.


Request
=======

The following endpoint accepts the receipt ID to provide an overall status of that delivery::

	/import/<receiptId>/status

The following HTTP status codes can be expected:

* `200`_, accompanied with the response body described below
* `404`_, when the delivery cannot be found


Response
========

The response body may look similar to this:

.. code-block:: json
	:linenos:
	:emphasize-lines: 2

	{
	  "Status": "Processing",
	  "StatusCode": 5,
	  "CompletedUtc": null,
	  "EstimatedCompletionUtc": null,
	  "Delivery": {
	    "AcceptedUtc": "2017-12-24T14:00:00.0000000Z",
	    "Data": "Product",
	    "ContractVersion": "1.0",
	    "MerchantId": "3ff7cdd47fe243d48e12ff62a1215a87",
	    "ForeignKey": null
	  },
	  "Products": {
	    "Successful": 3,
	    "Pending": 2,
	    "Failed": 1
	  }
	}

The most significant property is ``Status`` (line 2), which indicates the current overall **import status**.
It is also reflected as the integer in the property ``StatusCode`` (line 3) to facilitate system integration.
These two properties are populated by a value from the :doc:`import status enumeration <importstatuscode>`.

The response also contains static details about the ``Delivery`` (line 6), as well as import progress information (line 13).




.. _200: https://httpstatuses.com/200
.. _404: https://httpstatuses.com/404
