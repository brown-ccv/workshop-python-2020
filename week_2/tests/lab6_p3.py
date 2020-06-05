test = {
  'name': '6.3',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Maybe there's a typo?
          >>> 'word_list' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # Your loop is off.
          >>> word_list == ["Willie", "likes", "sleeping", "and", "eating"]
          True
          """
        },
      ]
    }
  ]
}