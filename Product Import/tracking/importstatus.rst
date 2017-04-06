.. include:: ../../toc_default.txt


.. _tracking-import-status:

Import Status
#############

This is the equivalent of the "*is it done yet?*" question.

Since the import process is asynchronous, this query will have to be polled every now and then to eventually get the answer when all products have been processed.

The following endpoint accepts the receipt ID to provide an overall status of that delivery::

	/import/<receiptId>/status

If the delivery cannot be found, the response HTTP status code is `404`_. Otherwise, the code should be `200`_.

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

The most significant property is ``Status`` (line 2, and as an integer for system integration in the property ``StatusCode``), which indicates the current :doc:`import status <importstatuscode>`.

The response also contains static details about the ``Delivery`` (line 6), as well as import progress information (line 13).




.. _200: https://httpstatuses.com/200
.. _404: https://httpstatuses.com/404
