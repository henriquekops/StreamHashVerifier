#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# external dependencies
from Crypto.Hash import SHA256

__author__ = "Henrique Kops"


def sha(msg:str, h:str) -> str:
	"""SHA256 wrapper function

	Args:
		msg (str): message to apply SHA256
		h (str): previously calculated SHA256

	Returns:
		str: SHA256 over msg and h (if exists) 
	"""
	hash = SHA256.new()
	hash.update(msg)
	if h: hash.update(h)
	return hash.digest()
