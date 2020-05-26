test = {
  'name': 'lab3_p4b',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # The variable name is incorrect.
          >>> # It should start with var1_ and end with the variablee type (int, flt, str, etc).
          >>> 'var1_int' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The variable was named correctly but its value is off.
          >>> # We need the 5th element of the second list in nested_lst.
          >>> var1_int == 5
          True
          """
        }
      ]
    }
  ]
}