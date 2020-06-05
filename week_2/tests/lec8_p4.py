test = {
  'name': '8.4',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Maybe there's a typo?
          >>> 'a1_int' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Maybe there's a typo?
          >>> 'a2_int' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Maybe there's a typo?
          >>> 'b1_int' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Maybe there's a typo?
          >>> 'b2_int' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # Your function is off for input=10,20
          >>> a1_int == 30
          True
          """
        },
        {
          'code': r"""
          >>> # Your function is off for input=10,20
          >>> a2_int == 200
          True
          """
        },
        {
          'code': r"""
          >>> # Your function is off for input=5,9
          >>> b1_int == 14
          True
          """
        },
        {
          'code': r"""
          >>> # Your function is off for input=5,9
          >>> b2_int == 45
          True
          """
        }
      ]
    }
  ]
}