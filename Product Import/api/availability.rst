Availability Data Type
######################

The availability data type specifies details regarding stock, delivery times, etc.

Every product must specify the availability status for each market, as well as the expected delivery time range. The intention is to give the customer an as accurate estimation as possible of when the product will be delivered.

.. ATTENTION::
	Products with the status ``offline`` will **not** be buyable.

This data type is incremental, which means that any data that can be applied will be applied without altering related data. Hence, it is possible to import just the updates as soon as they are available.

The URL to post availability data to is::

	https://productimport.cdon.com/availability


Data Contract
=============

The relevant schema files are the following:

* availability.xsd
* types.xsd

The last file is a supplement to the availability.xsd, which define the availability data structure.


Validation Rules
================

The delivery time is a range in number of days, where the minimum value may not be greater than the maximum value.


Stock
=====

The :code:`Stock` value represents the number of products to be imported to CDON:s product catalog.

Regarding services, digital products or other products with **unlimited stock value**, the imported value has to be very high (but not higher than a signed 32-bit integer) so that the product do not run out of stock due to no stock updates.


Will The Product Be Buyable?
============================

There are three parameters that control whether a product can be purchased by a customer:

* Status
* StartSellingDate
* Stock

As mentioned above, the ``Status`` will ultimately decide whether the product is presented to customers or not. If it is set to ``Offline``, it will not be made available for purchase regardless of the other parameters.

If ``Stock`` is greater than zero and ``StartSellingDate`` is in the past, the product is **buyable**.
If ``Stock`` is zero and ``StartSellingDate`` is in the past, the product is not buyable, but the customer can sign up for notification when the product becomes available for purchase.
If ``StartSellingDate`` is in the future, the product will be **bookable**.
