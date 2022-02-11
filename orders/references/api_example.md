# Примеры запросов к API 

## Списки
#### Список категорий
```
GET /api/v1/category

Поиск по наименованию - задать параметр search 
GET /api/v1/category?search=смарт

200 OK
[
    {
        "id": 224,
        "name": "Смартфоны"
    },
    {
        "id": 15,
        "name": "Аксессуары"
    }
]
```
#### Список магазинов, предоставляющих услуги
```
GET /api/v1/shop

Поиск по наименованию - задать параметр search 
GET /api/v1/shop?search=связ

200 OK
[
    {
        "id": 1,
        "name": "Связной",
        "url": null,
        "state": true
    }
]
```
#### Список продуктов
```
GET /api/v1/product

Поиск по наименованию или модели - задать параметр search 
GET /api/v1/product?search=xr

Фильтр по магазину и категории - задать параметры shop_id и category_id
GET /api/v1/product?shop_id=123&category_id=987

200 OK
[
    {
        "id": 1,
        "model": "apple/iphone/xs-max",
        "product": {
            "id": 1,
            "name": "Смартфон Apple iPhone XS Max 512GB (золотистый)"
        },
        "shop": 1,
        "quantity": 14,
        "price": 110000,
        "price_rrc": 116990,
        "product_parameters": [
            {
                "parameter": "Диагональ (дюйм)",
                "value": "6.5"
            },
            {
                "parameter": "Разрешение (пикс)",
                "value": "2688x1242"
            },
            {
                "parameter": "Встроенная память (Гб)",
                "value": "512"
            },
            {
                "parameter": "Цвет",
                "value": "золотистый"
            }
        ]
    }
]
```
## Пользователи

#### Регистрация 
```
POST /api/v1/user/register
{
    "email": "mail@test.org"
    "first_name": "Jhon",
    "last_name": "Smith",
    "password": "fsjfkl12!",
    "company": "My Dog",
    "position": "Manager"
}

200 OK
```

#### Получение токена
```
POST /api/v1/user/login
{
    "email": "mail@test.org"
    "password": "fsjfkl12!",
}

200 OK
{
    "token": "b39d0f93f9e895b82f1724832b7c186a",
}
```
## Контакты пользователя
#### Отображение контактов
```
GET /api/v1/user/contact
Authorization: Token 05b0897fc95950b403f0f81330d3fdb63c4ab960

200 OK
[
    {
        "id": 1,
        "city": "Город 1",
        "street": "Улица 1",
        "house": "1",
        "structure": "1",
        "building": "1",
        "apartment": "1",
        "phone": "11111111"
    }
]
```
#### Добавление контакта
```
POST /api/v1/user/contact
Authorization: Token 05b0897fc95950b403f0f81330d3fdb63c4ab960
    {
        "city": "Город 1",
        "street": "Улица 1",
        "house": "1",
        "structure": "1",
        "building": "1",
        "apartment": "1",
        "phone": "11111111"
    }
    
201 OK
{
    "id": 8,
    "city": "Город 3",
    "street": "Улица 3",
    "house": "3",
    "structure": "3",
    "building": "3",
    "apartment": "3",
    "phone": "+8(123)8889977"
}
```
#### Редактирование контакта
```
PUT /api/v1/user/contact
Authorization: Token 05b0897fc95950b403f0f81330d3fdb63c4ab960
    {
        "id": "1",
        "city": "Город 2",
        "street": "Улица 2",
        "house": "2",
        "structure": "2",
        "building": "2",
        "apartment": "2",
        "phone": "+88(123)1234567"
    }
    
200 OK
{
    "id": "1",
    "city": "Город 2",
    "street": "Улица 2",
    "house": "2",
    "structure": "2",
    "building": "2",
    "apartment": "2",
    "phone": "+88(123)1234567"
}
```
#### Удаление контакта
```
DELETE /api/v1/user/contact
Authorization: Token 05b0897fc95950b403f0f81330d3fdb63c4ab960
    {
        "id": 1
    }
    
200 OK
```
## Продавец
#### Обновление прайса 
```
POST /api/v1/partner/load
Authorization: Token 05b0897fc95950b403f0f81330d3fdb63c4ab960
{
    "url": "https://partner-site.ru/files/price.yaml"
}

200 OK
```
#### Отображение заказов
```
GET /api/v1/partner/orders
Authorization: Token 05b0897fc95950b403f0f81330d3fdb63c4ab960

200 OK
[
    {
        "id": 2,
        "ordered_items": [
            {
                "id": 3,
                "product_info": 3,
                "quantity": 1
            }
        ],
        "state": "new",
        "dt": "2021-12-26T07:01:08.683656Z"
    }
]
```

## Покупатель
#### Отображение корзины
```
GET /api/v1/user/basket
Authorization: Token 05b0897fc95950b403f0f81330d3fdb63c4ab960

200 OK
[
    {
        "id": 1,
        "ordered_items": [
            {
                "id": 1,
                "product_info": 1,
                "quantity": 2
            },
            {
                "id": 2,
                "product_info": 2,
                "quantity": 1
            }
        ],
        "state": "basket",
        "dt": "2021-12-26T06:26:22.390546Z"
    }
]
```
#### Добавление позиций в корзину
```
POST /api/v1/user/basket
Authorization: Token 05b0897fc95950b403f0f81330d3fdb63c4ab960
{
    "ordered_items": [
                {
                    "product_info": 1,
                    "quantity": 2
                }
            ]
}

200 OK
{
  "Status": true,
  "Создано позиций": 1
}
```
#### Удаление позиций из корзины
```
DELETE /api/v1/user/basket
Authorization: Token 05b0897fc95950b403f0f81330d3fdb63c4ab960
{
    "ordered_items": [
                {
                    "product_info": 1 
                }
            ]
}

200 OK
{
  "Status": true,
  "Удалено позиций": 1
}
```
#### Редактирование позиций в корзине
```
PUT /api/v1/user/basket
Authorization: Token 05b0897fc95950b403f0f81330d3fdb63c4ab960
{
    "ordered_items": [
                {
                    "product_info": 1,
                    "quantity": 5
                }
            ]
}

200 OK
{
  "Status": true,
  "Обновлено позиций": 1
}
```

#### Отображение заказов
```
GET /api/v1/user/orders
Authorization: Token 05b0897fc95950b403f0f81330d3fdb63c4ab960

200 OK
[
    {
        "id": 2,
        "ordered_items": [
            {
                "id": 3,
                "product_info": 3,
                "quantity": 1
            }
        ],
        "state": "new",
        "dt": "2021-12-26T07:01:08.683656Z"
    }
]
```
#### Создание заказа из корзины
```
POST /api/v1/user/orders
Authorization: Token 05b0897fc95950b403f0f81330d3fdb63c4ab960

{
    "id": 6
}    

200 OK
```