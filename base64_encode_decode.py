# -*- coding: utf-8 -*-

"""
  @Author: xuanyuwu
  @File: base64_encode_decode.py
  @Date: 2023/7/24
  @Description: None.
"""
import sys
import base64

from workflow import Workflow3


def process(query_str):
    wf = Workflow3()

    # 判断是否为Base64编码
    try:
        decoded_string = base64.b64decode(query_str)
        wf.add_item(title="Decode: %s" % decoded_string, valid=True, copytext=decoded_string, arg=decoded_string)
    except Exception:
        encoded_string = base64.b64encode(query_str)
        wf.add_item(title="Encode: %s" % encoded_string, valid=True, copytext=encoded_string, arg=encoded_string)

    # 向Alfred输出结果
    wf.send_feedback()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        exit(0)

    query = sys.argv[1]
    process(query)
