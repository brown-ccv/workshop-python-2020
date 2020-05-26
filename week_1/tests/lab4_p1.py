test = {
  'name': '4.1',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you don't have a variable
          >>> # named ages_dict. Maybe there's a typo?
          >>> 'ages_dict' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The key 'Ashley' does not exist. 
          >>> 'Ashley' in ages_dict
          True
          """
        },
        {
          'code': r"""
          >>> # The key 'Kurt' does not exist. 
          >>> 'Kurt' in ages_dict
          True
          """
        },
        {
          'code': r"""
          >>> # The key 'Emily' does not exist. 
          >>> 'Emily' in ages_dict
          True
          """
        },
        {
          'code': r"""
          >>> # The value assigned to 'Ashley' is
          >>> # not correct. 
          >>> ages_dict['Ashley'] == 30
          True
          """
        },
        {
          'code': r"""
          >>> # The value assigned to 'Kurt' is
          >>> # not correct. 
          >>> ages_dict['Kurt'] == 28
          True
          """
        },
        {
          'code': r"""
          >>> # The value assigned to 'Emily' is
          >>> # not correct. 
          >>> ages_dict['Emily'] == 33
          True
          """
        }
      ]
    }
  ]
}