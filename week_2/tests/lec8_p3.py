test = {
  'name': '8.3',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Maybe there's a typo?
          >>> 'res1_flt' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Maybe there's a typo?
          >>> 'res2_flt' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # Your function is off for input=10,20
          >>> res1_flt == 15.0
          True
          """
        },
        {
          'code': r"""
          >>> # Your function is off for input=16,16
          >>> res2_flt == 16.0
          True
          """
        }
      ]
    }
  ]
}