.. include:: ../toc_default.txt


Import Status Code
##################

The import status enumeration is used by the :ref:`tracking-import-status` query to indicate the current overall status of an import. The property may be one of the following values:

.. _table-tracking-import-status-code:

+-----------------------+-------------+-----------------------------------------------+--------------------+
| Status                | Status Code | Description                                   | Processing Started |
+=======================+=============+===============================================+====================+
| NoContent             | 1           | The delivery was empty.                       | No                 |
+-----------------------+-------------+-----------------------------------------------+--------------------+
| Receiving             | 2           | The delivery is still being received.         | Yes                |
+-----------------------+-------------+-----------------------------------------------+--------------------+
| IngestionFailure      | 3           | Something went wrong when receiving the       | Yes                |
|                       |             | delivery. This is also indicated by the HTTP  |                    |
|                       |             | status code `500`_.                           |                    |
+-----------------------+-------------+-----------------------------------------------+--------------------+
| Queued                | 4           | All data has been received, but processing    | No                 |
|                       |             | has not yet started.                          |                    |
+-----------------------+-------------+-----------------------------------------------+--------------------+
| Processing            | 5           | Processing has begun, and there are still     | Yes                |
|                       |             | products to process.                          |                    |
+-----------------------+-------------+-----------------------------------------------+--------------------+
| CompletedSuccessfully | 6           | All products have been successfully imported! | Yes                |
+-----------------------+-------------+-----------------------------------------------+--------------------+
| CompletedWithErrors   | 7           | All products have been processed, but some    | Yes                |
|                       |             | (or all) failed to be imported.               |                    |
+-----------------------+-------------+-----------------------------------------------+--------------------+

Statuses marked with *Processing Started* indicate that there **may** be products which have been processed.
