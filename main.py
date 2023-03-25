# Version: 1.0
# Project: Sample API Rest (Flask) Python 3.9
# Author: Luis Rachope
# Date: 20/03/2022 16:55:34
#Para levantar a API na porta 5000, utilize o prompt de comando e digite "python main.py" dentro da pasta do projeto.

import src.server.instance as server
from src.controllers.books import *

server.run()

