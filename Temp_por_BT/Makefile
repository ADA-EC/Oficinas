#
# Sistema de Monitoramento de Compostagem
#
# Tem como proposito monitorar as leiras do grupo GEISA (USP-SC)
#
# Copyright (C) 2018 ADA-Projetos em Engenharia de Computacao
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Pedro V. B. Jeronymo (pedrovbj@gmail.com)
#
NAME=main
PORT=/dev/ttyACM0
MICRO=168
CPU_F=8000000
OBJ = main.o bluetooth/bluetooth.o ds18b20/ds18b20.o
CFLAGS=-Os -DF_CPU=$(CPU_F)

all: exe
	avr-objcopy -O ihex -R .eeprom $(NAME).out $(NAME).hex

exe: $(OBJ)
	avr-gcc -mmcu=atmega$(MICRO) $(OBJ) -o $(NAME).out

%.o: %.c
	avr-gcc -c -o $@ $< $(CFLAGS) -std=c11 -mmcu=atmega$(MICRO)

upload: all
	avrdude -c avrisp -p m$(MICRO) -P $(PORT) -b 19200 -U flash:w:$(NAME).hex

clean:
	rm $(OBJ)
	rm $(NAME).out
	rm $(NAME).hex
