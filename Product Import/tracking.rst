Tracking
########

Products in any delivery are processed individually as they journey through the import process. As the product passes certain milestones during the import, an entry is recorded in what is called the "tracking API". As the name suggests, these entries can be used to track the progress of the import (and individual products).

The :doc:`receipt <receipts>` that is given when a delivery has been accepted is the key to retrieve status of the import, but also to examine what events have passed for each product. By using the tracking API, detailed information is provided to e.g. why a product has not been successfully imported.

The URL to the tracking-API is::

	http://tracking-import.api.marketplace.cdon.com


.. _tracking-import-status:
Import Status
=============

This is the equivalent of the "*is it done yet?*" question.

Since the import process is asynchronous, this query will have to be polled every now and then to eventually get the answer when all products have been processed.

The following endpoint accepts the receipt ID to provide an overall status of that delivery::

	/import/<receiptId>/status

If the delivery cannot be found, the response HTTP status code is `404`_. Otherwise, the code should be `200`_.

The response body may look similar to this:

.. code-block:: json
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


The most significant property is ``Status`` (line 2), which indicates the current import status.

.. _table-import-status:
.. table:: Import Statuses

+-----------------------+-------------+-----------------------------------------------+--------------------+
| Status                | Status Code | Description                                   | Processing Started |
+=======================+=============+===============================================+====================+
| NoContent             | 1           | The delivery was empty.                       | No                 |
+-----------------------+-------------+-----------------------------------------------+--------------------+
| Receiving             | 2           | The delivery is still being received.         | Yes                |
+-----------------------+-------------+-----------------------------------------------+--------------------+
| IngestionFailure      | 3           | Something went wrong when receiving the       | Yes                |
|                       |             | delivery. This is also indicated by the HTTP  |                    |
|                       |             | status code `500`_.                           |                    |
+-----------------------+-------------+-----------------------------------------------+--------------------+
| Queued                | 4           | All data has been received, but processing    | No                 |
|                       |             | has not yet started.                          |                    |
+-----------------------+-------------+-----------------------------------------------+--------------------+
| Processing            | 5           | Processing has begun, and there are still     | Yes                |
|                       |             | products to process.                          |                    |
+-----------------------+-------------+-----------------------------------------------+--------------------+
| CompletedSuccessfully | 6           | All products have been successfully imported! | Yes                |
+-----------------------+-------------+-----------------------------------------------+--------------------+
| CompletedWithErrors   | 7           | All products have been processed, but some    | Yes                |
|                       |             | (or all) failed to be imported.               |                    |
+-----------------------+-------------+-----------------------------------------------+--------------------+

Statuses marked with *Processing Started* indicate that there **may** be products which have been processed.

The response also contains static details about the ``Delivery`` (line 6), as well as import progress information (line 13).


.. _tracking-import-summary:
Import Summary
==============

The summary will list all products in the delivery, with a brief status of each product's progress. The foremost reason to use this endpoint is to gain swift access to what products have failed.

The following endpoint accepts the receipt ID to provide a summary of that delivery::

	/import/<receiptId>/summary


If the delivery cannot be found or the data has not yet been received, the response HTTP status code is `404`_. Otherwise, the code should be `200`_.

The response body may look similar to this:

.. code-block:: json
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

As seen above, the response contains a list of products, in which the ``Status`` (line 15) property is the most significant.

.. _table-import-summary:
.. table:: Product Statuses

+-----------------------+-------------+-----------------------------------------------+
| Status                | Status Code | Description                                   |
+=======================+=============+===============================================+
| Queued                | 1           | Still waiting to be imported.                 |
+-----------------------+-------------+-----------------------------------------------+
| Processing            | 2           | The import process is ongoing for this        |
|                       |             | product.                                      |
+-----------------------+-------------+-----------------------------------------------+
| Imported              | 3           | The product has been successfully imported!   |
+-----------------------+-------------+-----------------------------------------------+
| PartiallyImported     | 4           | Some of the data has been imported and others |
|                       |             | has been discarded.                           |
+-----------------------+-------------+-----------------------------------------------+
| Failed                | 5           | This product has been rejected for some       |
|                       |             | reason.                                       |
+-----------------------+-------------+-----------------------------------------------+

The product element also contains two more vital properties: ``TrackingId`` (line 17) and ``TrackingCode`` (line 18).

The *TrackingId* is the unique identifier for this particular event, whereas the *TrackingCode* is a code identifying the event type (similar to an error code). Please make sure to provide these two properties if contacting support, as they help pin-point the exact event and reason for something going wrong.


.. _tracking-product-details:
Product Details
===============

It is possible to retrieve the full tracking history for a product in a specific delivery. The purpose would be to in detail examine a product's journey through the import process to be able to identify the reason for a rejection and amend the data.

The following endpoint accepts the receipt ID and the product ID to provide a detailed description of that product in that delivery::

	/import/<receiptId>/<productId>


If the delivery cannot be found or no events have been recorded for that particular product, the response HTTP status code is `404`_. Otherwise, the code should be `200`_.

The response body may look similar to this:

.. code-block:: json
	:emphasize-lines: 4,5

	[
	  {
	    "Timestamp": "2017-12-24T14:00:00.0000000Z",
	    "TrackingId": "11c80f46f423431692c5291b997116a6",
	    "TrackingCode": 1383146305,
	    "ReceiptId": "00b24f3a93124da7aec34447124e5aa1",
	    "MerchantId": "3ff7cdd47fe243d48e12ff62a1215a87",
	    "ProductId": "product_a",
	    "ChannelId": null,
	    "Message": "Business constraint violation",
	    "DebugInformation": null
	  }
	]

As seen above, the response is an array of events (shortened here for brevity). Notice that ``TrackingId`` (line 4) and ``TrackingCode`` (line 5) are the same properties as in the :ref:`import-summary`.




.. _200: https://httpstatuses.com/200
.. _404: https://httpstatuses.com/404
.. _500: https://httpstatuses.com/500


.. highlight:: json
	:linenothreshold: 5
