test = {
  'name': '8.1',
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
          >>> # It looks like your variable is not named correctly.
          >>> # Maybe there's a typo?
          >>> 'res3_int' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # Your function gives the incorrect answer for
          >>> # input = 1. 
          >>> res1_int == 2
          True
          """
        },
         {
          'code': r"""
          >>> # Your function gives the incorrect answer for
          >>> # input = 9. 
          >>> res2_int == 18
          True
          """
        },
         {
          'code': r"""
          >>> # Your function gives the incorrect answer for
          >>> # input = 19. 
          >>> res3_int == 38
          True
          """
        }
      ]
    }
  ]
}