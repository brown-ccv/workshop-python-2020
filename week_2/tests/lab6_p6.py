test = {
  'name': '6.6',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Maybe there's a typo?
          >>> 'dog_str' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # Your loop is off.
          >>> dog_str == 'Willie likes sleeping and eating '
          True
          """
        },
      ]
    }
  ]
}