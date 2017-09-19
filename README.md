# Restaurant Chain Back End Doc

## A restaurant chain backend server built on Django rest framework

## Project Structure

![](https://i.imgur.com/GCSU2Y8.png)

---

## Supported Http Request Types
GET: Retrieves data from the server 
POST: Sends data to the server for a new entity. 
PUT: Used to replace an existing entity
DELETE: Removes data from the server.

## API Reference
  
### 1. GET
#### a. URL: http://localhost:8000/api/restaurants/
####  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   or   http://localhost:8000/api/restaurants/:id
desciption: Fetches the all/one the restaurant data in the database.
Sample response:
```
[
    {
    "restaurantId": 3,
    "restaurantName": "McDonald's (Long Island)",
    "restaurantLocation": "Long Island",
    "restaurantContact": "1599841561",
    "restaurantOpenTime": "18:01:18",
    "restaurantCloseTime": "18:01:19",
    "restaurantSales": {
        "sales": [
          140,
          360,
          60,
          300,
          70,
          700,
          100,
          200,
          200,
          400,
          200,
          600
        ],
    },
    "restaurantLongtitude": "-63.5846110000",
    "restaurantLatitude": "44.6354720000",
    "restaurantImage": "http://bevitahealthy.com/wp-content/uploads/2017/05/mc.jpg"
    },
    {
    "restaurantId": 4,
    "restaurantName": "McDonald's (Bedford Terminal)",
    "restaurantLocation": "Bedford Terminal",
    "restaurantContact": "789456123",
    "restaurantOpenTime": "18:01:18",
    "restaurantCloseTime": "18:01:19",
    "restaurantSales": {
        "sales": [
          210,
          20,
          500,
          800,
          300,
          800,
          100,
          500,
          60,
          300,
          100,
          900
        ],
    },
    "restaurantLongtitude": "-63.5846110000",
    "restaurantLatitude": "44.6354720000",
    "restaurantImage": "https://media-cdn.tripadvisor.com/media/photo-o/04/51/2a/54/mcdonald-s.jpg"
    }
    ,
    ...
]


```

#### b. URL: http://localhost:8000/api/recipes/
####  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   or   http://localhost:8000/api/recipes/:id
desciption: Fetches the all/one the recipes data in the database.
Sample response:
```
[
    {
    "recipeId": 1,
    "recipeName": "French Fries",
    "recipePrice": "2.00",
    "recipeDescription": "Hot served french fries",
    "recipeImagepath": "https://i.ytimg.com/vi/QTS4OlryASo/maxresdefault.jpg"
    },
    {
    "recipeId": 2,
    "recipeName": "Chicken Burger",
    "recipePrice": "5.00",
    "recipeDescription": "Juicy Chicken served with fresh lettuce and tomato.",
    "recipeImagepath": "https://sparkpeo.hs.llnwd.net/e1/resize/630m620/e2/guid/WW-Feta-Chicken-Burgers/b83e3206-f74a-459d-bfc6-c5718dc9bcd0.jpg"
    },
    ...
]

```

#### c. URL: http://localhost:8000/api/employees/
####  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   or   http://localhost:8000/api/employees/:id
desciption: Fetches the all/one the employees data in the database.
Sample response:

```
[
    {
    "employeeId": 4,
    "employeeBelong": 3,
    "employeeJobnumber": "APTX-4896",
    "employeeTitle": "Manager",
    "employeeSex": 1,
    "employeeFirstname": "Sadakane",
    "employeeLastname": "Shimazu",
    "employeeContact": "123456789",
    "employeeSalary": "1236.00",
    "employeePhoto": "https://timedotcom.files.wordpress.com/2017/06/jon-snow-fb.jpg?quality=85&w=560&h=374&crop=1"
    },
      {
    "employeeId": 5,
    "employeeBelong": 4,
    "employeeJobnumber": "APTX9011",
    "employeeTitle": "Cashier",
    "employeeSex": 1,
    "employeeFirstname": "Nikita",
    "employeeLastname": "Khrushchev",
    "employeeContact": "156149851",
    "employeeSalary": "3000.00",
    "employeePhoto": "http://digitalspyuk.cdnds.net/16/22/768x512/gallery-1464868156-got506-102814-hs-dsc-1130.jpg"
    },
    ...

]


```

### 2. POST
#### a. URL: http://localhost:8000/restaurants/
desciption: Create a new restaurant data in the database.

#### b. URL: http://localhost:8000/recipes/
desciption: Create a new restaurant data in the database.

#### c. URL: http://localhost:8000/employees/
Desciption: Create a new restaurant data in the database.


### 3. PUT/DELETE
#### a. URL: http://localhost:8000/restaurants/:id
Desciption: Update/Delete a new restaurant data in the database.

#### b. URL: http://localhost:8000/recipes/:id
Desciption: Update/Delete a new restaurant data in the database.

#### c. URL: http://localhost:8000/employees/:id
Desciption: Update/Delete a new restaurant data in the database.

---
## Database : SQLite3 

---


