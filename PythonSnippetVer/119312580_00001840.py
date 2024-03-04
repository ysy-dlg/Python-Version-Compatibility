import sys
import select
import termios
import tty
def getkey():
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    answer = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
    return answer
print """Menu
1) Say Foo
2) Say Bar"""
answer=getkey()
if "1" in answer: print "foo"
elif "2" in answer: print "bar"