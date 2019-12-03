# prices2
Nueva version 2.0 de la app prices  desarrollada con django.

se compone de las aplicaciones:
* gestionTiendas -> gestion de las tiendas disponibles
* gestionArticulos -> gestion de los articulos disponibles
* gestionClientes -> gestion de los usuarios/clientes que haran las compras
* gestionPrecios -> gestion de los precios de los articulos en las tiendas que correspondan
* gestionListaCompra -> gestion de las listas de la compra con los articulos que desean los clientes




- creacion de las apps dentro del proyecto
python manage.py startapp gestionTiendas

- chequeo de la apliaccion
python manage.py check gestionListaCompra

- creacion de la base de datos
python manage.py makemigrations
