.. include:: ../../toc_default.txt

Tracking
########

Products in any delivery are processed individually as they journey through the import process. As the product passes certain milestones during the import, an entry is recorded in what is called the "tracking API". As the name suggests, these entries can be used to track the progress of the import (and individual products).

.. image:: emitting.png
	:alt: Emitting Tracking Events

API
====
The tracking application can be accessed using a web API. To access the API you must supply an authorization header to identify yourself. Use the same authorization header key as when you submit the products.

The tracking API has 3 endpoints:

Overview
----
::

    https://mis.cdon.com/deliveries


Get the status of your last 100 deliveries. (Latest first)
The response will be a JSON file with a list of the deliveries::
    [
        { 
            "receiptId": "08d71ef5fe115a0800155d4af3d60000",
            "startTime": "2019-08-12T07:23:39.491834+00:00",
            "endTime": "2019-08-12T07:23:40.5525303+00:00",
            "endPoint": "Product",
            "status": "Failed",
            "errorMessage": "1 product(s) failed",
            "total": 1,
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
            "total": 1,
            "totalPending": 1,
            "totalSucceeded": 0,
            "totalFailed": 0
        }
    ]
    
It is also possible to specify how many records you want to return by adding the querystring "take"::
    
    https://mis.cdon.com/deliveries?take=10
    
The maximum supported value is 1000.

Delivery status
----
::

    https://mis.cdon.com/deliveries/<ReceiptId>

Get the status of a specific delivery using the ReceiptId.
The response will be a JSON file with the status of that delivery::
    { 
        "receiptId": "08d71ef5fe115a0800155d4af3d60000",
        "startTime": "2019-08-12T07:23:39.491834+00:00",
        "endTime": "2019-08-12T07:23:40.5525303+00:00",
        "endPoint": "Product",
        "status": "Failed",
        "errorMessage": "1 product(s) failed",
        "total": 1,
        "totalPending": 0,
        "totalSucceeded": 0,
        "totalFailed": 1
    }
    
Product failures
----
::

    https://mis.cdon.com/deliveries/<ReceiptId>/failures

If a delivery has one or more failed products, details of these failures can be viewed using this endpoint.
The response will be a JSON file with a list of the failed products of the specified delivery::
    [
        {
            "productId": "1087760",
            "errorMessage": "Missing required GTIN."
        },
	{
            "productId": "1087761",
            "errorMessage": "Missing required GTIN."
        }
    ]
    
