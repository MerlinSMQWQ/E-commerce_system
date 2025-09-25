import User
import Product
import Order
from Order import OrderStatus

# 使用pytest测试Product、User、Order是否实现
def test_order_with_available_stock():
    product = Product(product_id='product-001', stock = 10, price = 20)
    user = User(user_id='user-001', balance = 1)
    order = Order(order_id = 'order-001', user = user, product = product, quantity = 5)

    assert product.stock == 5
    assert order.status == OrderStatus.UNPAID