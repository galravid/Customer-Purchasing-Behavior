[
  {
    $addFields: {
      ProductTypeNum: {
        $switch: {
          branches: [
            {
              case: {
                $eq: [
                  "$ProductType",
                  "Headphones"
                ]
              },
              then: 1
            },
            {
              case: {
                $or: [
                  {
                    $eq: [
                      "$ProductType",
                      "Tablet"
                    ]
                  },
                  {
                    $eq: [
                      "$ProductType",
                      "Laptop"
                    ]
                  },
                  {
                    $eq: [
                      "$ProductType",
                      "Smartwatch"
                    ]
                  }
                ]
              },
              then: 2
            },
            {
              case: {
                $eq: [
                  "$ProductType",
                  "Smartphone"
                ]
              },
              then: 3
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
        ProductTypeNum: {
          $in: [1, 2, 3]
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
        _id: "$ProductTypeNum",
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
