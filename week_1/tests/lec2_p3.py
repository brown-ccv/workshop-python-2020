test = {
  'name': '2.3',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # exercise_str.  Maybe there's a typo?
          >>> 'exercise_str' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The value assigned to exercise_str is
          >>> # not correct. 
          >>> exercise_str == 'This is a sentence that I have assigned to the variable, "exercise string".'
          True
          """
        }
      ]
    }
  ]
}