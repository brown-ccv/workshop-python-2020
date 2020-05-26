test = {
  'name': 'd3p1',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Remember, the variable name should start with var_ 
          >>> # and it should end with the type of the variable.
          >>> # Maybe there's a typo?
          >>> 'var_int' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The variable name is good but the value is off.
          >>> # Remember that we want the fourth element of the second list.
          >>> var_int == 40
          True
          """
        }
      ]
    }
  ]
}