.. include:: toc_default.txt


Markets
#######

On the CDON web site, there is a concept known as *markets*, which roughly translates to which country the customer is visiting from, except in the case of b2b_se where it means that the product can be sold on our B2B-site. The identifiers for these markets, e.g. "se", follows the `ISO 3166-1 alpha-2`_ country code definition. However, currently there are only five supported markets:

* se, Sweden
* b2b_se, B2B Sweden
* dk, Denmark
* no, Norway
* fi, Finland

The Marketplace APIs inherit this concept, which is why some product and order data is different between markets.

In some APIs, there is also a "default" market used as a fallback value. However, localized content is always preferred as it provides a better user experience.


.. _ISO 3166-1 alpha-2: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
