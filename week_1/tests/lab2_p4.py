test = {
  'name': '2.4',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # c_str.  Maybe there's a typo?
          >>> 'c_str' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The value assigned to c_str is
          >>> # not correct. 
          >>> c_str == sentence_str[:2] + sentence_str[-2:]
          True
          """
        }
      ]
    }
  ]
}