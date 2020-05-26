test = {
  'name': '4.9',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Something in prices_dict is not correct.
          >>> prices_dict == {'banana': 4, 'apple': 2, 'pear': 3}
          True
          """
        }
      ]
    }
  ]
}