test = {
  'name': '4.10',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you don't have a variable
          >>> # named inventory_dict. Maybe there's a typo?
          >>> 'inventory_dict' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # Something in inventory_dict is not correct.
          >>> inventory_dict == {'gold' : 500,'pouch' : ['flint', 'twine', 'gemstone'],'backpack' :['xylophone','dagger','bedroll','bread loaf']}
          True
          """
        }
      ]
    }
  ]
}