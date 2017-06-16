#!/usr/bin/env python
#coding=utf8

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")

import time
from sample_common import MNSSampleCommon
from mns.account import Account
from mns.queue import *

#从sample.cfg中读取基本配置信息
## WARNING： Please do not hard code your accessId and accesskey in next line.(more information: https://yq.aliyun.com/articles/55947)
accid,acckey,endpoint,token = MNSSampleCommon.LoadConfig()

#初始化 my_account, my_queue
my_account = Account(endpoint, accid, acckey, token)
queue_name = sys.argv[1] if len(sys.argv) > 1 else "MySampleQueue"
my_queue = my_account.get_queue(queue_name)

#删除队列
try:
    my_queue.delete()
    print "Delete Queue Succeed! QueueName:%s\n" % queue_name
except MNSExceptionBase, e:
    print "Delete Queue Fail! Exception:%s\n" % e
