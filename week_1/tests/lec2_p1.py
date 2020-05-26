test = {
  'name': '2.1',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # another_uppercase_str.  Maybe there's a typo?
          >>> 'another_uppercase_str' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The value assigned to another_uppercase_str is
          >>> # not correct. 
          >>> another_uppercase_str == 'A'
          True
          """
        }
      ]
    }
  ]
}