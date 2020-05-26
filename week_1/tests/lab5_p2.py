test = {
  'name': 'lab5p2',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It seems the can_enter_bool variable was not created.
          >>> # Typo?
          >>> 'can_enter_bool' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # Something is off with your if statement.
          >>> # Please test your code by trying out all possibilities.
          >>> ((age_int >= 8) and (age_int <= 12) and (can_enter_bool == True)) or (((age_int < 8) or (age_int > 12)) and (can_enter_bool == False))
          True
          """
        }
      ]
    }
  ]
}