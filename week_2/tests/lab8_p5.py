test = {
  'name': '8.5',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like one of your variables is not named
          >>> # correctly. Maybe there's a typo?
          >>> 'class_avg_flt' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # It looks like your function returns the wrong result.
          >>> # Check your function.
          >>> class_avg_flt == 83.86666666666666
          True
          """
        },
      ]
    }
  ]
}