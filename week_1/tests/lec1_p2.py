test = {
  'name': 'ex2',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Remember, the variable name should start with compvars_ab_ 
          >>> # and it should end with the type of the variable (bool).
          >>> # Maybe there's a typo?
          >>> 'compvars_ab_bool' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The variable name is good but the value is off.
          >>> # a_int = 3, and b_int = 9.1
          >>> # What's type(a_int) and type(b_int)? 
          >>> compvars_ab_bool == False
          True
          """
        }
      ]
    }
  ]
}