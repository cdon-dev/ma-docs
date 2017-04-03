########
Overview
########

When a customer buys something on CDON the order is saved, and sent to your specific Marketplace account (merchant account). It is your responsibility to handle the orders that have been delivered to your Merchant account. This can be done by either using the Marketplace Admin or by using the API Integration. There are greater benefits by integrating as your own employees will have fewer systems to work with but it requires an integration.

The Marketplace support team can aid you if you have specific questions. We also have integration partners that have built modules for quite a few e-commerce platforms.


Error Codes
===========

Marketplace order API returns reponse codes to indicate what failed in your specific call to the order API. Unsuccessful responses (HTTP status code 400) return details about the error as an response object containing the following information:

.. _table-order-error-codes:
.. table:: Order Error Codes

+-----------------------+-------------+----------------------------------------------------+
| Key                   | Value Type  | Value Description                                  |
+=======================+=============+====================================================+
| ErrorCode             | integer     | An internal status code that represents the error. |
+-----------------------+-------------+----------------------------------------------------+
| Message               | string      | A short description of the error.                  |
+-----------------------+-------------+----------------------------------------------------+

The response body looks like this:

.. code-block:: json

	{
	  "ErrorCode": 1000,
	  "Message": "Order does not exist"
	}
	


The list of ``internal`` response codes is as follows:

.. _table-order-error-codes:
.. table:: Order Error Codes

+-------------+----------------------------------------------------------------------+
| ErrorCode   | Description                                                          |
+=============+======================================================================+
| 1000        | The order was not found.                                             |
+-------------+----------------------------------------------------------------------+
| 1001        | The order row was not found.                                         |
+-------------+----------------------------------------------------------------------+
| 1002        | Order row overflow.                                                  |
+-------------+----------------------------------------------------------------------+
| 1003        | Negative order row price.                                            |
+-------------+----------------------------------------------------------------------+
| 1004        | The order already exists.                                            |
+-------------+----------------------------------------------------------------------+
| 1005        | The package carrier does not exist.                                  |
+-------------+----------------------------------------------------------------------+
| 1006        | The order row is not in a valid state for the command.               |
+-------------+----------------------------------------------------------------------+
| 1008        | The same order row occurs multiple times in the same command.        |
+-------------+----------------------------------------------------------------------+
| 1009        | No rows were specified in the command.                               |
+-------------+----------------------------------------------------------------------+
| 2001        | Invoice row overflow.                                                |
+-------------+----------------------------------------------------------------------+
| 2002        | No rows to invoice.                                                  |
+-------------+----------------------------------------------------------------------+
| 3001        | Value of returned products is not high enough to charge for NPU.     |
+-------------+----------------------------------------------------------------------+
| 3002        | At least one order row must be marked as returned to charge for NPU. |
+-------------+----------------------------------------------------------------------+
| 3003        | Can not charge for NPU more than once.                               |
+-------------+----------------------------------------------------------------------+
| 3004        | Returned order row must have been sent with package id.              |
+-------------+----------------------------------------------------------------------+
| 3005        | There is no NPU charge to retract.                                   |
+-------------+----------------------------------------------------------------------+

