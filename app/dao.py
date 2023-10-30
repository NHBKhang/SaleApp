def get_catogories():
    return [
        {
            'id': 0,
            'name': 'Trang chủ'
        },
        {
            'id': 1,
            'name': 'Phone'
        },
        {
            'id': 2,
            'name': 'Tablet'

        }]


def get_products(kw=None):
    products = [
        {
            'id': 1,
            'name': 'IPhone 13',
            'price': 20000000,
            'description': 'Iphone 13',
            'image': 'https://cdn.hoanghamobile.com/i/preview/Uploads/2021/09/15/image-removebg-preview-12.png'
        },
        {
            'id': 1,
            'name': 'IPhone 13',
            'price': 20000000,
            'description': 'Iphone 13',
            'image': 'https://cdn.hoanghamobile.com/i/preview/Uploads/2021/09/15/image-removebg-preview-12.png'

        },
        {
            'id': 1,
            'name': 'IPhone 13',
            'price': 20000000,
            'description': 'Iphone 13',
            'image': 'https://cdn.hoanghamobile.com/i/preview/Uploads/2021/09/15/image-removebg-preview-12.png'

        },
        {
            'id': 1,
            'name': 'Samsung',
            'price': 20000000,
            'description': 'Iphone 13',
            'image': 'https://cdn.hoanghamobile.com/i/preview/Uploads/2021/09/15/image-removebg-preview-12.png'

        }]
    if kw:
        products = [p for p in products if kw.lower() in p['name'].lower()]

    return products
