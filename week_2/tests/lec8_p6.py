test = {
  'name': '8.6',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Maybe there's a typo?
          >>> 'res1_str' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Maybe there's a typo?
          >>> 'res2_str' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # Your function is off for input.
          >>> res1_str == 'dog ran'
          True
          """
        },
        {
          'code': r"""
          >>> # Your function is off for input.
          >>> res2_str == 'dog ate'
          True
          """
        }
      ]
    }
  ]
}