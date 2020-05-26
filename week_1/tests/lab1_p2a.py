test = {
  'name': 'lab1_p2a',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Remember, we want a boolian variable that starts with somenum_
          >>> 'somenum_bool' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The variable name is good but the value is off.
          >>> # Print the type of somenum_int. What type should it be based on the variable name?
          >>> # Are the two types the same?
          >>> somenum_bool == True
          True
          """
        }
      ]
    }
  ]
}