test = {
  'name': 'l5p2',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It seems the has_a_e_bool variable was not created.
          >>> # Typo?
          >>> 'has_a_e_bool' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # Something is off with your if statement.
          >>> # Please test your code by trying out all possibilities
          >>> ((('a' in my_str) or ('e' in my_str)) and (has_a_e_bool == True)) or (('a' not in my_str) and ('e' not in my_str) and (has_a_e_bool == False))
          True
          """
        }
      ]
    }
  ]
}