test = {
  'name': '8.4',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like one of your variables is not named
          >>> # correctly. Maybe there's a typo?
          >>> 'lloyd_avg_str' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # It looks like your function returns the wrong result.
          >>> # Check your function.
          >>> lloyd_avg_str == 'B'
          True
          """
        },
      ]
    }
  ]
}