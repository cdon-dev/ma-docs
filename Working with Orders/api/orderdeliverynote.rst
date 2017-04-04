.. include:: ../../toc_default.txt


Order Return address
###############

To use the Delivery Note API you first need to register a return address in the Marketplace admin. Thereafter you can fetch your address ids and use them in the delivery note API call.

Request Example
======================
	GET https://admin.marketplace.cdon.com/api/returnaddress HTTP/1.1
	Accept: application/json
	Authorization: api <apiKey>


Response Example - json:
========================

.. code-block:: json

	{
	  "DisplayName": "Display name",
	  "AddressId": "8f8355a0-768f-45cb-b877-aeb5d127c766",
	  "StreetAddress": "SomeStreet 3",
	  "PostalCode": "34450",
	  "City": "Malmö",
	  "Country": "Sweden",
	  "COAddress": null,
	  "BoxAddress": null,
	}

Response Attributes
==================

.. _table-order-response-attributes:

+-----------------------+-------------+-----------------------------------------------------------+
| Variable              | Type        | Description                                               |
+=======================+=============+===========================================================+
| DisplayName           | string      | Display name for the return address.                      |
+-----------------------+-------------+-----------------------------------------------------------+
| AddressId             | guid        | An id which refers to your return address.                |
+-----------------------+-------------+-----------------------------------------------------------+
| StreetAddress         | string      | The street address.                                       |
+-----------------------+-------------+-----------------------------------------------------------+
| PostalCode            | string      | The street postal code your return address resides in.    |
+-----------------------+-------------+-----------------------------------------------------------+
| City                  | string      | The city your return address resides in.                  |
+-----------------------+-------------+-----------------------------------------------------------+
| Country               | string      | The country your return address resides in.               |
+-----------------------+-------------+-----------------------------------------------------------+
| COAddress             | string      | CO address of you return address.                         |
+-----------------------+-------------+-----------------------------------------------------------+
| BoxAddress            | string      | Box address of you return address.                        |
+-----------------------+-------------+-----------------------------------------------------------+



Order Delivery note
###############

Delivery Note API provides you the ability to generate Delivery Note report for specified orders.

Request Example - JSON
======================

.. code-block:: json

	[
	 {
	  "OrderId": 1,
	  "AddressId": "04e02c6f-ca99-4903-8ee9-692a28044111",
	  "DeliveryNoteRows": [
	  {
		 "ProductId": "sample string 1",
		 "ProductName": "sample string 2",
		 "Quantity": 3,
		 "PickingLocation": "sample string 4"
	  },
	  {
		 "ProductId": "sample string 1",
		 "ProductName": "sample string 2",
		 "Quantity": 3,
		 "PickingLocation": "sample string 4"
	  }
	]
	 },
	 {
	  "OrderId": 1,
	  "AddressId": "04e02c6f-ca99-4903-8ee9-692a28044111",
	  "DeliveryNoteRows": [
	  {
		 "ProductId": "sample string 1",
		 "ProductName": "sample string 2",
		 "Quantity": 3,
		 "PickingLocation": "sample string 4"
	  },
	  {
		 "ProductId": "sample string 1",
		 "ProductName": "sample string 2",
		 "Quantity": 3,
		 "PickingLocation": "sample string 4"
	  }
	 ]
	 }
	]

Request Attributes
==================

.. _table-deliverynote-request-attributes:

+-----------------------+------------------------------+-----------------------------------------------------------------------------------+------------+
| Variable              | Type                         | Description                                                                       | Required   |
+=======================+==============================+===================================================================================+============+
| OrderId               | integer                      | An id which refers to your order and store in the Marketplace.                    | Yes        |
+-----------------------+------------------------------+-----------------------------------------------------------------------------------+------------+
| AddressId             | guid                         | Refers to the return address associated to a specific order.                      | Yes        |
+-----------------------+------------------------------+-----------------------------------------------------------------------------------+------------+
| DeliveryNoteRows      | IEnumerable{DeliveryNoteRow} | Indicates DeliveryNoteRow list.                                                   | Yes        |
+-----------------------+------------------------------+-----------------------------------------------------------------------------------+------------+

.. _table-deliverynote-request-attributes:

+-----------------------+-------------+----------------------------------------------------------------------------------------------------+------------+
| Variable              | Type        | Description                                                                                        | Required   |
+=======================+=============+====================================================================================================+============+
| ProductId             | integer     | An id which refers to the product and store in the Marketplace.                                    | Yes        |
+-----------------------+-------------+----------------------------------------------------------------------------------------------------+------------+
| ProductName           | string      | Refers to the product name associated to a specific product.                                       | Yes        |
+-----------------------+-------------+----------------------------------------------------------------------------------------------------+------------+
| Quantity              | integer     | Indicates how many products will be delivered.                                                     | Yes        |
+-----------------------+-------------+----------------------------------------------------------------------------------------------------+------------+



Response
========================
This request returns an http status code, indicating how the call went, where the desired result is OK (200), including a binary stream of delivery note PDF document.

Code Example C#
========================

.. code-block:: csharp

	public bool GetDeliveryNote()
	{
	  var parameters = BuildRequestParameter();
	  var apiKey = "bbbbbbb7-bb99-999b-bbb7-bbbbbbbbbbbb";
	  var baseUri = new Uri("https://admin.marketplace.cdon.com/");

	  var client = new HttpClient(new HttpClientHandler()) { BaseAddress = baseUri };
	  client.DefaultRequestHeaders.Add("Authorization", "api " + apiKey);
	  var response = client.PostAsync("/api/deliverynote/", 
					 new StringContent(JsonConvert.SerializeObject(request), Encoding.UTF8, "application/json")).Result;
	  if (response.IsSuccessStatusCode)
	  {
		 var disposition = response.Content.Headers.ContentDisposition.ToString();
		 var filename = disposition.Substring(disposition.IndexOf('=') + 1);
		 var stream = response.Content.ReadAsStreamAsync().Result;

		 var filepath = Path.Combine("d:\\Downloads", filename);
		 using (var fileStream = File.Create(filepath))
		 {
			 stream.Seek(0, SeekOrigin.Begin);
			 stream.CopyTo(fileStream);
		 }
	}
	}

	private static IEnumerable BuildRequestParameter()
	{
	  var result = new List
	  {
		 new DeliveryNoteModel
		 {
			 AddressId = new Guid("6778a353-f685-40a1-ac5b-f9694fb85ac3"),
			 OrderId = 242842680,
			 DeliveryNoteRows = new List(new[]
			 {
				 new DeliveryNoteRow
				 {
					 ProductId = "1111111111",
					 ProductName = "Product Name 1",
					 Quantity = 2
				 }
			 })
		 },
		 new DeliveryNoteModel
		 {
			 AddressId = new Guid("6eff7efc-b4cd-47db-b933-02c47631742f"),
			 OrderId = 41989521,
			 DeliveryNoteRows = new List(new[]
			 {
				 new DeliveryNoteRow
				 {
					 ProductId = "2222222222",
					 ProductName = "Product Name 2",
					 Quantity = 1
				 }
			 })
		 },
		 new DeliveryNoteModel
		 {
			 AddressId = new Guid("6eff7efc-b4cd-47db-b933-02c47631742f"),
			 OrderId = 41358099,
			 DeliveryNoteRows = new List(new[]
			 {
				 new DeliveryNoteRow
				 {
					 ProductId = "3333333333",
					 ProductName = "Product Name 3",
					 Quantity = 1
				 }
			 })
		 }
	  };
	  return result;
	}
