test = {
  'name': '8.2',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Maybe there's a typo?
          >>> 'res1_int' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Maybe there's a typo?
          >>> 'res2_int' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # Your function is off for input=5,9
          >>> res1_int == 14
          True
          """
        },
        {
          'code': r"""
          >>> # Your function is off for input=10,20
          >>> res2_int == 30
          True
          """
        },
      ]
    }
  ]
}