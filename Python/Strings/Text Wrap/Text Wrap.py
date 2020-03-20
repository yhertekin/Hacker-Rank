def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    wordlist = wrapper.wrap(string)
    return "\n".join(wordlist)