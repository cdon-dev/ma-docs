.. include:: ../toc_default.txt


Product Status Code
###################

The product status enumeration is used by the :ref:`tracking-import-summary` query to indicate the current status of an specific product in a delivery. The property may be one of the following values:

.. _table-tracking-product-status-code:

+-----------------------+-------------+-----------------------------------------------+
| Status                | Status Code | Description                                   |
+=======================+=============+===============================================+
| Queued                | 1           | Still waiting to be imported.                 |
+-----------------------+-------------+-----------------------------------------------+
| Processing            | 2           | The import process is ongoing for this        |
|                       |             | product.                                      |
+-----------------------+-------------+-----------------------------------------------+
| Imported              | 3           | The product has been successfully imported!   |
+-----------------------+-------------+-----------------------------------------------+
| PartiallyImported     | 4           | Some of the data has been successfully        |
|                       |             | imported, whereas other data has not yet      |
|                       |             | been imported.                                |
+-----------------------+-------------+-----------------------------------------------+
| Failed                | 5           | This product has been rejected for some       |
|                       |             | reason.                                       |
+-----------------------+-------------+-----------------------------------------------+
