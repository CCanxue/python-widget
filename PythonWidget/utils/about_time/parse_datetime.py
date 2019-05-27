# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2018-02-08 14:01:56
# @Last Modified by:   liangxiaodong
# @Last Modified time: no
from datetime import datetime

def parse_datetime(dt):
    strd = str(dt)
    table = bytes.maketrans(b'-:.', b'___')
    return str(bytes(strd, encoding='utf-8').translate(table), encoding='utf-8')


def parse_datetime2(dt):
    strd = str(dt)
    table = str.maketrans('-:.', '___')
    return strd.translate(table)


if __name__ == "__main__":
    print(parse_datetime(datetime.now()))
    print(parse_datetime2(datetime.now()))