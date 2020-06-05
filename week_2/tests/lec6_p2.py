test = {
  'name': '6.2',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Maybe there's a typo?
          >>> 'this_str' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # this_str is off. Maybe there's a typo?
          >>> this_str == 'I am a dog.'
          True
          """
        },
        {
          'code': r"""
          >>> # Your first loop is off.
          >>> char == '.'
          True
          """
        },
        {
          'code': r"""
          >>> # Your second loop is off.
          >>> word == 'dog.'
          True
          """
        }
      ]
    }
  ]
}