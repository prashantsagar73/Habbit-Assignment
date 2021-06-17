from django.test import TestCase
from django.contrib.auth.models import User
from courses.models import Product, Category


class Test_Create_Product(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')
        test_product = Product.objects.create(category_id=1, course='course Title',
                                              price='Product price', slug='product-course', author_id=1, status='published')

    def test_product_content(self):
        product = Product.postobjects.get(id=1)
        author = Product.postobjects.get(id=1)
        cat = Category.objects.get(id=1)
        course = f'{product.author}'
        price = f'{product.price}'
        status = f'{product.status}'
        self.assertEqual(author, 'test_user1')
        self.assertEqual(course, 'course Title')
        self.assertEqual(price, ' Content')
        self.assertEqual(status, 'published')
        self.assertEqual(str(product), "Product course")
        self.assertEqual(str(cat), "django")
