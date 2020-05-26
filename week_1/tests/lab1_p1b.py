test = {
  'name': 'lab1_p1b',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Remember, we want to save the value 86400 as a variable.
          >>> # What type should the variable be?
          >>> # Start the variable name with seconds_in_day_
          >>> 'seconds_in_day_int' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The variable name is good but the value is off.
          >>> # Seems like a typo.
          >>> seconds_in_day_int == 86400
          True
          """
        }
      ]
    }
  ]
}