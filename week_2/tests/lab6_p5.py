test = {
  'name': '6.5',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't use the format
          >>> # given in the problem. Maybe there's a typo?
          >>> 'phrase_str' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # Your loop is off.
          >>> phrase_str == 'and eating'
          True
          """
        },
      ]
    }
  ]
}