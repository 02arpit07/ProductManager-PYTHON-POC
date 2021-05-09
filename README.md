# ProductManager-PYTHON-POC

I have created a web-app and api's using DJANGO and DJANGO REST FRAMEWORK respectively.

After downloading the repository
Run it using->    python manage.py runserver


Now check this url-> yOU WILL ABLE TO USE APP WITH FRONTEND 
http://127.0.0.1:8000/

=> You will land on Python webapp, where you can perform all crud operations.




Now if you want to access the Api 's 
You can check it on postman


GetallProducts
GET
http://127.0.0.1:8000/api/product


GetProductById
GET
http://127.0.0.1:8000/api/detail/1



PostProduct
POST
http://127.0.0.1:8000/api/product/

Note-: Please make sure you have selected body -> form-data and inserted the product_image as file. and entered all other fields too.



DeleteProductById
DELETE
http://127.0.0.1:8000/api/detail/6/



UpdateProductById
PUT
http://127.0.0.1:8000/api/detail/1/

Note-: Please make sure you have selected body -> form-data and inserted the product_image as file. and entered all other fields too.
