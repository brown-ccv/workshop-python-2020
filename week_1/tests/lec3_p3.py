test = {
  'name': 'd3p3',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # The items aren't sorted correctly yet.
          >>> # Sorted numbers first followed by the sorted names
          >>> # All in the same list.
          >>> spam_lst == [1,2,3,4,'Alice','Bob','Kallie']
          True
          """
        }
      ]
    }
  ]
}