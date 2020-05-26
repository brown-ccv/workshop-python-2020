test = {
  'name': 'lab1_p1',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Please check for a typo. The variable name should be 
          >>> # my_favorite_things_lst
          >>> 'my_favorite_things_lst' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The variable name is good you need to have at least three values.
          >>> len(my_favorite_things_lst) >= 3
          True
          """
        }
      ]
    }
  ]
}