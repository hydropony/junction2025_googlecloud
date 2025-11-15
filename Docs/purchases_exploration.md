# Purchases Exploration

- File: `valio_aimo_purchases_junction_2025.csv`
- Sampled rows: 100000

## Dtypes

| column | dtype |
|---|---|
| order_number | int64 |
| po_row_number | int64 |
| customer_number | int64 |
| po_created_date | object |
| requested_delivery_date | object |
| product_code | int64 |
| plant | int64 |
| storage_location | int64 |
| ordered_qty | float64 |
| unit | object |
| received_qty | float64 |

## Non-null ratios (top)

| column | non_null_ratio |
|---|---|
| order_number | 1.000 |
| po_row_number | 1.000 |
| customer_number | 1.000 |
| po_created_date | 1.000 |
| requested_delivery_date | 1.000 |
| product_code | 1.000 |
| plant | 1.000 |
| storage_location | 1.000 |
| ordered_qty | 1.000 |
| unit | 1.000 |
| received_qty | 1.000 |

## Candidate fields (auto-detected)

- sku: product_code
- order: order_number, ordered_qty
- customer: customer_number
- date: po_created_date, requested_delivery_date
- qty: ordered_qty, received_qty
- delivered: requested_delivery_date

## Top values for selected categorical/id columns

### product_code

| value | count |
|---|---|
| 407451 | 3332 |
| 407338 | 2714 |
| 407474 | 2146 |
| 407337 | 963 |
| 407327 | 765 |
| 409887 | 742 |
| 409881 | 711 |
| 407326 | 697 |
| 410602 | 676 |
| 402432 | 651 |
| 404015 | 646 |
| 407332 | 629 |
| 407464 | 621 |
| 412827 | 590 |
| 407470 | 590 |
| 412837 | 569 |
| 402431 | 539 |
| 412828 | 481 |
| 407452 | 477 |
| 410635 | 473 |

### customer_number

| value | count |
|---|---|
| 30386 | 23539 |
| 30554 | 7869 |
| 30060 | 4459 |
| 30256 | 3477 |
| 30520 | 3353 |
| 30373 | 3160 |
| 30064 | 2555 |
| 30198 | 2360 |
| 400163 | 2116 |
| 30102 | 1831 |
| 400435 | 1625 |
| 30048 | 1459 |
| 30359 | 1300 |
| 30282 | 1118 |
| 30194 | 1061 |
| 30251 | 1054 |
| 30186 | 982 |
| 30504 | 935 |
| 400032 | 881 |
| 30013 | 855 |

## Sample rows

```json
[
  {
    "order_number": 2300000000,
    "po_row_number": 10,
    "customer_number": 30386,
    "po_created_date": "2024-09-01",
    "requested_delivery_date": "2024-09-03",
    "product_code": 407329,
    "plant": 1001,
    "storage_location": 2011,
    "ordered_qty": 8.0,
    "unit": "ST",
    "received_qty": 8.0
  },
  {
    "order_number": 2300000001,
    "po_row_number": 10,
    "customer_number": 30386,
    "po_created_date": "2024-09-01",
    "requested_delivery_date": "2024-09-03",
    "product_code": 408060,
    "plant": 1001,
    "storage_location": 2011,
    "ordered_qty": 3.0,
    "unit": "ST",
    "received_qty": 3.0
  },
  {
    "order_number": 2300000002,
    "po_row_number": 10,
    "customer_number": 30386,
    "po_created_date": "2024-09-01",
    "requested_delivery_date": "2024-09-03",
    "product_code": 407332,
    "plant": 1001,
    "storage_location": 2011,
    "ordered_qty": 4.0,
    "unit": "ST",
    "received_qty": 4.0
  },
  {
    "order_number": 2300000002,
    "po_row_number": 20,
    "customer_number": 30386,
    "po_created_date": "2024-09-01",
    "requested_delivery_date": "2024-09-03",
    "product_code": 407326,
    "plant": 1001,
    "storage_location": 2011,
    "ordered_qty": 4.0,
    "unit": "ST",
    "received_qty": 4.0
  },
  {
    "order_number": 2300000003,
    "po_row_number": 10,
    "customer_number": 30386,
    "po_created_date": "2024-09-01",
    "requested_delivery_date": "2024-09-04",
    "product_code": 407466,
    "plant": 1001,
    "storage_location": 2011,
    "ordered_qty": 4.0,
    "unit": "RAS",
    "received_qty": 4.0
  }
]
```