Price Data Type
###############

The price data type specifies pricing details for a product. Every product must have price information for every market it will be sold in. This also includes VAT and shipping rates.

This data type is incremental, which means that any data that can be applied will be applied without altering related data. Hence, it is possible to import just the updates as soon as they are available.

The URL to post price data to is::

	https://mis.cdon.com/price


Data Contract
=============

The relevant schema files are the following:

* price.xsd
* types.xsd

The last file is a supplement to the price.xsd, which define the price data structure.


Validation Rules
================

The sale price may not be greater than the original price.


Price
=====

The product price consists of two price values; **original** and **sale** price.

* The ``OriginalPrice`` represents the `list price`_.
* The ``SalePrice`` represents the price that the product is up for sales for.

Please note that the prices must include VAT.


VAT
===

The ``Vat`` allows different values depending on VAT rates in the market where the products are being sold. The value is expressed as a percentage.

**Example**::

 	12

which represents a VAT of 12%.


Shipping Costs
==============

The ``ShippingCost`` allow the follwing values:

.. _table-shipping-rates:

====== ======= ====== =======
Sweden Denmark Norway Finland
====== ======= ====== =======
0      0       0      0
19     19      19     1.95
29     29      39     2.95
39     39      49     3.95
49     49      59     4.90
59     59      79     4.95
79     79      99     5.95
99     99      399    7.95
199    199     799    9.95
395    495     995    59.00
495    N/A     N/A    79.00
====== ======= ====== =======



.. _list price: https://en.wikipedia.org/wiki/List_price
