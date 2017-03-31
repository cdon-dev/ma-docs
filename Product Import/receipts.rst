Receipts
########

Importing products to CDON Marketplace is an asynchronous process, meaning that it is not instantaneous. When you deliver data to the API, a **receipt** will be issued as soon as the data has been pre-validated and accepted.

Example of a receipt:

.. code-block:: json

	00b24f3a93124da7aec34447124e5aa1

The receipt is a unique 32-character long string associated with a **single** delivery.

The receipt means that the data has been received and that the import will start as soon as possible. Since the actual import may take a long time (depending of the size and current workload), the receipt is intended to be used to inquire about the current status of that particular import at a later moment.

.. IMPORTANT::
	A receipt in the delivery response does **not** mean that any products have been imported |---| the receipt is only an acknowledgement that the delivery has been received and accepted.

The asynchronous process has several benefits:

* A response is generated as soon as the data is received.

  There is no need to wait for the entire import to complete.

* The import is more error resilient.

  Errors and warnings will be tracked and handled to have as small impact as possible on the rest of the import.

* Multiple imports can be enqueued in parallel.

  The four different types of data can be imported simultaneously.

* Detailed per-product results can be retrieved.

  Each failed product can be examined and diagnosed in detail, and amended individually without affecting any other part of the import process.

.. IMPORTANT::
 	Take note that the asynchronous import also implies that there will **not** be any notification when the import has completed. Thus, it is important that you save the receipt for future use.


.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
