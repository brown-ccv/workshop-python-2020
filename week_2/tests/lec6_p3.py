test = {
  'name': '6.3',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Maybe there's a typo?
          >>> 'years_list' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # Your list is off. Maybe there's a typo?
          >>> years_list == [1995, 1964, 1961, 1993]
          True
          """
        },
        {
          'code': r"""
          >>> # Your first loop is off.
          >>> i == 3
          True
          """
        }
      ]
    }
  ]
}