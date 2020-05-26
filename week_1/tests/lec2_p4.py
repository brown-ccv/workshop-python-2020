test = {
  'name': '2.4',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # my_name_str.  Maybe there's a typo?
          >>> 'my_name_str' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # a_str.  Maybe there's a typo?
          >>> 'a_str' in vars()
          True
          """
        },
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
          >>> # It looks like you didn't give anything the name
          >>> # d_str.  Maybe there's a typo?
          >>> 'c_str' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # d_str.  Maybe there's a typo?
          >>> 'd_str' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # e_str.  Maybe there's a typo?
          >>> 'e_str' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # The value assigned to my_name_str is
          >>> # not correct. 
          >>> my_name_str == 'Andras Zsom'
          True
          """
        },
        {
          'code': r"""
          >>> # The value assigned to a_str is
          >>> # not correct. 
          >>> a_str == my_name_str[-4]
          True
          """
        },
        {
          'code': r"""
          >>> # The value assigned to b_str is
          >>> # not correct. 
          >>> b_str == my_name_str[-4:]
          True
          """
        },
        {
          'code': r"""
          >>> # The value assigned to c_str is
          >>> # not correct. 
          >>> c_str == my_name_str[::2]
          True
          """
        },
        {
          'code': r"""
          >>> # The value assigned to d_str is
          >>> # not correct. 
          >>> d_str == my_name_str[::-3]
          True
          """
        },
        {
          'code': r"""
          >>> # The value assigned to e_str is
          >>> # not correct. 
          >>> e_str == my_name_str[2:6]
          True
          """
        },
      ]
    }
  ]
}