test = {
  'name': '4.1',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like 'smith' is not a key in phone_nums_dict
          >>> 'smith' in phone_nums_dict
          True
          """
        },
        {
          'code': r"""
          >>> # The value assigned to 'smith' is
          >>> # not correct. 
          >>> phone_nums_dict['smith'] == '307-821-7788'
          True
          """
        }
      ]
    }
  ]
}