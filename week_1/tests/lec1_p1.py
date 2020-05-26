test = {
  'name': 'ex1',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Remember, the variable name should start with ans1_ 
          >>> # and it should end with the type of the variable (int or flt).
          >>> # Maybe there's a typo?
          >>> 'ans1_flt' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The variable name is good but the value is off.
          >>> # a_int is 5, b_int is 8.
          >>> ans1_flt == 0.625
          True
          """
        }
      ]
    }
  ]
}