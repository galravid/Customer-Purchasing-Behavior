[
  {
    $addFields: {
      PaymentMethodCategories: {
        $switch: {
          branches: [
            {
              case: {
                $eq: ["$PaymentMethod", "Cash"]
              },
              then: 1
            },
            {
              case: {
                $eq: [
                  "$PaymentMethod",
                  "Debit Card"
                ]
              },
              then: 2
            },
            {
              case: {
                $or: [
                  {
                    $eq: [
                      "$PaymentMethod",
                      "PayPal"
                    ]
                  },
                  {
                    $eq: [
                      "$PaymentMethod",
                      "Paypal"
                    ]
                  },
                  {
                    $eq: [
                      "$PaymentMethod",
                      "Credit Card"
                    ]
                  }
                ]
              },
              then: 3
            },
            {
              case: {
                $eq: [
                  "$PaymentMethod",
                  "Bank Transfer"
                ]
              },
              then: 4
            }
          ]
        }
      }
    }
  },
  {
    $match:
      /**
       * query: The query in MQL.
       */
      {
        PaymentMethodCategories: {
          $in: [1, 2, 3, 4]
        }
      }
  },
  {
    $group:
      /**
       * _id: The id of the group.
       * fieldN: The first field name.
       */
      {
        _id: "$PaymentMethodCategories",
        AVG_of_Total_price: {
          $avg: "$TotalPrice"
        }
      }
  },
  {
    $sort:
      /**
       * Provide any number of field/order pairs.
       */
      {
        _id: 1
      }
  }
]
