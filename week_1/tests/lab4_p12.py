test = {
  'name': '4.12',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like the key 'gold' does not exist.
          >>> # Maybe there's a typo?
          >>> 'gold' in inventory_dict
          True
          """
        },
        {
          'code': r"""
          >>> # The value of the key 'gold' is not correct.
          >>> inventory_dict['gold'] == 550
          True
          """
        }
      ]
    }
  ]
}