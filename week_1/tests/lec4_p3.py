test = {
  'name': '4.3',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like the key 9 does not exist.
          >>> # Maybe there's a type error?
          >>> 9 in phone_nums_dict
          True
          """
        },
        {
          'code': r"""
          >>> # The value assigned to the key 9 is
          >>> # not correct. 
          >>> phone_nums_dict[9] == 27
          True
          """
        }
      ]
    }
  ]
}