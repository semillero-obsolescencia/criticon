# Criticón

Carrito de mercado autónomo de generación de discursos estéticos. Esta es la version genérica.
Y esta es otra versión 


# Instalación

Bajar el código del proyecto

```
git clone git@github.com:semillero-obsolescencia/criticon.git
```

## 1: Instalar opencv 3 en raspberrypi:

Para instalar opencv3 en raspberrypi seguir este tutorial:

http://www.pyimagesearch.com/2015/10/26/how-to-install-opencv-3-on-raspbian-jessie/un

O hacer la mas fácil: usar el script de instalación incluído en el codigo:

**Advertencia: Este script fué probado en raspbian Jessie, y compila e instala opencv3 para python3.**

```
cp criticon/misc/nstall-opencv.sh ./
sudo chmod +x install-opencv.sh
./install-opencv.sh
```

## 2: Instalar dependencias y paquetes para el proyecto

En linux (raspbian jessie ) necesitará instalar `festival` y `zbar`:

```
sudo apt-get install festival festival-dev espeak zbar-tools libzbar-dev
```

Instalar la voz en español de festival

```sudo apt-get install festvox-ellpc11k```


Instalar voces en español con soporte para acentos:

```
cd ~/
git clone https://github.com/guadalinex-archive/hispavoces.git
cd hispavoces/packages
sudo dpkg -i festvox-palpc16k_1.0-1_all.deb
sudo dpkg -i festvox-sflpc16k_1.0-1_all.deb
```

Clonar el repositorio del proyecto e instalar las librerías de python:

```
workon criticon
cd criticon
pip install -r requirements.txt
```

# Uso

Para iniciar el criticon debe activarse el entorno virtual de python, luego descender en el directorio del proyecto.

```
workon criticon
cd criticon
```

Luego  ejecutar el script ```criticon.py``` desde una terminal, o una conexion ssh:

```
python criticon.py
```

O si está corriendo  el servidor X y la interfaz gráfica de usuario en raspbian, es posible ejecutar el script con la opción ```-d``` para monitorear la cámara.

```
python criticon.py -d
```

## Script de inicio

Configuración de la raspberrypi para que inicie criticón automáticamente al iniciar el sistema.
```
sudo cp init/criticon.service /lib/systemd/system/
sudo chmod 644 /lib/systemd/system/criticon.service
sudo systemctl daemon-reload
sudo systemctl enable criticon.service
```

Para probarlo:

```
sudo systemctl start criticon.service
sudo systemctl status criticon.service
```

Para parar el servicio

```
sudo systemctl stop criticon.service
```


### Fuentes tipográficas para el Criticon2000

Dynamixion Script

https://www.fontsquirrel.com/fonts/DymaxionScript?q%5Bterm%5D=retro&q%5Bsearch_check%5D=Y

Top Speed

http://www.dafont.com/top-speed.font


## Referencias

Soporte para voces en festival

https://www.raspberrypi.org/forums/viewtopic.php?f=76&t=123283
https://vijamaroylinux.blogspot.com.co/2008/12/festival-un-conversor-de-texto-voz.html
