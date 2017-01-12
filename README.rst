=========
pywe-base
=========

Wechat Base Class for Python.

Installation
============

::

    pip install pywe-base


Usage
=====

::

    In [1]: from pywe_base import BaseWechat

    In [7]: class XXX(BaseWechat):
       ...:     pass
       ...:

    In [3]: xxx = XXX()

    In [4]: xxx.API_DOMAIN
    Out[4]: 'https://api.weixin.qq.com'

    In [5]: xxx.OPEN_DOMAIN
    Out[5]: 'https://open.weixin.qq.com'

    In [6]: xxx._requests
    Out[6]: <bound method XXX._requests of <__main__.XXX object at 0x7f9248260d10>>

    In [7]:

