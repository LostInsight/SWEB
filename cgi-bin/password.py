#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os

def set(panelname, panelpass):
	os.system("changepanel " + panelname + " " + panelpass)
