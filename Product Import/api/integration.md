# Introduction

Deliveries are made to Marketplace by posting **XML**-formatted data to the endpoint for the corresponding [data type](../data-types.md).

Responses are returned with a HTTP status code and possibly a body in **JSON**-format.

The [receipt](../receipts.md) received can be used to [track](../tracking.md) the progress of the delivery.


## Data Contracts

As mentioned in [validation](../validation.md), a pre-validation is performed on the delivery. This validation is based on a data contract specified in a set of XSD (XML Schema Definition) files.

The location of the schema files is:

[http://schemas.cdon.com/marketplace/](http://schemas.cdon.com/marketplace/)

Use these files to generate XML and validate against them to avoid submitting invalid data.