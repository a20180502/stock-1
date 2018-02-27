# 指数数据
# 中证指数官网:http://www.csindex.com.cn/zh-CN/indices/index
# 中证指数：http://www.csindex.com.cn/zh-CN/indices/index-detail/000908?earnings_performance=5%E5%B9%B4&data_type=json
import pandas as pd
import urllib.request
import json

class Index(object):
	"""docstring for Index"""
	def __init__(self):
		self.title = '各类指数信息'

# 中证指数,参数指数代码
	def csindex(self,code):
		url = 'http://www.csindex.com.cn/zh-CN/indices/index-detail/{}?earnings_performance=5%E5%B9%B4&data_type=json'.format(code)
		data = urllib.request.urlopen(url).read()
		return pd.DataFrame(json.loads(data))
