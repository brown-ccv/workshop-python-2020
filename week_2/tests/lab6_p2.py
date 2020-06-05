test = {
  'name': '6.2',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Maybe there's a typo?
          >>> 'sentence_str' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # Your loop is off.
          >>> sentence_str == 'My name is: Willie'
          True
          """
        },
      ]
    }
  ]
}