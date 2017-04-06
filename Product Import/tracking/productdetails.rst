.. include:: ../../toc_default.txt


.. _tracking-product-details:

Product Details
===============

It is possible to retrieve the full tracking history for a product in a specific delivery. The purpose would be to in detail examine a product's journey through the import process to be able to identify the reason for a rejection and amend the data.

The following endpoint accepts the receipt ID and the product ID to provide a detailed description of that product in that delivery::

	/import/<receiptId>/<productId>


If the delivery cannot be found or no events have been recorded for that particular product, the response HTTP status code is `404`_. Otherwise, the code should be `200`_.

The response body may look similar to this:

.. code-block:: json
	:linenos:
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

As seen above, the response is an array of events (shortened here for brevity). Notice that ``TrackingId`` (line 4) and ``TrackingCode`` (line 5) are the same properties as in the :ref:`tracking-import-summary`.




.. _200: https://httpstatuses.com/200
.. _404: https://httpstatuses.com/404
