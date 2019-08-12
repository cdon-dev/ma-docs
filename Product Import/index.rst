.. include:: ../toc_default.txt
.. include:: <isopub.txt>


Overview
########

By exporting your inventory to CDON Marketplace, your products will be added to the CDON product catalog, which makes them available to CDON's customers.

In the CDON Marketplace import process, there are two vital key concepts; **data types** and **receipts**. Deliveries are made by posting different :doc:`types of data <data-types>`, which populate a product with all necessary information. The :doc:`receipt <receipts>` is used to keep track on the progress of the import.

.. image:: overview.png
	:alt: Conceptual Overview

Each delivery is imported independently. When data of all types is available, the final product is assembled and added to the product catalog for presentation.

.. image:: assembly.png
	:alt: Data Assembly


The Import Process
==================

Data in a delivery is passed through a series of sequential steps which make out the import process. During this process, the data is validated and may be modified according to the current business rules.

.. image:: process.png
	:alt: Import Process

Deliveries containing multiple products are split up into individual products, which in turn are imported independently from each other.

.. image:: separation.png
	:alt: Product Separation

Products that fail validation are naturally not imported, but will not abort the entire delivery. Only products whose content has changed (since the last import) will be updated |mdash| unmodified data will be discarded early in the process.

.. caution::
	An inventory import is **greedy**, which means that any and all products that **can** be imported **will** be imported.


.. _product:

The Product
===========

The concept of a *product* is manifested by two types:

Simple Product
	A single, indivisible product, i.e. a "regular" product.

Product with Variations
	Multiple products that are considered "the same", but varies on a specific property.

It is important to understand the distinction between these. A variation product is e.g. a beverage with different flavor variants, or a t-shirt in different sizes, etc. Correctly defining a product makes it easier for the customer to find and buy the product.


Variation Products
------------------

If the product has variations, the "parent" product is called the **model product**.

The model product is the common denominator which attributes shared properties to the variation products and creates the context which relates all variations to each other.

It is not possible to buy the model product, but it invites the customer to decide on one of its variations.



Support
=======

CDON Marketplace has its own customer service that gladly helps you with Marketplace related cases.

When contacting support, please provide the following information when available:

* Merchant ID
* Receipt ID (see :doc:`receipts <receipts>`)

Those details will help giving a more accurate diagnosis with technical matters.
