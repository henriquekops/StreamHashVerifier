#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# external dependencies
from Crypto.Hash import SHA256

UTF_8 = "utf-8"

def sha(msg: str) -> str:
	hash = SHA256.new()
	hash.update(msg.encode(UTF_8))
	return hash.digest()
