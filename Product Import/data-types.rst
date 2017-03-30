##########
Data Types
##########

In order to present a complete and buyable product to CDON's customers, four distinct types of data are required:

* :doc:`Product Description <api/product>`
* :doc:`Price <api/price>`
* :doc:`Availability <api/availability>`
* :doc:`Media <api/media>`

These four types of data are fully independent from each other in the context of importing the data. In most cases, they also have different life cycles. Depending on your business, some data is shorter lived and require more frequent updates than other data. This enables a more flexible delivery with faster imports.

Although the data is separate from each other, all four types of data are constituents necessary to form a complete product. If any type is missing, the product will be **unavailable** until all product data requirements have been met. When all data is available, it will be compiled into a final product.


*************
Data Contract
*************

To facilitate a structured delivery of data, each set of data must fulfill a **data contract** that specify the structure of the data, expected data types and mandatory fields. If this contract is not met, the import process is unable to accept the data. The contracts are publicly available and can also be used as an acceptance test on the delivery before transmitting it to CDON Marketplace.


**********
Identities
**********

The product ID is the key that correlates all product data from different types.

Note that product IDs are **not case sensitive**, and only accepts certain characters. For example, the following IDs are all considered equal::

	Product_A
	product_a
	PRODUCT_A
	pRoDuCt_A


.. ATTENTION::
	No check will be done to identify duplicate (and possibly conflicting) product identities. It is the merchant's responsibility to maintain data consistency in regards of product identities.


Valid Identity Characters
=========================

The following characters are allowed in an identity token:

* a-z
* A-Z
* 0-9
* \\ (slash)
* \- (hyphen)
* \_ (underscore)

A valid product ID is 1 |--| 40 characters long.


.. |--| unicode:: U+2013  .. en dash, trimming surrounding whitespace
   :trim:
