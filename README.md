# Backend Challenge:
Prueba para backend con Python/Django 

## Objetivo:

Diseñar una API con

+ Python3.x
+ Django
+ PostgreSQL


### Consideraciones

Producto
+ id: String
+ name: String
+ value: Float
+ discount_value: Float?
+ stock: Int

Endpoints
+ POST: api/products/bulk_insert
+ GET: api/products


## USO

+ Método GET
+ Endpoint api/products

```bash
curl http://127.0.0.1:8000/api/products
```

+ Método POST
+ Endpoint api/products/bulk_insert

```bash
curl -H "Content-Type: application/json" -X POST -d '{"products": [{ "name": "Polo Niña", "value": "28.5", "stock": 15, "discount_value": "7.4" }]}' "http://127.0.0.1:8000/api/products/bulk_insert"

