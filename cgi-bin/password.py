#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import urllib2
import commands
import base64

def changed(panelname, panelpass):
	cmdcg = "changepanel " + panelname + " " + panelpass
	os.system(cmdcg)
