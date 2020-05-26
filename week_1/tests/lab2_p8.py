test = {
  'name': '2.8',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # catdog_str.  Maybe there's a typo?
          >>> 'catdog_str' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The value assigned to catdog_str is
          >>> # not correct. 
          >>> catdog_str == 'The dog said, "woof woof woof" and the cat answered, "hisshiss".'
          True
          """
        }
      ]
    }
  ]
}