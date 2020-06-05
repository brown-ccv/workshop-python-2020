test = {
  'name': '6.7',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Maybe there's a typo?
          >>> 'new_nums_list' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # Your loop is off.
          >>> new_nums_list == [3, 6, 9, 15, 21]
          True
          """
        },
      ]
    }
  ]
}