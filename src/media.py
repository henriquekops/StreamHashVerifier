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
	"""Encoding entrypoint

	Args:
		path (str): file path of the media to be encrypted by SHA256

	Returns:
		str: first 1024 SHA256 block of the media file
	"""
	try:
		f = open(path, MODE)
		return iter(f)
	finally:
		f.close()


def iter(f:TextIOWrapper) -> str:
	"""Media file iterator

	Args:
		f (TextIOWrapper): media file to be encrypted by SHA256

	Returns:
		str: first 1024 SHA256 block of the media file
	"""
	f_size = f.seek(0, SEEK_END)
	pointer = f_size % CHUNK
	times = (f_size // CHUNK) + 1
	h:bytes = None
	for _ in range(times):
		f.seek(-pointer, SEEK_END)
		h = sha(f.read(CHUNK), h)
		pointer += CHUNK
	return h.hex()
