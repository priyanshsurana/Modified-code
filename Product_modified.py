from products import dao


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data: dict) -> 'Product':
        """Creates a Product instance from a dictionary or sqlite3.Row."""
        return Product(
            id=data['id'],
            name=data['name'],
            description=data['description'],
            cost=data['cost'],
            qty=data['qty'] if 'qty' in data else 0  # Default to 0 if 'qty' is missing
        )


def list_products() -> list[Product]:
    """Fetches and returns a list of all products as Product instances."""
    return [Product.load(product) for product in dao.list_products()]


def get_product(product_id: int) -> Product:
    """Fetches and returns a single product by its ID."""
    product_data = dao.get_product(product_id)
    return Product.load(product_data)


def add_product(product: dict):
    """Adds a new product. Validates the input before adding."""
    required_keys = {'id', 'name', 'description', 'cost', 'qty'}
    if not required_keys.issubset(product):
        raise ValueError(f"Product data must include keys: {required_keys}")
    
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    """Updates the quantity of a product. Ensures quantity is non-negative."""
    if qty < 0:
        raise ValueError("Quantity cannot be negative")
    dao.update_qty(product_id, qty)
