import random
import string
import sys

def randomString(stringLength):
    """Generate a random string with the combination of lowercase and uppercase letters """
    symbols="!#$%&*?@"
    chars_allowed=""
    final_char_mix=""
    if("onlylower" in sys.argv):
    	chars_allowed=string.ascii_lowercase
    else:
    	chars_allowed=string.ascii_letters

    if("nosymbol" not in sys.argv):
    	final_char_mix= chars_allowed+symbols;
    else:
    	final_char_mix=chars_allowed

    return ''.join(random.choice(final_char_mix) for i in range(stringLength))
print (randomString(int(sys.argv[1])))
