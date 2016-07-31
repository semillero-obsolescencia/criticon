# Criticón

Carrito de mercado autónomo de generación de discursos estéticos.


# Instalación

En linux (raspbian jessie ) necesitará instalar `festival`, `espeak` y `zbar`:

```
sudo apt-get install festival festival-dev espeak zbar-tools libzbar-dev
```

Instalar la voz en español de festival

```sudo apt-get install festvox-ellpc11k```

Instalar opencv 3 en raspberrypi:

http://www.pyimagesearch.com/2015/10/26/how-to-install-opencv-3-on-raspbian-jessie/un

Soporte para voces en festival


https://www.raspberrypi.org/forums/viewtopic.php?f=76&t=123283

Clonar el repositorio e instalar las librerías de python:

```
pip install -r requirements.txt
```


# Script de inicio
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
