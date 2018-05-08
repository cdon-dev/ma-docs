.. include:: ../toc_default.txt


Product Identities
##################

The product identifier is the key that correlates all product data from different types.

All four :doc:`data types <data-types>` specify the product key by using the element :code:`id`.



Model Product and Variations
============================

The *model product* (see :ref:`product`) must always have its own **unique** key, regardless of whether it has any variations or not.

If the product has any variations, each variation is obligated to have its own unique product key.

A variation product cannot be redefined to later map to a different model product. 

.. ATTENTION::
	No check will be done to identify duplicate (and possibly conflicting) product identities. It is the merchant's responsibility to maintain data consistency in regards of product identities.

For the product data types :doc:`availability <api/availability>`, :doc:`media <api/media>` and :doc:`price <api/price>`, data associated with the model product's key is discarded if the product has variations.



The Product Data Type
=====================

The :doc:`product data type <api/product>` has encapsulated the :code:`<id>` element inside an :code:`<identity>`-element.

.. code-block:: xml

	<identity>
	  <id>main_product_key</id>
	  <gtin>global_trade_item_number</gtin>
	  <mpn>manufacturer_part_number</mpn>
	  <sku>stock_keeping_unit</sku>
	  <pickingLocation>Location in warehouse, etc.</pickingLocation>
	</identity>

The :code:`id`-element is always **mandatory**.
The other elements, :code:`gtin`, :code:`mpn`, :code:`sku` and :code:`pickingLocation` are product data that is **not** used for identification during processing, but are persisted if provided.

.. ATTENTION::
	Except for the :code:`id`-element, the identifiers are primarily optional. However, certain categories require one or more of them, which will be enforced during processing.



Case Insensitive
================

Note that product id:s are **not case sensitive**! For example, the following id:s are all considered equal::

	Product_A
	product_a
	PRODUCT_A
	pRoDuCt_A



Valid Identity Characters
=========================

A valid product key is 1 |--| 40 characters long, and only accepts certain characters.

The following characters are allowed in an identity token:

* a-z
* A-Z
* 0-9
* \\ (backslash)
* \- (hyphen)
* \_ (underscore)

If specified, the element :code:`gtin` must be exactly either 8, 12, 13 or 14 digits long. For reference, see `gtin.info <http://www.gtin.info/>`_.

The restrictions are more lenient for the elements :code:`mpn`, :code:`sku` and :code:`pickingLocation`. If specified, 1 |--| 50 characters of any kind is permitted.



.. |--| unicode:: U+2013  .. en dash, trimming surrounding whitespace
   :trim:
