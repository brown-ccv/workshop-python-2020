test = {
  'name': '2.10',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # index_str.  Maybe there's a typo?
          >>> 'index_str' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The value assigned to index_str is
          >>> # not correct. 
          >>> index_str == sentence_str.find('are')
          True
          """
        }
      ]
    }
  ]
}