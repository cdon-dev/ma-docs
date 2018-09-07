Product Data Type
#################

The product data type is the information that describes the product and specifies feature values. Some of this data will be published to customers while other data is metadata for controlling product behavior once published.

To reduce the quantity of imported data, products whose content has not changed since the last successful import will be discarded automatically.

The URL to post product data to is::

	https://productimport.cdon.com/product


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


Product Size and Weight
=======================

The :code:`Dimensions` property of a product describe the product's size and weight.

Spatial Dimensions
******************

.. _table-product-size:
============ ========== ============================================
Abbreviation Unit       Comment
============ ========== ============================================
um           micrometre
µm           micrometre The same as 'um', but with the greek letter.
mm           millimetre
cm           centimetre
dm           decimetre
m            metre
km           kilometre
in           inch       0.0254 metres
ft           foot       0.3048 metres
yd           yard       0.9144 metres
============ ========== ============================================

Mass Dimensions
***************

.. _table-product-mass:
============ ============ ============================================
Abbreviation Unit         Comment
============ ============ ============================================
mcg          microgram
µg           microgram    The same as 'mcg', but with the greek letter.
mg           milligram
g            gram
hg           hectogram
kg           kilogram
t            metric tonne Equivalent to a 1000 kilograms
gr           grain        0.06479891 grams
oz           ounce        28.349523125 grams
lb           pound        453.59237 grams
============ ============ ============================================

Energy Classification
=====================

Energy :code:`Energy` property of a product describe the energy classification.
The energy property consists of four parts specified as tags.

The energy classification property is optional, however to determine which products that **should** include energy classifications, or to 
read further regarding energy classification, please visit https://europa.eu/youreurope/business/environment/energy-labels/index_en.htm.

Energy Properties
*****************
.. _table-product-energy:
============= =========== ===================================
Property name Data type   Description
============= =========== ===================================
class         energyClass Energy class enumeration
label         URL         Energy label
arrow         URL         Energy arrow
sheet         URL         Energy sheet ( aka Fische )
============= =========== ===================================

Energy Classes Enumeration
**************************

Accepted values for :code:`energyClass` is:

* APlusPlusPlus     
* APlusPlus         
* APlus             
* A                 
* B                 
* C                 
* D                 
* E                 
* F                 
* G                 

Sanitization
============

Textual data that will be published to end-users will be sanitized. HTML- and other scripting code as well as foul language will be removed.
