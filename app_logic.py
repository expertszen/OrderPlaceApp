def calculate_discount(price, discount_percent):
    """
    Calculate the price after applying the discount.

    Parameters:
    - price (int or float): Original price
    - discount_percent (int or float): Discount percentage

    Returns:
    - float: Discounted price rounded to two decimal places

    Raises:
    - TypeError: If inputs are not numeric
    """
    if not isinstance(price, (int, float)) or not isinstance(discount_percent, (int, float)):
        raise TypeError("Inputs must be numeric.")
    return round(price - (price * discount_percent / 100), 2)


def validate_email(email):
    """
    Validate whether the input string is a valid email format.

    Parameters:
    - email (str): Email address to validate

    Returns:
    - bool: True if email contains '@' and '.', else False

    Raises:
    - TypeError: If email is not a string
    """
    if not isinstance(email, str):
        raise TypeError("Email must be a string.")
    return "@" in email and "." in email


def process_order(order_id, quantity):
    """
    Process an order based on order ID and quantity.

    Parameters:
    - order_id (str): The unique identifier of the order
    - quantity (int): The quantity to process

    Returns:
    - str: Confirmation message

    Raises:
    - TypeError: If order_id is not a string or quantity is not an integer
    - ValueError: If quantity is less than or equal to zero
    """
    if not isinstance(order_id, str) or not isinstance(quantity, int):
        raise TypeError("Invalid input types.")
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")
    return f"Order {order_id} processed with quantity {quantity}"