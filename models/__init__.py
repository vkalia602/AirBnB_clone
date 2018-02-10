#!/usr/bin/python3

"""models package"""
from .engine.file_storage import FileStorage

storage = FileStorage('file.json', {})
storage.reload()    # sets storage.objects to a json dict
