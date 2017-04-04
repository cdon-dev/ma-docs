.. include:: ../../toc_default.txt


Fetch Report
############

In order to generate a report you perform a POST call to the reports API with the parameters you wish to use for the report. The call must also include the fields ReportId and Format for the type of report you wish to generate and the format of the report.

Let’s say for example that you wish to create a report of all Swedish orders that are either returned or cancelled and you want the result as JSON.

From the call to GET api/reports you know that the ReportId of order report is “d4ea173d-bfbc-48f5-b121-60f1a5d35a34”.

From the call to GET api/reports/d4ea173d-bfbc-48f5-b121-60f1a5d35a34 you know that to filter on Swedish orders you set the CountryCodes attribute to “Sweden” and to get returned and cancelled orders you set the States attribute to 2 and 3. So in the end the filter would look like this:


.. code-block:: json

	{
	  "CountryCodes": [ "Sweden" ],
	  "States": ["2", "3"]
	}


You then post the parameters as form data (content-type: application/x-www-form-urlencoded) so the request body would look like this::

	ReportId=d4ea173d-bfbc-48f5-b121-60f1a5d35a34&format=json&filter={"CountryCodes":["Sweden"],"States":["2","3"]}

Note that not specifying a parameter is the same as specifying all the values for that parameter, e.g. not including the CountryCodes attribute is the same as getting orders for all countries.


Order Report Attributes
=======================

Below we list some the filter parameters for the order API that have static values and what those values are.

.. _table-report-attributes:

+-----------------------+-------------+------------------------------------------------------------------------------------------------+
| Variable              | Type        | Description                                                                                    |
+=======================+=============+================================================================================================+
| States                | enum        | The state of the order. Available states are:                                                  |
|                       |             |    Pending = 0                                                                                 |
|                       |             |    Delivered = 1                                                                               |
|                       |             |    Cancelled = 2                                                                               |
|                       |             |    Returned = 3                                                                                |
|                       |             |    Invoiced = 4                                                                                |
+-----------------------+-------------+------------------------------------------------------------------------------------------------+
| CountryCodes          | string      | Country of the order, indicating in what channel the order was placed. Availabe countries are: |
|                       |             |    Sweden                                                                                      |
|                       |             |    Denmark                                                                                     |
|                       |             |    Norway                                                                                      |
|                       |             |    Finland                                                                                     |
+-----------------------+-------------+------------------------------------------------------------------------------------------------+
| PaymentStates         | enum        | Indicates the state of the payment. Available states are:                                      |
|                       |             |    NotApplicable = 0                                                                           |
|                       |             |    AwaitingPayment = 1                                                                         |
|                       |             |    Paid = 2                                                                                    |
|                       |             |    AwaitingRefund = 3                                                                          |
|                       |             |    Refunded = 4                                                                                |
+-----------------------+-------------+------------------------------------------------------------------------------------------------+


Code Example - C#
=================

Below you can find an example of a method that calls the POST api to get a report of pending orders.
The method takes the path to the API, i.e. /api/reports, and the reportId of the kind of report to generate.


.. code-block:: csharp

	public string Post(Guid repordId, string path)
	{
	  var filter = new JavaScriptSerializer().Serialize(new
	  {
		 States = new[] { "0" } // Pending state
	  });

	  var content = new FormUrlEncodedContent(new[]
	  {
		 new KeyValuePair("ReportId", repordId.ToString()),
		 new KeyValuePair("format", "json"),
		 new KeyValuePair("filter", filter)
	  });

	  var httpClient = new HttpClient() { BaseAddress = new Uri("https://admin.marketplace.cdon.com/") };
	  httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("api", ApiKey);
	  var response = httpClient.PostAsync(path, content).Result;
	  response.EnsureSuccessStatusCode();

	  return response.Content.ReadAsStringAsync().Result;
	}
