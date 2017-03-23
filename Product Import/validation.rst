##########
Validation
##########

The pre-validation performed immediately on the import request only validates that the data is acceptable in the sense that it is compliant with the delivery contract. No evaluation of the contents is done at this stage.

After the data has been accepted, one of the stages is the business validation. During this process data may be discarded or modified according to the current business rules. Any products that violate a business rule will be rejected, and the details concerning this event is retrievable using the receipt.

This kind of delayed validation offers two important benefits:

* Each product is evaluated individually. This allows for a complete inventory validation, as opposed to an import that halts on the first error.
* Detailed validation messages allow for self-help. Failed products have already been identified and can be amended by you for re-import.
