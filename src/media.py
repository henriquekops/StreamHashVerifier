#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
from io import TextIOWrapper
from os import SEEK_END

# project dependencies
from src.sha import sha

__author__ = "Henrique Kops"

MODE = "rb"
CHUNK = 1024


def encode(path:str) -> str:
	try:
		f = open(path, MODE)
		return iter(f)
	finally:
		f.close()


def iter(f:TextIOWrapper) -> str:
	f_size = f.seek(0, SEEK_END)
	pointer = f_size % CHUNK
	times = (f_size // CHUNK) + 1
	h:bytes = None
	for _ in range(times):
		f.seek(-pointer, SEEK_END)
		h = sha(f.read(CHUNK), h)
		pointer += CHUNK
	return h.hex()
