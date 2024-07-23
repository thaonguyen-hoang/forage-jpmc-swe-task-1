import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # dataPoint = ('ABC', 120.48, 121.2, (120.48 + 121.2) / 2)
    # self.assertEqual(getDataPoint(quotes[0]), dataPoint)
    # dataPoint = ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)
    # self.assertEqual(getDataPoint(quotes[1]), dataPoint)

    """---Model answer---"""
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    dataPoint = ('ABC', 120.48, 119.2, (120.48 + 119.2) / 2)
    self.assertEqual(getDataPoint(quotes[0]), dataPoint)
    dataPoint = ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)
    self.assertEqual(getDataPoint(quotes[1]), dataPoint)

  """ ------------ Add more unit tests ------------ """
  def test_getRatio_calculateRatio(self):
    self.assertEqual(getRatio(10.0, 0.0), None)
    self.assertEqual(getRatio(0.0, 21.5), 0.0)
    self.assertEqual(getRatio(10.0, 5.0), 2.0)

if __name__ == '__main__':
    unittest.main()
