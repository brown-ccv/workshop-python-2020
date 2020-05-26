test = {
  'name': 'lab1_p3b',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # someothernum_int is an integer and we multiply it with 2.25.
          >>> # Print out the type of someothernum_int and 2.2.5 and their product.
          >>> # If the product is a float, you need to create a new variable.
          >>> 'someothernum_flt' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The variable name is good but the value is off.
          >>> # Are you sure you multiplied somenum_int by 2?
          >>> someothernum_flt == 67*2.25
          True
          """
        }
      ]
    }
  ]
}