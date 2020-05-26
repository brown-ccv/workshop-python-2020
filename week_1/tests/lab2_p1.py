test = {
  'name': '2.1',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # sentence_str.  Maybe there's a typo?
          >>> 'sentence_str' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The value assigned to sentence_str is
          >>> # not correct. 
          >>> sentence_str == 'All dogs are good and cool'
          True
          """
        }
      ]
    }
  ]
}