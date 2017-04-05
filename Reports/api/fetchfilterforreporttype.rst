.. include:: ../../toc_default.txt


Fetch Filter for Report Type
############################

| GET api/reports/{reportId}
| Gets the available parameters for the report with the specifed reportId.



Response Example - JSON
=======================

.. code-block:: json

	{
	 "Parameters": [
	 {
	  "Type": "term",
	  "Metadata": {
		 "Label": "Country",
		 "PostFieldName": "CountryCodes"
	  },
	  "Values": [
	  {
		 "Term": "Sweden",
		 "DisplayName": "Sweden",
		 "Selected": false,
		 "Enabled": true,
		 "FilteredCount": 100
	  },
	  {
		 "Term": "Denmark",
		 "DisplayName": "Denmark",
		 "Selected": false,
		 "Enabled": true,
		 "FilteredCount": 50
	  }
	 ]
	 },
	 {
	  "Type": "term",
	  "Metadata": {
		 "Label": "State",
		 "PostFieldName": "States"
	  },
	  "Values": [
	  {
		 "Term": "0",
		 "DisplayName": "Pending",
		 "Selected": false,
		 "Enabled": true,
		 "FilteredCount": 10
	  },
	  {
		 "Term": "2",
		 "DisplayName": "Cancelled",
		 "Selected": false,
		 "Enabled": true,
		 "FilteredCount": 10
	  },
	  {
		 "Term": "3",
		 "DisplayName": "Returned",
		 "Selected": false,
		 "Enabled": true,
		 "FilteredCount": 30
	  },
	  {
		 "Term": "4",
		 "DisplayName": "Invoiced",
		 "Selected": false,
		 "Enabled": true,
		 "FilteredCount": 100
	  }
	  ]
	 }
	 ],
	 "Formats": [
	 {
	   "DisplayName": "Excel",
	   "Key": "excel"
	 },
	 {
	   "DisplayName": "JSON",
	   "Key": "json"
	 },
	 {
	   "DisplayName": "XML",
	   "Key": "xml"
	 }
	 ]
	}


The “Parameters”-array contains several the types of parameters available and values that can be used to filter on this parameter. The “Formats”-array contains the available formats that the report can be generated in. For the Parameters the PostFieldName is the key for the filter and Term is the value of the filter.

In the above example (which is for the order report api) we see that we can filter the report to contain Swedish or Danish orders and also on the state of the order (Invoiced, Returned or Cancelled). We also see how many orders there are that match the different filter values. For example, there are 100 Swedish orders and 30 orders that have Returned as the state. In the Formats-section we see that the available formats for the report is Excel, JSON and XML. For more information on how to use this information to generate a report see the documentation for POST api/reports.


Code Example - C#
=================
Below you can find a method that calls the GET api to get the details of how to generate a specific report.
The method takes the path to the API, i.e. /api/reports, and the reportId of the report that you wish to get parameter details for as arguments.


.. code-block:: csharp

	public string Get(Guid repordId, string path)
	{
	  var httpClient = new HttpClient() { BaseAddress = new Uri("https://admin.marketplace.cdon.com/") };
	  httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("api", ApiKey);
	  var response = httpClient.GetAsync(path + repordId).Result;
	  response.EnsureSuccessStatusCode();

	  return response.Content.ReadAsStringAsync().Result;
	}
