test = {
  'name': 'lab3_p3b',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It seems sub_lst was not created.
          >>> # Maybe a typo?
          >>> 'sub_lst' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # It seems the slicing is not correct.
          >>> sub_lst == [16, 14, 12, 10, 8, 6, 4, 2]
          True
          """
        }
      ]
    }
  ]
}