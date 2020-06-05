exercise_list = [10, 20, 30, 40, 50, 100]

test = {
  'name': '6.5',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Maybe there's a typo?
          >>> 'doubles_list' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # Your list comprehension is off. Maybe there's a typo?
          >>> doubles_list == [item*2 for item in exercise_list]
          True
          """
        },
      ]
    }
  ]
}