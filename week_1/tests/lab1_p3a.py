test = {
  'name': 'lab1_p3a',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # somenum_int is an integer and we multiply it with another integer.
          >>> # Print out the type of somenum_int * 2.
          >>> # If it is an int, you can just update somenum_int, no need to create a new variable.
          >>> 'somenum_flt' not in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The variable name is good but the value is off.
          >>> # Are you sure you multiplied somenum_int by 2?
          >>> somenum_int == 327*2
          True
          """
        }
      ]
    }
  ]
}