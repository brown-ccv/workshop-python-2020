test = {
  'name': 'lab1_p2c',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Remember, we want a boolian variable that starts with whatevs_
          >>> 'whatevs_bool' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The variable name is good but the value is off.
          >>> # Print the type of whatevs_flt. What type should it be based on the variable name?
          >>> # Are the two types the same?
          >>> whatevs_bool == True
          True
          """
        }
      ]
    }
  ]
}