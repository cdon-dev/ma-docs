# Stock Data Type

The stock data type specifies availability details for a product.

Every product must specify the availability status for each market, as well as the expected delivery time range. The intention is to give the customer an as accurate estimation as possible of when the product will be delivered.

Products with the status "*offline*" will not be buyable.

This data type is incremental, which means that any data that can be applied will be applied without altering related data. Hence, it is possible to import just the updates as soon as they are available.


## XSD

The data structure is defined in a number of XSD (XML Schema Definition) files at the following location:

[http://schemas.cdon.com/marketplace/](http://schemas.cdon.com/marketplace/)

The relevant files are the following:

* stock.xsd
* types.xsd

The last file is a supplement to the stock.xsd, which define the stock data structure.


## Validation

The delivery time is a range in number of days, where the minimum value may not be greater than the maximum value.