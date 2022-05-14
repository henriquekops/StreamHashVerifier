#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# external dependencies
from Crypto.Hash import SHA256


def sha(msg:str, h:str) -> str:
	hash = SHA256.new()
	hash.update(msg)
	if h: hash.update(h)
	return hash.digest()
