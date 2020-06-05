test = {
  'name': '6.6',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Maybe there's a typo?
          >>> 'cities_dict' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # Your list is off. Maybe there's a typo?
          >>> key == 'LAX'
          True
          """
        },
        {
          'code': r"""
          >>> # Your list is off. Maybe there's a typo?
          >>> value == 'Los Angeles'
          True
          """
        }
      ]
    }
  ]
}