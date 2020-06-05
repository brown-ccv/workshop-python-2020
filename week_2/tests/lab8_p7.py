test = {
  'name': '8.6',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like one of your variables is not named
          >>> # correctly. Maybe there's a typo?
          >>> 'groceries' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # It looks like one of your variables is not named
          >>> # correctly. Maybe there's a typo?
          >>> 'stock' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # It looks like one of your variables is not named
          >>> # correctly. Maybe there's a typo?
          >>> 'prices' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # There's something off with your groceries list.
          >>> groceries == ['banana', 'orange', 'apple']
          True
          """
        },
        {
          'code': r"""
          >>> # There's something off with your stock dict.
          >>> stock == {"banana": 6,"apple": 0,"orange": 32,"pear": 15}
          True
          """
        },
        {
          'code': r"""
          >>> # There's something off with your prices dict.
          >>> prices == {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}
          True
          """
        },
      ]
    }
  ]
}