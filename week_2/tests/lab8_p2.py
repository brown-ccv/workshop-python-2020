test = {
  'name': '8.2',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like one of your variables is not named
          >>> # correctly. Maybe there's a typo?
          >>> 'avg_flt' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # It looks like your function returns the wrong result.
          >>> # Check your function.
          >>> avg_flt == 2.0
          True
          """
        },
      ]
    }
  ]
}