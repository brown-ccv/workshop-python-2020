test = {
  'name': '6.1',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Maybe there's a typo?
          >>> 'my_numbers_list' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The elements in the list are off.
          >>> my_numbers_list == [10,20,30,40,50]
          True
          """
        },
        {
          'code': r"""
          >>> # The elements in the list are off.
          >>> item == 50
          True
          """
        }
      ]
    }
  ]
}