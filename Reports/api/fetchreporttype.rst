.. include:: ../../toc_default.txt


Fetch order report type
###############

Gets a list of available report types.


Response Attributes
==================

.. _table-report-response-attributes:

+-----------------------+-------------+-----------------------------------------------------------+
| Variable              | Type        | Description                                               |
+=======================+=============+===========================================================+
| ReportId              | guid        | The unique id of the report type.                         |
+-----------------------+-------------+-----------------------------------------------------------+
| DisplayName           | string      | The name of the report type.                              |
+-----------------------+-------------+-----------------------------------------------------------+
| Description           | string      | A description of the report type.                         |
+-----------------------+-------------+-----------------------------------------------------------+



Response Example - json:
========================

.. code-block:: json

	[
	 {
	  "ReportId": "00000000-0000-0000-0000-000000000001",
	  "DisplayName": "The name of the report",
	  "Description": "Description for the report"
	 }
	 {
	  "ReportId": "00000000-0000-0000-0000-000000000002",
	  "DisplayName": "The name of another report",
	  "Description": "Description for another report"
	 }
	]

The ReportId is used when calling the other report APIs.


Code Example C#
========================

.. code-block:: csharp

	public string Get(string path)
	{
	  var httpClient = new HttpClient() { BaseAddress = new Uri("https://admin.marketplace.cdon.com/") };
	  httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("api", ApiKey);
	  var response = httpClient.GetAsync(path).Result;
	  response.EnsureSuccessStatusCode();

	  return response.Content.ReadAsStringAsync().Result;
	}
