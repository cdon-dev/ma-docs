Price Data Type
###############

The price data type specifies pricing details for a product. Every product must have price information for every market it will be sold in. This also includes VAT and shipping rates.

This data type is incremental, which means that any data that can be applied will be applied without altering related data. Hence, it is possible to import just the updates as soon as they are available.

The URL to post price data to is::

	http://import.api.marketplace.cdon.com/price


Data Contract
=============

The relevant schema files are the following:

* price.xsd
* types.xsd

The last file is a supplement to the price.xsd, which define the price data structure.


Validation Rules
================

The sale price may not be greater than the recommended price.


Price
=====

The product price consists of two price values; **recommended** and **sale** price.

The *recommended* price represents the `list price`_.

The *sale* price represents the price that the product is up for sales for.

Please note that the prices must include VAT.


VAT
===

The VAT is percentage represented by a decimal number between 0 and 1 with up to three decimals.

**Example**::

 	0.125

which represents 12.5%.


Shipping Rates
==============

The following shipping rates are allowed:

.. _table-shipping-rates:
.. table:: Valid Shipping Rates

====== ======= ====== =======
Sweden Denmark Norway Finland
====== ======= ====== =======
0      0       0      0
19.00  19.00   19.00  1.95
29.00  29.00   29.00  2.95
39.00  39.00   39.00  3.95
49.00  49.00   49.00  4.90
59.00  59.00   59.00  4.95
79.00  79.00   79.00  5.95
99.00  99.00   99.00  7.95
199.00 199.00  399.00 9.95
N/A    N/A     799.00 59.00
====== ======= ====== =======



.. _list price: https://en.wikipedia.org/wiki/List_price
