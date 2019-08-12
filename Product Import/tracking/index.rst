.. include:: ../../toc_default.txt


Tracking
########

.. include:: toc_tracking.txt

Products in any delivery are processed individually as they journey through the import process. As the product passes certain milestones during the import, an entry is recorded in what is called the "tracking API". As the name suggests, these entries can be used to track the progress of the import (and individual products).

.. image:: emitting.png
	:alt: Emitting Tracking Events

Overview
####
To get the status for your last 100 deliveries use the following endpoint:
https://mis.cdon.com/deliveries
The response will be a json file with a list of the deliveries::
    { 
        "receiptId": "08d71ef5fe115a0800155d4af3d60000",
        "startTime": "2019-08-12T07:23:39.491834+00:00",
        "endTime": "2019-08-12T07:23:40.5525303+00:00",
        "endPoint": "Product",
        "status": "Failed",
        "errorMessage": "1 product(s) failed",
        "totalProducts": 1,
        "totalPending": 0,
        "totalSucceeded": 0,
        "totalFailed": 1
    },
    {
        "receiptId": "08d71ef3a1e2149000155d4af3d60000",
        "startTime": "2019-08-12T07:06:45.8434386+00:00",
        "endTime": null,
        "endPoint": "Product",
        "status": "Pending",
        "errorMessage": null,
        "totalProducts": 1,
        "totalPending": 1,
        "totalSucceeded": 0,
        "totalFailed": 0
    },

The :doc:`receipt <../receipts>` that is given when a delivery has been accepted is the key to retrieve status of the import. By using the tracking API, detailed information is provided to e.g. why a product has not been successfully imported.
