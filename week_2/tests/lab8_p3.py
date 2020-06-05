test = {
  'name': '8.3',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like one of your variables is not named
          >>> # correctly. Maybe there's a typo?
          >>> 'lloyd_avg_flt' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # It looks like your function returns the wrong result.
          >>> # Check your function.
          >>> lloyd_avg_flt == 80.55
          True
          """
        },
      ]
    }
  ]
}