#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# built-in dependencies
import time
from sys import argv, exit

# project dependencies
from src.media import encode

__author__ = "Henrique Kops"

HELP = "Usage:\n\tpython main.py < video file >"


if __name__ == "__main__":

	if len(argv) != 2:
		print(HELP)
		exit(0)

	file_path = argv[1]

	s = time.time()

	h0 = encode(file_path)
	
	e = time.time()

	print(f"SHA256 of the first block (1024b) = {h0}")
	print(f"time elapsed = {e-s}")
