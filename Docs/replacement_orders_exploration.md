# Replacement Orders Exploration

- File: `valio_aimo_replacement_orders_junction_2025.csv`
- Sampled rows: 15069

## Dtypes

| column | dtype |
|---|---|
| order_number | int64 |
| order_created_date | object |
| order_created_time | int64 |
| requested_delivery_date | object |
| customer_number | int64 |
| order_row_number | int64 |
| product_code | int64 |
| order_qty | float64 |
| sales_unit | object |
| delivery_number | float64 |
| plant | float64 |
| storage_location | float64 |
| delivered_qty | float64 |
| transfer_number | float64 |
| warehouse_number | float64 |
| picking_confirmed_date | object |
| picking_confirmed_time | float64 |
| picking_picked_qty | float64 |

## Non-null ratios (top)

| column | non_null_ratio |
|---|---|
| order_number | 1.000 |
| order_created_time | 1.000 |
| requested_delivery_date | 1.000 |
| customer_number | 1.000 |
| order_row_number | 1.000 |
| product_code | 1.000 |
| order_qty | 1.000 |
| sales_unit | 1.000 |
| order_created_date | 1.000 |
| storage_location | 0.976 |
| delivered_qty | 0.976 |
| delivery_number | 0.976 |
| plant | 0.976 |
| transfer_number | 0.937 |
| warehouse_number | 0.937 |
| picking_confirmed_date | 0.937 |
| picking_confirmed_time | 0.937 |
| picking_picked_qty | 0.937 |

## Candidate fields (auto-detected)

- sku: product_code
- order: order_number, order_created_date, order_created_time, order_row_number, order_qty
- customer: customer_number
- date: order_created_date, order_created_time, requested_delivery_date, picking_confirmed_date, picking_confirmed_time
- qty: order_qty, delivered_qty, picking_picked_qty
- delivered: requested_delivery_date, delivery_number, delivered_qty

## Top values for selected categorical/id columns

### product_code

| value | count |
|---|---|
| 403744 | 426 |
| 416992 | 192 |
| 401030 | 186 |
| 407335 | 167 |
| 400070 | 143 |
| 400938 | 138 |
| 400135 | 129 |
| 402546 | 122 |
| 403504 | 120 |
| 406012 | 118 |
| 407314 | 115 |
| 400166 | 109 |
| 401016 | 101 |
| 400122 | 96 |
| 416974 | 83 |
| 406938 | 83 |
| 402344 | 82 |
| 404279 | 79 |
| 413134 | 75 |
| 411281 | 74 |

### customer_number

| value | count |
|---|---|
| 33007 | 184 |
| 30811 | 131 |
| 30792 | 105 |
| 31228 | 60 |
| 32704 | 60 |
| 31209 | 60 |
| 31893 | 58 |
| 34731 | 56 |
| 33332 | 56 |
| 31721 | 53 |
| 33968 | 53 |
| 31064 | 53 |
| 34666 | 52 |
| 35020 | 51 |
| 34730 | 50 |
| 33967 | 49 |
| 33964 | 48 |
| 34667 | 47 |
| 34729 | 47 |
| 33965 | 45 |

## Sample rows

```json
[
  {
    "order_number": 32014535,
    "order_created_date": "2024-09-02",
    "order_created_time": 70832,
    "requested_delivery_date": "2024-09-02",
    "customer_number": 33345,
    "order_row_number": 10,
    "product_code": 410397,
    "order_qty": 2.0,
    "sales_unit": "ST",
    "delivery_number": 21042242.0,
    "plant": 30588.0,
    "storage_location": 2012.0,
    "delivered_qty": 2.0,
    "transfer_number": 32017375.0,
    "warehouse_number": 3001.0,
    "picking_confirmed_date": "2024-09-02",
    "picking_confirmed_time": 82024.0,
    "picking_picked_qty": 2.0
  },
  {
    "order_number": 32014536,
    "order_created_date": "2024-09-02",
    "order_created_time": 70818,
    "requested_delivery_date": "2024-09-02",
    "customer_number": 31599,
    "order_row_number": 10,
    "product_code": 406468,
    "order_qty": 1.0,
    "sales_unit": "ST",
    "delivery_number": 21042243.0,
    "plant": 30588.0,
    "storage_location": 2012.0,
    "delivered_qty": 1.0,
    "transfer_number": 32017376.0,
    "warehouse_number": 3001.0,
    "picking_confirmed_date": "2024-09-02",
    "picking_confirmed_time": 81259.0,
    "picking_picked_qty": 1.0
  },
  {
    "order_number": 32014537,
    "order_created_date": "2024-09-02",
    "order_created_time": 71137,
    "requested_delivery_date": "2024-09-02",
    "customer_number": 31260,
    "order_row_number": 10,
    "product_code": 411433,
    "order_qty": 5.0,
    "sales_unit": "PAK",
    "delivery_number": 21042244.0,
    "plant": 30588.0,
    "storage_location": 2012.0,
    "delivered_qty": 5.0,
    "transfer_number": 32017373.0,
    "warehouse_number": 3001.0,
    "picking_confirmed_date": "2024-09-02",
    "picking_confirmed_time": 74027.0,
    "picking_picked_qty": 5.0
  },
  {
    "order_number": 32014538,
    "order_created_date": "2024-09-02",
    "order_created_time": 71223,
    "requested_delivery_date": "2024-09-02",
    "customer_number": 31600,
    "order_row_number": 10,
    "product_code": 406468,
    "order_qty": 1.0,
    "sales_unit": "ST",
    "delivery_number": 21042245.0,
    "plant": 30588.0,
    "storage_location": 2012.0,
    "delivered_qty": 1.0,
    "transfer_number": 32017377.0,
    "warehouse_number": 3001.0,
    "picking_confirmed_date": "2024-09-02",
    "picking_confirmed_time": 81532.0,
    "picking_picked_qty": 1.0
  },
  {
    "order_number": 32014539,
    "order_created_date": "2024-09-02",
    "order_created_time": 71239,
    "requested_delivery_date": "2024-09-02",
    "customer_number": 33814,
    "order_row_number": 10,
    "product_code": 410636,
    "order_qty": 1.0,
    "sales_unit": "ST",
    "delivery_number": 21042246.0,
    "plant": 30588.0,
    "storage_location": 2012.0,
    "delivered_qty": 1.0,
    "transfer_number": 32017372.0,
    "warehouse_number": 3001.0,
    "picking_confirmed_date": "2024-09-02",
    "picking_confirmed_time": 75944.0,
    "picking_picked_qty": 1.0
  }
]
```