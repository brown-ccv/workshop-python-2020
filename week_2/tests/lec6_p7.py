cities_dict = {'BOS': 'Boston',
          'NYC': 'New York City',
          'LAX': 'Los Angeles'}

test = {
  'name': '6.7',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Maybe there's a typo?
          >>> 'cities_list' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # Your list comprehension is off. Maybe there's a typo?
          >>> cities_list == [v for v in cities_dict.values()]
          True
          """
        }
      ]
    }
  ]
}