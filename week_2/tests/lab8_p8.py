test = {
  'name': '8.8',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like one of your variables is not named
          >>> # correctly. Maybe there's a typo?
          >>> 'groc_tot_flt' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # It looks like your function returns the wrong result.
          >>> # Check your function.
          >>> groc_tot_flt == 7.5
          True
          """
        },
      ]
    }
  ]
}