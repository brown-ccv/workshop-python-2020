test = {
  'name': 'lab1_p1a',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Remember, we want to save the value of  pi as a variable.
          >>> # What type should the variable be?
          >>> # Start the variable name with pi_
          >>> 'pi_flt' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The variable name is good but the value is off.
          >>> # Seems like a typo.
          >>> pi_flt == 3.1416
          True
          """
        }
      ]
    }
  ]
}