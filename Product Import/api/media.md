# Media Data Type

The media data type associate pictures and videos with a product.

The URL to post media data to is:
```
http://import.api.marketplace.cdon.com/media
```


## Data Contract

The relevant schema files are the following:

* media.xsd
* types.xsd

The last file is a supplement to the media.xsd, which define the media data structure.


## Product Variations

Product elements in the product data type support variations of the same product (e.g. different colors of a product). In the media import, it is possible to assign different media to both the main product and/or the variation products.


### Product ID

The media will, of course, be imported to the specified product ID.

If media is added to the main product, this media will be presented when the product page is first displayed to the user. The media added to the variation products will presented when the user selects the variation.


### Multi-variations

In cases where a product variant varies on two attributes at the same time, certain rules apply.

* Size and Color. *Color* is the predominant variable.
* Size and Flavor. *Size* is the predominant variable.

This means that the predominant variable's media will be presented to the user.

Example 1:
> A shirt varies on size (e.g. S, M or L) and color (e.g. red or green).
When the user has selected the size "M", the picture displayed will not change until the user selects another color.

Example 2:
> A beverage varies on size (e.g. 2dl, 5dl or 1 liter) and flavor (e.g. banana or strawberry).
When the user has selected the flavor "banana", the picture displayed will not change until the user selects another size.


## Validation Rules

Every product must have exactly one main picture.

Extra pictures and/or videos are optional.