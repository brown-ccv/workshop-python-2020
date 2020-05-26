test = {
  'name': '4.11',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like the key 'pocket' doesn't exist.
          >>> # Maybe there's a typo?
          >>> 'pocket' in inventory_dict
          True
          """
        },
        {
          'code': r"""
          >>> # The value of the key 'pocket' is not correct.
          >>> inventory_dict['pocket'] == ['seashell', 'strange berry', 'lint']
          True
          """
        }
      ]
    }
  ]
}