test = {
  'name': '6.4',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Maybe there's a typo?
          >>> 'int_list' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Maybe there's a typo?
          >>> 'tens_list' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # Your list is off. Maybe there's a typo?
          >>> int_list == [1,2,3,4,5,6,7,8,9,10]
          True
          """
        },
        {
          'code': r"""
          >>> # Your loop is off.
          >>> item == 10
          True
          """
        }
      ]
    }
  ]
}