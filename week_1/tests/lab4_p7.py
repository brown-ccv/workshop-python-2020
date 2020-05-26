test = {
  'name': '4.7',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you don't have a variable
          >>> # named prices_dict. Maybe there's a typo?
          >>> 'prices_dict' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # Something in prices_dict is not correct.
          >>> prices_dict == {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}
          True
          """
        }
      ]
    }
  ]
}