# Criticón

Carrito de mercado autónomo de generación de discursos estéticos.


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

## Como se genera el discurso crítico del Criticón ?

La crítica de arte es una forma de analizar y evaluar las obras de arte, por lo tanto es una actividad que generalmente implica la emisión de un juicio estético.  La crítica de arte es usualmente un problema intelectual que depende del contexto cultural en el que se realiza, por lo tanto, a pesar de que la crítica busca la interpretación racional del arte, lo que se considera una buena o mala obra de arte depende de situaciones contingentes del momento, lugar y la subjetividad desde la que se realiza la crítica.

Uno de los problemas de hacer una máquina que realize crítica de arte es que los computadores procesan la información en términos absolutos y cuantitativos, mientras que los seres humanos pensamos, apreciamos y nos referimos a la creación artística en términos cualitativos, no cuantitativos.

Esta contradicción es parte fundamental del funcionamiento del criticón.  Cuando una obra ( representada por un código de barras ) es detectada, el criticón asigna un puntaje que, por el momento, es un número decimal generado aleatoriamente en el rango que va de 0.1 a 5.0 .  Si el puntaje se encuentra entre 0.1 y 1.6, el juicio emitido por el criticón es negativo, si se encuentra entre 1.67 y 3.33 el juicio es neutral, y si se encuentra entre 3.34 y 5.0, el juicio es positivo.

De acuerdo a si el juicio es negativo, neutral o positivo, el criticón genera una frase, o conjunto de frases acordes. Criticón genera este discurso a partir de una serie de plantillas que usa para crear permutaciones o combinaciones de elementos que componen una frase.  Las plantillas son documentos de texto plano que contienen la estructura de la frase y los elementos que pueden entrar en cada parte de la estructura.  Cuando un código es escaneado, el criticón elige una de las plantillas y construye un conjunto de frases, usando todas las combinaciones posibles de los elementos en la plantilla, usando siempre la estructura definida en la misma, luego selecciona únicamente una de las frases y la pronuncia.

El siguiente es un ejemplo de plantilla que genera una apreciación negativa:

```
# critica negativa 01
SENTENCE -> NOUN VERB ADJ;
NOUN -> "Esta obra";
VERB -> "es";
ADJ -> "fea" | "horrible" | "simple";
```

Que generaría una frase como esta:

"Esta obra es fea"

Este es probablemente el ejemplo más básico de crítica de arte, y a pesar de que no se requiere mucho trabajo intelectual para llegar a una conclusión así, pero sirve como ejemplo para entender como generar frases más complejas.

Este sistema de generación de textos en lenguaje natural proviene de la implementación de la librería [nlgen](https://github.com/toumorokoshi/nlgen), que usa un lenguaje de marcado propio que se encuentra documentado aquí:

[http://nlgen.readthedocs.io/]


### Cómo alimentar el discurso del Criticón ?

Para alimentar el discurso del Criticón sólo hace falta crear nuevas plantillas usando el lenguaje de marcado de nlgen e incluir las plantillas en alguna de las siguientes carpetas: 

```
data/negativo
data/neutral
data/positivo
```

El código del Criticón contiene una plantilla de ejemplo en cada carpeta ( que en últimas es una categora ).  Es posible agregar nuevas plantillas, el Criticón elegirá una aleatoriamente y generará y elegirá una frase a partir de esta.


### Fuentes tipográficas para el Criticon2000

Dynamixion Script

https://www.fontsquirrel.com/fonts/DymaxionScript?q%5Bterm%5D=retro&q%5Bsearch_check%5D=Y

Top Speed

http://www.dafont.com/top-speed.font


## Referencias

Soporte para voces en festival

https://www.raspberrypi.org/forums/viewtopic.php?f=76&t=123283
https://vijamaroylinux.blogspot.com.co/2008/12/festival-un-conversor-de-texto-voz.html
