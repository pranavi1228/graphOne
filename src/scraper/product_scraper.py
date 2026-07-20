from datetime import datetime


async def fetch_products(startups):
    """
    Convert startup records into product records.
    """
    print(type(startups))

    products = []

    for startup in startups:

        products.append(
            {
                "schemaVersion": "1.0",
                "recordType": "PRODUCT",
                "source": startup["source"],
                "content": {
                    "startupName": startup["content"]["entityName"],
                    "pricingModel": "UNKNOWN",
                },
                "collectedAt": datetime.utcnow().isoformat(),
            }
        )

    print(f"Products extracted : {len(products)}")

    return products