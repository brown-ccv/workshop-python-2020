test = {
  'name': '2.3',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # b_str.  Maybe there's a typo?
          >>> 'b_str' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The value assigned to b_str is
          >>> # not correct. 
          >>> b_str == sentence_str[::-1]
          True
          """
        }
      ]
    }
  ]
}