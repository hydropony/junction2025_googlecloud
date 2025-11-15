# Sales & Deliveries Exploration

- File: `valio_aimo_sales_and_deliveries_junction_2025.csv`
- Sampled rows: 100000

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
| storage_location | 0.986 |
| delivered_qty | 0.986 |
| delivery_number | 0.986 |
| plant | 0.986 |
| transfer_number | 0.983 |
| warehouse_number | 0.983 |
| picking_confirmed_date | 0.983 |
| picking_confirmed_time | 0.983 |
| picking_picked_qty | 0.983 |

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
| 400122 | 1380 |
| 404279 | 1045 |
| 400315 | 842 |
| 401016 | 707 |
| 401080 | 632 |
| 400077 | 523 |
| 403377 | 485 |
| 409443 | 470 |
| 400431 | 451 |
| 400070 | 434 |
| 405270 | 423 |
| 401216 | 406 |
| 408414 | 405 |
| 400127 | 389 |
| 407451 | 387 |
| 407338 | 375 |
| 400129 | 364 |
| 407314 | 361 |
| 412217 | 350 |
| 400432 | 348 |

### customer_number

| value | count |
|---|---|
| 34750 | 405 |
| 31346 | 351 |
| 31350 | 311 |
| 34834 | 310 |
| 32722 | 298 |
| 31383 | 284 |
| 31371 | 280 |
| 32036 | 271 |
| 32032 | 264 |
| 32190 | 258 |
| 33320 | 239 |
| 32934 | 238 |
| 31799 | 237 |
| 33520 | 237 |
| 31893 | 236 |
| 33400 | 232 |
| 30692 | 228 |
| 33282 | 226 |
| 30685 | 216 |
| 32101 | 216 |

## Sample rows

```json
[
  {
    "order_number": 10000000,
    "order_created_date": "2024-09-01",
    "order_created_time": 336,
    "requested_delivery_date": "2024-09-02",
    "customer_number": 33258,
    "order_row_number": 10,
    "product_code": 409510,
    "order_qty": 5.0,
    "sales_unit": "ST",
    "delivery_number": 20000000.0,
    "plant": 30588.0,
    "storage_location": 2012.0,
    "delivered_qty": 5.0,
    "transfer_number": 30000212.0,
    "warehouse_number": 3001.0,
    "picking_confirmed_date": "2024-09-01",
    "picking_confirmed_time": 203837.0,
    "picking_picked_qty": 5.0
  },
  {
    "order_number": 10000000,
    "order_created_date": "2024-09-01",
    "order_created_time": 336,
    "requested_delivery_date": "2024-09-02",
    "customer_number": 33258,
    "order_row_number": 40,
    "product_code": 410914,
    "order_qty": 12.0,
    "sales_unit": "ST",
    "delivery_number": 20000000.0,
    "plant": 30588.0,
    "storage_location": 2012.0,
    "delivered_qty": 12.0,
    "transfer_number": 30000212.0,
    "warehouse_number": 3001.0,
    "picking_confirmed_date": "2024-09-01",
    "picking_confirmed_time": 203734.0,
    "picking_picked_qty": 12.0
  },
  {
    "order_number": 10000000,
    "order_created_date": "2024-09-01",
    "order_created_time": 336,
    "requested_delivery_date": "2024-09-02",
    "customer_number": 33258,
    "order_row_number": 50,
    "product_code": 406587,
    "order_qty": 4.0,
    "sales_unit": "ST",
    "delivery_number": 20000000.0,
    "plant": 30588.0,
    "storage_location": 2012.0,
    "delivered_qty": 4.0,
    "transfer_number": 30000211.0,
    "warehouse_number": 3001.0,
    "picking_confirmed_date": "2024-09-01",
    "picking_confirmed_time": 204149.0,
    "picking_picked_qty": 4.0
  },
  {
    "order_number": 10000000,
    "order_created_date": "2024-09-01",
    "order_created_time": 336,
    "requested_delivery_date": "2024-09-02",
    "customer_number": 33258,
    "order_row_number": 60,
    "product_code": 406588,
    "order_qty": 4.0,
    "sales_unit": "ST",
    "delivery_number": 20000000.0,
    "plant": 30588.0,
    "storage_location": 2012.0,
    "delivered_qty": 4.0,
    "transfer_number": 30000211.0,
    "warehouse_number": 3001.0,
    "picking_confirmed_date": "2024-09-01",
    "picking_confirmed_time": 204124.0,
    "picking_picked_qty": 4.0
  },
  {
    "order_number": 10000000,
    "order_created_date": "2024-09-01",
    "order_created_time": 336,
    "requested_delivery_date": "2024-09-02",
    "customer_number": 33258,
    "order_row_number": 70,
    "product_code": 401369,
    "order_qty": 8.0,
    "sales_unit": "BOT",
    "delivery_number": 20000000.0,
    "plant": 30588.0,
    "storage_location": 2012.0,
    "delivered_qty": 8.0,
    "transfer_number": 30000211.0,
    "warehouse_number": 3001.0,
    "picking_confirmed_date": "2024-09-01",
    "picking_confirmed_time": 205255.0,
    "picking_picked_qty": 8.0
  }
]
```