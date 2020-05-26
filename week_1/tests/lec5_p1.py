test = {
  'name': 'l5p1',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Maybe there's a typo?
          >>> ((len(my_lst) > 10) and (my_lst[-1] == 'yes') or (len(my_lst) <= 10) and (my_lst[-1] == 'no'))
          True
          """
        }
      ]
    }
  ]
}