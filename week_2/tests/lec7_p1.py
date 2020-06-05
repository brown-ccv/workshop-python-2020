test = {
  'name': 'l7p1',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It seems the oldies_lst list was not created.
          >>> # Typo?
          >>> 'nums_lst' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # It seems the list elements are off.
          >>> nums_lst == [24, 4567, 582, 78, 12, 675]
          True
          """
        }  
      ]
    }
  ]
}