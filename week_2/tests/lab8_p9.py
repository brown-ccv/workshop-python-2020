test = {
  'name': '8.9',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like one of your variables is not named
          >>> # correctly. Maybe there's a typo?
          >>> 'better_groc_tot_flt' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # It looks like your function returns the wrong result.
          >>> # Check your function.
          >>> better_groc_tot_flt == 5.5
          True
          """
        },
      ]
    }
  ]
}