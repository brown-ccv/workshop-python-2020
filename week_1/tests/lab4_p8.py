test = {
  'name': '4.8',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you don't have a variable
          >>> # named profit_flt. Maybe there's a typo?
          >>> 'profit_flt' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The value of profit_flt is not correct.
          >>> profit_flt == sum(prices_dict.values())
          True
          """
        }
      ]
    }
  ]
}