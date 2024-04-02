### Crear Entornos virtuales sin anaconda

- Creamos una carpeta donde trabajaremos nuestro proyecto

- creamos un entorno virtual para trabajar:
```sh
python3 -m venv <nombredelentorno>
```

- Luego activamos el entorno:
```sh
source nombredelentorno/bin/activate
```

- Instalamos paquetes si los necesitamos:
```sh
pip3 install paquete_que_deseas_instalar
```

- Luego instalamos pipx, pipx es una herramienta que nos permite instalar y ejecutar paquetes de Python en entornos virtuales y gestionará esos entornos virtuales automáticamente por nosotros.Podemos instalar pipx utilizando pip:
```sh
pip install pipx
```

- Si queremos descativar el entorno simplemente escribimos:
```sh
deactivate
```
