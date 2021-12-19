import sys

import sys
import os

from cx_Freeze import Executable, setup


files = ['Controls','GUI','Icons','Interface','LOGIC','chromedriver.exe' ]

exe=Executable(script='app.py', base='Win32GUI')

setup(
    name='SE2 AMZ SCRAPER',
    version='1.0',
    description='Aplicación para realizar scraping de datos de amazon',
    author='NanoElMagno SE2-Code',
    options={'build_exe':{'include_files':files}},
    executables=[exe]
)