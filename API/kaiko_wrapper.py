import unirest
import dateutil.parser
import datetime, time

api_key = "l47TFgwXpnmshAiGPqIzxOlhAVd9p116jKbjsn789BfxQhJJy9"
request_buckets = 20000

class Kaiko(object):

	@staticmethod
	def get_mempool_sizes(start, end):
		print("Mempool range (" + str(start) + "," + str(end) + ")")

		if (int(end) - int(start)) > request_buckets:
			time_dict = {}
			request_start = start
			request_end = start + request_buckets

			while(request_start < end):
				Kaiko.get_mempool_data(request_start, request_end, time_dict)
				request_start += request_buckets
				request_end += request_buckets

			return time_dict
		else:
			return Kaiko.get_mempool_data(start, end)

		
	@staticmethod
	def get_mempool_data(start, end, time_dict=None):
		print("Getting Mempool from Kaiko for (" + str(start) + "," + str(end) + ")")
		url = "https://kaiko-kaiko-private-v1.p.mashape.com/mempool?from=%s&to=%s" % (str(start), str(end))
		response = unirest.get(url,
		  headers={
		    "X-Mashape-Key": api_key,
		    "Accept": "application/json"
		  }
		)
		timestamps = response.body['ts']
		bytes = response.body['bytes']

		if time_dict is None:
			time_dict = {}
		
		epoch = datetime.datetime.utcfromtimestamp(0)
		for i, ts in enumerate(timestamps):
			# epoch time conversion
			date = dateutil.parser.parse(str(timestamps[i]))
			epoch = str(int(time.mktime(date.timetuple())))

			time_dict[epoch] = str(bytes[i])
		return time_dict # ("1462064399", "7381552")

