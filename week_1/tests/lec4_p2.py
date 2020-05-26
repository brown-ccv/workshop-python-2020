test = {
  'name': '4.2',
  'suites': [
    {
      'cases': [
         {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # hometown_dict. Maybe there's a typo?
          >>> 'hometown_dict' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # It looks like 'Ashley Lee' is not a key in phone_nums_dict.
          >>> # Maybe there's a typo?
          >>> 'Ashley Lee' in hometown_dict
          True
          """
        },
        {
          'code': r"""
          >>> # It looks like 'Jenny Yang' is not a key in phone_nums_dict.
          >>> # Maybe there's a typo?
          >>> 'Jenny Yang' in hometown_dict
          True
          """
        },
        {
          'code': r"""
          >>> # The value assigned to 'Ashley Lee' is
          >>> # not correct. 
          >>> hometown_dict['Ashley Lee'] == 'McLean'
          True
          """
        },
        {
          'code': r"""
          >>> # The value assigned to 'Jenny Yang' is
          >>> # not correct. 
          >>> hometown_dict['Jenny Yang'] == 'Reston'
          True
          """
        }
      ]
    }
  ]
}