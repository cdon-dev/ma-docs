.. include:: ../../toc_default.txt


Product Data Type
#################

The product data type is the information that describes the product and specifies feature values. Some of this data will be published to customers while other data is metadata for controlling product behavior once published.

To reduce the quantity of imported data, products whose content has not changed since the last successful import will be discarded automatically.

The URL to post product data to is::

	http://import.api.marketplace.cdon.com/product


Product Definition
==================

A vital concept with this data is that it represents a **complete product definition**. Each product must be delivered in its entirety, meaning there cannot be any partial product updates. The product data must thus, in each delivery, contain all data to fully describe it, lest the product will be redefined with a lesser definition.

In practice, this means that, for example, it is not possible to update only e.g. the title of a product. That would obliterate all category- and variation related data.


Data Contract
=============

The relevant schema files are the following:

* product.xsd
* types.xsd
* categories.xsd
* attributes.xsd
* variants.xsd

The last four files are supplements to the product.xsd, which define the overall product data structure.


Category
========
The category defines what attributes that describe the product.

A product must belong to exactly one category.


Variants
========

Some products may exist in different variants. Valid variables are:

* Size
* Color
* Flavor
* Size and Color combined
* Size and Flavor combined

Within the same product, all variants must be of the same variable(s), meaning a single product cannot have one variant that varies on e.g. *flavor*, and another variant that varies on e.g. *size and color*.


Sanitization
============

Textual data that will be published to end-users will be sanitized. HTML- and other scripting code as well as foul language will be removed.
