test = {
  'name': 'lab3_p4c',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # The variable name is incorrect.
          >>> # It should be first_name_str.
          >>> 'first_name_str' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The variable value is off. Are you sure you selected your first name correctly?
          >>> first_name_str == nested_lst[2][0]
          True
          """
        }
      ]
    }
  ]
}