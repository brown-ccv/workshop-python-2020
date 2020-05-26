test = {
  'name': 'l5p3',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It seems the compare_str variable was not created.
          >>> # Typo?
          >>> 'compare_str' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # Something is off with your if statement.
          >>> # Please test your code by trying out all possibilities.
          >>> ((x_int > y_int) and (compare_str == 'larger')) or ((x_int == y_int) and (compare_str == 'equal')) or ((x_int < y_int) and (compare_str == 'smaller'))
          True
          """
        }
      ]
    }
  ]
}