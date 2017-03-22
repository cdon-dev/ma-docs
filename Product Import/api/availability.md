# Availability Data Type

The availability data type specifies details regarding stock, delivery times, etc.

Every product must specify the availability status for each market, as well as the expected delivery time range. The intention is to give the customer an as accurate estimation as possible of when the product will be delivered.

Products with the status "*offline*" will not be buyable.

This data type is incremental, which means that any data that can be applied will be applied without altering related data. Hence, it is possible to import just the updates as soon as they are available.


## Data Contract

The relevant schema files are the following:

* availability.xsd
* types.xsd

The last file is a supplement to the availability.xsd, which define the availability data structure.


## Validation Rules

The delivery time is a range in number of days, where the minimum value may not be greater than the maximum value.