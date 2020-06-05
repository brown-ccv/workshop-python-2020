test = {
  'name': '6.4',
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your variable is not named correctly.
          >>> # Maybe there's a typo?
          >>> 'num_words_int' in vars()
          True
          """
        },
        {
          'code': r"""
          >>> # Your loop is off.
          >>> num_words_int == len(word_list)
          True
          """
        },
      ]
    }
  ]
}