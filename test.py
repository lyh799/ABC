#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

# with open("conf.json") as f:
#     json_data = f.read()

# p1 = json_data.find('"db_server"')
# p2 = json_data.find(",", p1)
# db_server = json_data[p1 + len('"db_server": "') : p2 - 1]
# print(db_server)

conf = json.load(open("conf.json"))
print(conf["db_server"], conf["db_user"])
