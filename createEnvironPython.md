### Crear Entornos virtuales sin anaconda

1. Creamos una carpeta donde trabajaremos nuestro proyecto
2. creamos un entorno virtual para trabajar
2.1 ```python python3 -m venv <nombredelentorno> ```
2.2 Luego activamos el entorno: ```sh source nombredelentorno/bin/activate ```
2.3 Instalamos paquetes si los necesitamos:
```sh
pip3 install paquete_que_deseas_instalar
```
4. Luego instalamos pipx, pipx es una herramienta que nos permite instalar y ejecutar paquetes de Python en entornos virtuales,
 y gestionará esos entornos virtuales automáticamente por nosotros.Podemos instalar pipx utilizando pip:
```sh pip install pipx```
6. Si queremos descativar el entorno simplemente escribimos: ```sh deactivate```
