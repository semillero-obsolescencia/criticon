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
pi@raspberrypi:~/code/criticon/init $ sudo systemctl start criticon.service
pi@raspberrypi:~/code/criticon/init $ sudo systemctl status criticon.service
```
